<template>
  <nav class="nav-bar">
    <div class="row">
      <div class="pages col-6 justify-content-start align-items-center">
        <RouterLink :to="{ name: 'Home' }">Home</RouterLink> |
        <RouterLink :to="{ name: 'EndingList' }">AI 게시판</RouterLink> |
        <RouterLink :to="{ name: 'Community' }">커뮤니티</RouterLink> |
        <RouterLink :to="{ name: 'MovieList'}">영화 정보</RouterLink>
      </div>
      <div class="d-flex userpages col-6 justify-content-end align-items-center" v-if="isLogin">
        <button @click="goMyProfile" class="btn btn-link">마이페이지</button>
        <button @click="logOut" class="btn btn-link">로그아웃</button>
      </div>
      <div class="d-flex userpages col-6 justify-content-end" v-else>
        <RouterLink :to="{ name: 'Login' }">로그인</RouterLink>
        <span class="mx-2"> | </span>
        <RouterLink :to="{ name: 'SignUp' }">회원가입</RouterLink>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { useMovieStore } from '@/stores/counter';
import axios from 'axios';
import { computed } from 'vue';
import { RouterLink, useRouter } from 'vue-router';

const router = useRouter()
const store = useMovieStore()
const isLogin = computed (() => {
  return store.isLogin
})

const goProfile = function (userid) {
  router.push({ name: 'Profile', params: { userid: userid } })
}

const goMyProfile = function () {
  axios({
    method: 'get',
    url: `${store.API_URL}/accounts/user/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((response) => {
      goProfile(response.data.pk)
    })
    .catch((error) => {
      console.log(error)
    })
}

const logOut = store.logOut
</script>

<style scoped>
.nav-bar {
  position: sticky; /* Makes the navbar stick to the top */
  top: 0; /* Position the navbar at the top */
  background-color: #f8f9fa; /* Light background for visibility */
  padding: 1rem; /* Add some padding */
  z-index: 1000; /* Ensure it stays above other content */
}
nav.a {
  text-decoration: none;
}
</style>