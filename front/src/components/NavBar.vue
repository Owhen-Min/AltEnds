<template>
  <nav class="nav-bar">
    <RouterLink to="/">Home</RouterLink> |
    <RouterLink to="/aiboard">AI 게시판</RouterLink> |
    <RouterLink to="/community">커뮤니티</RouterLink> |
    <RouterLink :to="{name:'movielist'}">영화 정보</RouterLink>
  </nav>
</template>

<script setup>
import { RouterLink } from 'vue-router';
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