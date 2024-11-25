<template>
  <div class="page flex justify-center items-center">
    <div class="login-container">
      <div class="left">
        <div class="login-title">Welcome!</div>
        <div class="eula">영화가 가진 다양한 <strong>가능성</strong>과 <br>이를 누릴 수 있는 <strong>커뮤니티</strong>를<br> <strong>즐겨보세요.</strong></div>
      </div>
      <div class="gutter"></div>
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
          <path ref="pathElement" d="m 40,120.00016 239.99984,-3.2e-4 c 0,0 24.99263,0.79932 25.00016,35.00016 0.008,34.20084 -25.00016,40 -25.00016,40 h -239.99984 c 0,-0.0205 -25,4.01348 -25,38.5 0,34.48652 25,38.5 25,38.5 h 215 c 0,0 20,-0.99604 20,-25 0,-24.00396 -20,-25 -20,-25 h -190 c 0,0 -20,1.71033 -20,25 0,24.00396 20,25 20,25 h 168.57143" />
        </svg>
        <form @submit.prevent="logIn" class="login-form">
          <div class="form-group">
            <label for="username">아이디:</label>
            <input 
              type="text" 
              id="username" 
              v-model.trim="username" 
              required 
              placeholder="아이디를 입력하세요" 
              @click="onUsernameFocus" 
              ref="usernameInput"
              class="form-input" 
            />
          </div>

          <div class="form-group">
            <label for="password">패스워드:</label>
            <input 
              type="password" 
              id="password" 
              v-model.trim="password" 
              required 
              placeholder="패스워드를 입력하세요" 
              @click="onPasswordFocus" 
              ref="passwordInput"
              class="form-input" 
            />
          </div>

          <button type="submit" class="btn-primary" :disabled="isLoading">
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
  min-height: 100vh;
  background: rgba(33, 37, 41, 1);
  color: #f2f2f2;
  display: flex;
  align-items: center;
  justify-content: center;
}
.login-container {
  width: 100%;
  max-width: 1000px;
  margin: 0 auto;
  padding: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  background: rgba(255, 255, 255, 0.05) !important;
  backdrop-filter: blur(10px);
  border: none;
  border-radius: 12px;
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
}
.left {
  background: rgba(255, 255, 255, 0.08);
  border-radius: 12px;
  padding: 2rem;
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
  .login-container {
    margin: 20px;
    padding: 20px;
  }
}
.login-title {
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 700;
  font-size: 50px;
  margin: 50px 40px 20px;
}
.eula {
  color: #e0e0e0;
  font-size: 16px;
  line-height: 1.5;
  margin: 40px;
  padding-bottom: 20px;

  strong {
    color: #ffb88c;
  }
}
.right {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  border-radius: 12px;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
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
  padding: 40px;
  position: relative;
  width: 100%;
  max-width: 400px;
}
.form-group {
  margin-bottom: 20px;

  label {
    display: block;
    margin-bottom: 8px;
    font-size: 14px;
    color: #c2c2c5;
  }
}
.form-input {
  background: rgba(255, 255, 255, 0.1);
  border: 2px solid #ffb88c;
  border-radius: 8px;
  font-size: 16px;
  padding: 8px 12px;
  width: 100%;
  color: #f2f2f2;
  transition: all 0.3s ease;

  &:focus {
    outline: none;
    box-shadow: 0 0 0 2px rgba(255, 184, 140, 0.5);
    border-color: #ff6b6b;
  }

  &::placeholder {
    color: rgba(255, 255, 255, 0.5);
  }
}
.btn-primary {
  width: 100%;
  padding: 12px;
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  color: white;
  cursor: pointer;
  transition: transform 0.3s ease;

  &:hover:not(:disabled) {
    transform: scale(1.05);
  }

  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
}
.gutter {
  width: 1px;
  height: 80%;
  background: linear-gradient(
    to bottom,
    transparent,
    #ffb88c,
    #ff6b6b,
    transparent
  );
  margin: 0 1rem;
}
@media (max-width: 767px) {
  .login-container {
    flex-direction: column;
    padding: 20px;
  }

  .gutter {
    width: 80%;
    height: 1px;
    margin: 1rem 0;
  }
}
</style>