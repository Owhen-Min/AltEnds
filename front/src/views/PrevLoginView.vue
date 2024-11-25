<template>
  <div class="page flex justify-center items-center container-fluid">
    <div class="container">
      <div class="left">
        <div class="login-title">Welcome!</div>
        <div class="eula">영화가 가진 다양한 <strong>가능성</strong>과 <br>이를 누릴 수 있는 <strong>커뮤니티</strong>를<br> <strong>즐겨보세요.</strong></div>
      </div>
      <div class="right">
        <svg viewBox="0 0 320 300">
          <defs>
            <linearGradient
              id="linearGradient"
              x1="13"
              y1="193.49992"
              x2="307"
              y2="193.49992"
              gradientUnits="userSpaceOnUse">
              <stop style="stop-color:#ff00ff;" offset="0" />
              <stop style="stop-color:#ff0000;" offset="1" />
            </linearGradient>
          </defs>
          <path ref="pathElement" d="m 40,120.00016 239.99984,-3.2e-4 c 0,0 24.99263,0.79932 25.00016,35.00016 0.008,34.20084 -25.00016,35 -25.00016,35 h -239.99984 c 0,-0.0205 -25,4.01348 -25,38.5 0,34.48652 25,38.5 25,38.5 h 215 c 0,0 20,-0.99604 20,-25 0,-24.00396 -20,-25 -20,-25 h -190 c 0,0 -20,1.71033 -20,25 0,24.00396 20,25 20,25 h 168.57143" />
        </svg>
        <form @submit.prevent="logIn" class="login-form">
          <div class="form-group">
            <label for="username">아이디:</label>
            <input type="text" id="username" v-model.trim="username" required placeholder="아이디를 입력하세요" @click="onUsernameFocus" ref="usernameInput" />
          </div>

          <div class="form-group">
            <label for="password">패스워드:</label>
            <input type="password" id="password" v-model.trim="password" autocomplete="current-password" required placeholder="패스워드를 입력하세요" @click="onPasswordFocus" ref="passwordInput" />
          </div>

          <button type="submit" class="btn btn-warning" :disabled="isLoading">
            {{ isLoading ? '로그인 중...' : '로그인' }}
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import { useMovieStore } from '@/stores/movieStore';
import anime from 'animejs';

const username = ref('');
const password = ref('');
const isLoading = ref(false);
const store = useMovieStore();
let current = null;

// 템플릿에 정의된 ref를 사용하여 DOM 요소에 접근
const usernameInput = ref(null);
const passwordInput = ref(null);
const submitButton = ref(null);
const pathElement = ref(null);

const logIn = async () => {
  isLoading.value = true;
  try {
    const payload = { username: username.value, password: password.value };
    await store.logIn(payload); // 스토어의 로그인 메서드 호출
  } finally {
    isLoading.value = false; // 로딩 상태 리셋
  }
};

// 애니메이션 함수
const animatePath = (offsetValue, dashArray) => {
  if (current) current.pause();
  current = anime({
    targets: pathElement.value,
    strokeDashoffset: {
      value: offsetValue,
      duration: 700,
      easing: 'easeOutQuart'
    },
    strokeDasharray: {
      value: dashArray,
      duration: 700,
      easing: 'easeOutQuart'
    }
  });
};

// 이벤트 핸들러 등록
const onUsernameFocus = () => {
  animatePath(0, '240 1386');
};

const onPasswordFocus = () => {
  animatePath(-336, '240 1386');
};

const onSubmitFocus = () => {
  animatePath(-730, '530 1386');
};

onMounted(() => {
  if (usernameInput.value) {
    usernameInput.value.addEventListener('focus', onUsernameFocus);
  }
  if (passwordInput.value) {
    passwordInput.value.addEventListener('focus', onPasswordFocus);
  }
  if (submitButton.value) {
    submitButton.value.addEventListener('focus', onSubmitFocus);
  }
});

onBeforeUnmount(() => {
  if (usernameInput.value) {
    usernameInput.value.removeEventListener('focus', onUsernameFocus);
  }
  if (passwordInput.value) {
    passwordInput.value.removeEventListener('focus', onPasswordFocus);
  }
  if (submitButton.value) {
    submitButton.value.removeEventListener('focus', onSubmitFocus);
  }
});
</script>

<style lang="scss" scoped>
@import url('https://rsms.me/inter/inter-ui.css');

::selection {
  background: #2D2F36;
}
::-webkit-selection {
  background: #2D2F36;
}
::-moz-selection {
  background: #2D2F36;
}
body {
  background: white;
  font-family: 'Inter UI', sans-serif;
  margin: 0;
  padding: 20px;
}
.page {
  background: #a0a0a5; /* 배경색을 약간 더 어둡게 변경 */
  flex-direction: column;
  height: calc(95% - 40px);
  position: absolute;
  place-content: center;
  width: calc(100% - 40px);
}
@media (max-width: 767px) {
  .page {
    height: auto;
    margin-bottom: 20px;
    padding-bottom: 20px;
  }
}
.container {
  display: flex;
  height: 320px;
  margin: 0 auto;
  width: 640px;
}
@media (max-width: 767px) {
  .container {
    flex-direction: column;
    height: 630px;
    width: 320px;
  }
}
.left {
  background: white;
  height: calc(100% - 40px);
  top: 20px;
  position: relative;
  width: 50%;
}
@media (max-width: 767px) {
  .left {
    height: 100%;
    left: 20px;
    width: calc(100% - 40px);
    max-height: 270px;
  }
}
.login-title {
  font-size: 50px;
  font-weight: 900;
  margin: 50px 40px 20px;
  color: #474A59;
}
.eula {
  color: #999;
  font-size: 16px;
  line-height: 1.5;
  margin: 40px;
  padding-bottom: 20px;
}
.right {
  background: #474A59;
  box-shadow: 0px 0px 40px 16px rgba(0,0,0,0.22);
  color: #F1F1F2;
  position: relative;
  width: 50%;
}
@media (max-width: 767px) {
  .right {
    flex-shrink: 0;
    height: 100%;
    width: 100%;
    max-height: 350px;
  }
}
svg {
  position: absolute;
  width: 320px;
}
path {
  fill: none;
  stroke: url(#linearGradient);
  stroke-width: 4;
  stroke-dasharray: 240 1386;
}
.login-form {
  margin: 40px;
  position: absolute;
  width: calc(100% - 80px);
}
.form-group {
  margin-bottom: 15px;
}
label {
  color: #c2c2c5;
  display: block;
  font-size: 14px;
  height: 16px;
  margin-top: 20px;
  margin-bottom: 5px;
}
input[type="text"],
input[type="password"]{
  background: transparent !important;
  border: none;
  font-size: 20px;
  height: 30px;
  line-height: 30px;
  width: 100%;
  color: #f2f2f2;
}


.btn {
  padding: 10px;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  background-color: #707075;
  color: #f2f2f2;
  transition: background-color 0.3s;
}
.btn:hover {
  background-color: #0056b3;
}
.btn:disabled {
  background-color: #007bff;
  opacity: 0.6;
  cursor: not-allowed;
}
.btn:focus {
  color: #f2f2f2;
}
.btn:active {
  color: #d0d0d2;
}
#submit {
  color: #707075;
  margin-top: 40px;
  transition: color 300ms;
}
#submit:focus {
  color: #f2f2f2;
}
#submit:active {
  color: #d0d0d2;
}
</style>