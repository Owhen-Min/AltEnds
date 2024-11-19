<template>
  <div>
    <form @submit.prevent="logIn">
      <label for="username">아이디</label>
      <input type="text" id="username" v-model.trim="username"><br>

      <label for="password">패스워드</label>
      <input type="text" id="password" v-model.trim="password"><br>

      <input type="submit" value="로그인">
    </form>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/counter';
import { ref } from 'vue';

const store = useMovieStore()

const username = ref(null)
const password = ref(null)

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}

</script>

<style lang="scss" scoped>

</style>