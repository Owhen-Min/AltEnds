<template>
  <nav class="nav-bar">
    <div class="row">
      <div class="pages col-6 justify-content-start">
        <RouterLink to="/">Home</RouterLink> |
        <RouterLink to="/aiboard">AI 게시판</RouterLink> |
        <RouterLink to="/community">커뮤니티</RouterLink> |
        <RouterLink :to="{name:'movielist'}">영화 정보</RouterLink>
      </div>
      <div class="d-flex userpages col-6 justify-content-end" v-if="isUserLogin">
        <RouterLink :to="{name:'profile'}">마이 프로필</RouterLink>
      </div>
      <div class="d-flex userpages col-6 justify-content-end" v-else>
        <RouterLink :to="{name: 'login'}">로그인</RouterLink>
        <span class="mx-2"> | </span>
        <RouterLink :to="{name:'signup'}">회원가입</RouterLink>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { RouterLink } from 'vue-router';
const isUserLogin = false
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