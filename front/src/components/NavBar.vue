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

</style>