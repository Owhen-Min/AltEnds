<template>
  <div class="login-container">
    <h1 class="login-title">로그인</h1>
    <form @submit.prevent="logIn" class="login-form">
      <div class="form-group">
        <label for="username">아이디:</label>
        <input type="text" id="username" v-model.trim="username" required placeholder="아이디를 입력하세요" />
      </div>

      <div class="form-group">
        <label for="password">패스워드:</label>
        <input type="password" id="password" v-model.trim="password" required placeholder="패스워드를 입력하세요" />
      </div>

      <button type="submit" class="btn btn-primary" :disabled="isLoading">
        {{ isLoading ? '로그인 중...' : '로그인' }}
      </button>
    </form>

  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useMovieStore } from '@/stores/counter';


const username = ref('');
const password = ref('');
const isLoading = ref(false);
const store = useMovieStore()


const logIn = async () => {
  isLoading.value = true;
  try {
    const payload = { username: username.value, password: password.value };
    store.logIn(payload); // Call the store's login method
  } finally {
    isLoading.value = false; // Reset loading state
  }
};
</script>

<style lang="scss" scoped>
.login-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.login-title {
  text-align: center;
  margin-bottom: 20px;
  color: #333;
}

.login-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

label {
  margin-bottom: 5px;
  font-weight: bold;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
}

input[type="text"]:focus,
input[type="password"]:focus {
  border-color: #007bff;
  outline: none;
}

.btn {
  padding: 10px;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  background-color: #007bff;
  color: white;
  transition: background-color 0.3s;

  &:hover {
    background-color: #0056b3;
  }

  &:disabled {
    background-color: #007bff;
    opacity: 0.6;
    cursor: not-allowed;
  }
}
</style>
