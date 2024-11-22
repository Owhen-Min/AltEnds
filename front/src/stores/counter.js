import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'


export const useMovieStore = defineStore('movie', () => {
  const BASE_URL = 'http://127.0.0.1:8000'
  const API_VER = '/api/v1'
  const API_URL = BASE_URL + API_VER
  const token = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })
  const user = ref(null)
  const weeklyMovie = ref([])
  const router = useRouter()
  const showModal = ref(false); // Modal visibility state
  const errorTitle = ref('')
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
        logIn({ username, password1 })
      })
      .catch((error) => {
        errorTitle.value = '회원가입 실패'
        errorMessage.value = Object.values(error.response.data).flat().join('<br>')
        showModal.value = true;
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
        errorTitle.value = '로그인 실패';
        errorMessage.value = '아이디나 패스워드를 확인하세요.';
        showModal.value = true;
      })
      
      
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((response) => {
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

  const getMovies = function () {
    axios({
      method: 'get',
      url: `${API_URL}/movies/`,
    })
      .then((response) => {
        weeklyMovie.value = response.data
      })
      .catch((error) => {
        errorTitle.value = '주간영화 가져오기 실패'
        errorMessage.value = Object.values(error.response.data).flat().join('<br>')
        showModal.value = true;
      })
  }

  return { BASE_URL, API_VER, API_URL, token, isLogin, signUp, logIn, showModal, errorTitle, errorMessage, logOut, getProfile, user, getMovies, weeklyMovie }
}, {persist: true})
