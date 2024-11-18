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
  const router = useRouter()

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
        LoginView({ username, password })
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
      .catch((error) => {
        console.log(error)
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
        router.push({ name: 'HomeView' })
      })
      .catch((error) => {
        console.log(error)
      })
  }
  return { API_URL, isLogin, signUp, logIn, logOut }
})
