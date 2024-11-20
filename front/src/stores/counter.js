import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'


export const useMovieStore = defineStore('movie', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })
  const user = ref(null)
  const router = useRouter()
  const showModal = ref(false); // Modal visibility state
  const errorMessage = ref(''); // Error message state

  const signUp = function (payload) {
    const { username, password1, password2, firstname, nickname, email } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, firstname, nickname, email 
      }
    })
      .then((response) => {
        const password = password1
        // const payload = {
        //   username, password
        // }
        logIn({ username, password })
      })
      .catch((error) => {
        console.log(error)
      })
  }

  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`, 
      data: {
        username, password
      }
    })
      .then((response) => {
        token.value = response.data.key
      })
      .then(() => {
        axios({
          method: 'get',
          url: `${API_URL}/accounts/user/`,
          headers: {
            Authorization: `Token ${token.value}`,
          },
        })
          .then((response) => {
            axios({
              method: 'get',
              url: `${API_URL}/accounts/${response.data.pk}/`,
              headers: {
                Authorization: `Token ${token.value}`,
              },
            })
            .then((response) => {
              user.value = response.data
            })
          })
          .catch((error) => {
            console.log(error)
          })
      })
      .then(() => {
        router.push({ name: 'Home' })
      })
      .catch((error) => {
        errorMessage.value = '로그인 실패: 아이디나 패스워드를 확인하세요.';
        showModal.value = true;
      })
      
      
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((response) => {
        console.log(response.data)
        token.value = null,
        router.push({ name: 'Home' })
      })
      .catch((error) => {
        console.log(error)
      })
  }

  const getProfile = function (username) {
    axios({
      method: 'get',
      url: `${API_URL}/accounts/user/${username}/`,
    })
      .then((response) => {
        return response.data
      })
      .catch((error) => {
        console.log(error)
      })
  }

  const likes = function (articleid) {
    axios({
      method: 'post',
      url: `/articles/${articleid}/likes/`,
    })
      .then((response) => {
        return response.data.is_liked
      })
      .catch((error) => {
        console.log(error)
      })

  }
  return { API_URL, token, isLogin, signUp, logIn, showModal, errorMessage, logOut, getProfile, likes, user}
})
