<template>
    <RouterLink :to="{ name: 'MovieSelect' }">
      <button class="btn btn-primary col-12">
        영화 비틀러 가기
      </button>
    </RouterLink>
</template>
  
  <script setup>
  import { RouterLink } from 'vue-router';
  </script>
  
  <style scoped>
  .btn-primary {
    background: linear-gradient(45deg, #ff6b6b, #ffb88c);
    border: none;
    transition: transform 0.3s ease;
  }
  
  .btn-primary:hover {
    transform: scale(1.05);
  }
  
  a {
    color: white;
    text-decoration: none;
  }
  </style>