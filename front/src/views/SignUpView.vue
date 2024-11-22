<template>
  <div v-if="store">
    <h1>회원가입 페이지</h1>
    <form @submit.prevent="signUp">
      <div>
        <label for="username">아이디 :</label>
        <input type="text" id="username" autocomplete="username" v-model.trim="username">
        <p class="error" v-if="errors.username">{{ errors.username }}</p>
      </div>

      <div>
        <label for="password1">비밀번호 :</label>
        <input type="password" id="password1" autocomplete="new-password" v-model.trim="password1">
        <p class="error" v-if="errors.password1">{{ errors.password1 }}</p>
      </div>

      <div>
        <label for="password2">비밀번호 재입력 :</label>
        <input type="password" id="password2" autocomplete="new-password"v-model.trim="password2">
        <p class="error" v-if="errors.password2">{{ errors.password2 }}</p>
      </div>

      <div>
        <label for="firstname">이름 :</label>
        <input type="text" id="firstname" v-model.trim="firstname">
        <p class="error" v-if="errors.firstname">{{ errors.firstname }}</p>
      </div>

      <div>
        <label for="nickname">닉네임 :</label>
        <input type="text" id="nickname" v-model.trim="nickname">
        <p class="error" v-if="errors.nickname">{{ errors.nickname }}</p>
      </div>

      <div>
        <label for="email">이메일 :</label>
        <input type="text" id="email" v-model.trim="email">
        <p class="error" v-if="errors.email">{{ errors.email }}</p>
      </div>

      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/counter';
import { ref } from 'vue';

const username = ref(null);
const password1 = ref(null);
const password2 = ref(null);
const nickname = ref(null);
const firstname = ref(null);
const email = ref(null);
const errors = ref({}); // Track validation errors

const store = useMovieStore();

const validateForm = () => {
  errors.value = {}; // Clear previous errors

  if (!username.value) errors.value.username = "아이디를 입력하세요.";
  if (!password1.value) errors.value.password1 = "비밀번호를 입력하세요.";
  if (!password2.value) errors.value.password2 = "비밀번호를 재입력하세요.";
  if (password1.value && password2.value && password1.value !== password2.value) {
    errors.value.password2 = "비밀번호가 일치하지 않습니다.";
  }
  if (!firstname.value) errors.value.firstname = "이름을 입력하세요.";
  if (!nickname.value) errors.value.nickname = "닉네임을 입력하세요.";
  if (!email.value) errors.value.email = "이메일을 입력하세요.";

  return Object.keys(errors.value).length === 0; // Return true if no errors
};

const signUp = function () {
  if (!validateForm()) {
    return; // Stop form submission if validation fails
  }

  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    firstname: firstname.value,
    email: email.value,
  };
  store.signUp(payload);
};
</script>

<style scoped>
.error {
  color: red;
  font-size: 0.875em;
  margin-top: 4px;
}
</style>
