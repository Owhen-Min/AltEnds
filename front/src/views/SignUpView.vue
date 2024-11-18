<template>
  <div v-if="store">
    <h1>회원가입 페이지</h1>
    <form @submit.prevent="signUp">
      <label for="username">아이디 : </label>
      <input type="text" id="username" v-model.trim="username"><br>

      <label for="password1">비밀번호 : </label>
      <input type="text" id="password1" v-model.trim="password1"><br>
      
      <label for="password2">비밀번호 재입력 : </label>
      <input type="text" id="password2" v-model.trim="password2"><br>

      <label for="firstname">이름 : </label>
      <input type="text" id="firstname" v-model.trim="firstname"><br>

      <label for="nickname">닉네임 : </label>
      <input type="text" id="nickname" v-model.trim="nickname"><br>

      <label for="email">이메일 : </label>
      <input type="text" id="email" v-model.trim="email"><br>

      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/counter';
import { ref } from 'vue';

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const nickname = ref(null)
const firstname = ref(null)
const email = ref(null)

const store = useMovieStore()

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    firstname: firstname.value,
    email: email.value,
  }
  store.signUp(payload)
}

</script>

<style scoped>

</style>