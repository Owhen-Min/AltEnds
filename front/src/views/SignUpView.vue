<template>
  <div class="container-fluid bg-dark py-5" v-if="store">
    <div class="container">
      <div class="row justify-content-center align-items-center gx-5">
        <!-- 환영 메시지 섹션 -->
        <div class="col-lg-5 col-md-6 mb-4 mb-md-0">
          <div class="welcome-section text-center">
            <h1 class="gradient-text mb-4">환영합니다!</h1>
            <div class="welcome-image mb-4">
              <img src="http://127.0.0.1:8000/media/static/logo3.png/" alt="로고" class="img-fluid">
            </div>
            <p class="welcome-text mb-4">
              영화의 새로운 결말을 만들어보세요.<br>
              AI와 함께 당신만의 특별한 이야기를 시작하세요.
            </p>
            <div class="features">
              <div class="feature-item">
                <i class="bi bi-film"></i>
                <span>다양한 영화 컨텐츠</span>
              </div>
              <div class="feature-item">
                <i class="bi bi-robot"></i>
                <span>AI 기반 결말 생성</span>
              </div>
              <div class="feature-item">
                <i class="bi bi-people"></i>
                <span>커뮤니티 활동</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 회원가입 폼 섹션 -->
        <div class="col-lg-6 col-md-6">
          <div class="signup-card content-card">
            <h2 class="gradient-text text-center mb-4">회원가입</h2>
            
            <form @submit.prevent="signUp" class="signup-form">
              <div class="form-group mb-3">
                <label for="username" class="form-label">아이디</label>
                <input 
                  type="text" 
                  id="username" 
                  class="form-control" 
                  autocomplete="username" 
                  v-model.trim="username"
                  :class="{ 'is-invalid': errors.username }"
                >
                <div class="error-message" v-if="errors.username">{{ errors.username }}</div>
              </div>

              <div class="form-group mb-3">
                <label for="password1" class="form-label">비밀번호</label>
                <input 
                  type="password" 
                  id="password1" 
                  class="form-control" 
                  autocomplete="new-password" 
                  v-model.trim="password1"
                  :class="{ 'is-invalid': errors.password1 }"
                >
                <div class="error-message" v-if="errors.password1">{{ errors.password1 }}</div>
              </div>

              <div class="form-group mb-3">
                <label for="password2" class="form-label">비밀번호 확인</label>
                <input 
                  type="password" 
                  id="password2" 
                  class="form-control" 
                  autocomplete="new-password" 
                  v-model.trim="password2"
                  :class="{ 'is-invalid': errors.password2 }"
                >
                <div class="error-message" v-if="errors.password2">{{ errors.password2 }}</div>
              </div>

              <div class="form-group mb-3">
                <label for="firstname" class="form-label">이름</label>
                <input 
                  type="text" 
                  id="firstname" 
                  class="form-control" 
                  v-model.trim="firstname"
                  :class="{ 'is-invalid': errors.firstname }"
                >
                <div class="error-message" v-if="errors.firstname">{{ errors.firstname }}</div>
              </div>

              <div class="form-group mb-3">
                <label for="nickname" class="form-label">닉네임</label>
                <input 
                  type="text" 
                  id="nickname" 
                  class="form-control" 
                  v-model.trim="nickname"
                  :class="{ 'is-invalid': errors.nickname }"
                >
                <div class="error-message" v-if="errors.nickname">{{ errors.nickname }}</div>
              </div>

              <div class="form-group mb-4">
                <label for="email" class="form-label">이메일</label>
                <input 
                  type="email" 
                  id="email" 
                  class="form-control" 
                  v-model.trim="email"
                  :class="{ 'is-invalid': errors.email }"
                >
                <div class="error-message" v-if="errors.email">{{ errors.email }}</div>
              </div>

              <div class="d-grid">
                <button type="submit" class="btn btn-primary">회원가입</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movieStore';
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
.content-card {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  border-radius: 12px;
  padding: 2rem;
  color: white;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
}

.gradient-text {
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 700;
}

.form-label {
  color: rgba(255, 255, 255, 0.9);
  margin-bottom: 0.5rem;
}

.form-control {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: white;
  padding: 0.8rem;
  transition: all 0.3s ease;
}

.form-control:focus {
  background: rgba(255, 255, 255, 0.15);
  border-color: #ffb88c;
  box-shadow: 0 0 0 0.2rem rgba(255, 184, 140, 0.25);
  color: white;
}

.form-control::placeholder {
  color: rgba(255, 255, 255, 0.5);
}

.error-message {
  color: #ff6b6b;
  font-size: 0.875rem;
  margin-top: 0.5rem;
}

.btn {
  padding: 0.8rem;
  font-weight: 600;
  transition: all 0.3s ease;
}

.btn:hover {
  transform: translateY(-2px);
}

.btn-primary {
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  border: none;
}

.is-invalid {
  border-color: #ff6b6b !important;
}

.is-invalid:focus {
  box-shadow: 0 0 0 0.2rem rgba(255, 107, 107, 0.25) !important;
}

@media (max-width: 768px) {
  .content-card {
    padding: 1.5rem;
  }
  
  .form-control {
    padding: 0.6rem;
  }
}

.welcome-section {
  color: white;
  padding: 2rem;
}

.welcome-image {
  max-width: 200px;
  margin: 0 auto;
  transition: transform 0.3s ease;
}

.welcome-image:hover {
  transform: scale(1.05);
}

.welcome-text {
  font-size: 1.2rem;
  line-height: 1.8;
  color: rgba(255, 255, 255, 0.9);
}

.features {
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
  margin-top: 2rem;
}

.feature-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 8px;
  transition: transform 0.3s ease;
}

.feature-item:hover {
  transform: translateX(10px);
  background: rgba(255, 255, 255, 0.1);
}

.feature-item i {
  font-size: 1.5rem;
  color: #ffb88c;
}

.feature-item span {
  font-size: 1.1rem;
  color: rgba(255, 255, 255, 0.9);
}

h1.gradient-text {
  font-size: 2.5rem;
  margin-bottom: 1.5rem;
}

@media (max-width: 992px) {
  .welcome-section {
    padding: 1rem;
  }

  .welcome-image {
    max-width: 150px;
  }

  .welcome-text {
    font-size: 1.1rem;
  }

  .feature-item {
    padding: 0.8rem;
  }
}
</style>
