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
  const showModal = ref(false)
  const modalConfig = ref({
    title: '',
    message: '',
    type: 'error'
  })

  const showModalMessage = (title, message, type = 'error') => {
    modalConfig.value = {
      title,
      message,
      type
    }
    showModal.value = true
  }

  const closeModal = () => {
    showModal.value = false
    modalConfig.value = {
      title: '',
      message: '',
      type: 'error'
    }
  }

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
        logIn({ username, password })
      })
      .catch((error) => {
        showModalMessage(
          '회원가입 실패',
          Object.values(error.response.data).flat().join('<br>'),
          'error'
        )
      })
  }

  const logIn = function (payload) {
    const { username, password } = payload

    return axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`, 
      data: {
        username, password
      }
    })
      .then((response) => {
        token.value = response.data.key
        return axios({
          method: 'get',
          url: `${API_URL}/accounts/user/`,
          headers: {
            Authorization: `Token ${token.value}`,
          },
        })
      })
      .then((response) => {
        return axios({
          method: 'get',
          url: `${API_URL}/accounts/${response.data.pk}/`,
          headers: {
            Authorization: `Token ${token.value}`,
          },
        })
      })
      .then((response) => {
        user.value = response.data
        router.push({ name: 'Home' })
      })
      .catch((error) => {
        showModalMessage(
          '로그인 실패',
          '아이디나 패스워드를 확인하세요.',
          'error'
        )
        throw error;
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
        showModalMessage(
          '주간영화 가져오기 실패',
          Object.values(error.response.data).flat().join('<br>'),
          'error'
        )
      })
  }

  return { BASE_URL, API_VER, API_URL, token, isLogin, signUp, logIn, showModal, modalConfig, showModalMessage, closeModal, logOut, getProfile, user, getMovies, weeklyMovie }
}, {persist: true})
