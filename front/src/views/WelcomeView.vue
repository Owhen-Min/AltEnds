<template>
  <div class="container-fluid bg-dark py-5">
    <div class="container">
      <div class="row g-4">
        <!-- 메인 소개 섹션 -->
        <div class="col-lg-6">
          <section class="intro-section content-card h-100 d-flex justify-content-center align-items-center">
            <div class="intro-content text-center w-100">
              <h1 class="intro text-white text-center mb-4 feature-card">영화의 새로운 가능성을 열다</h1>
              <img src="/logo.png" alt="로고" class="intro intro-logo mb-4">
              <p class="intro lead mb-4">
                AI와 함께 기존의 영화를 비틀어보세요.<br>
                새로운 이야기로 영화를 다시 한 번 즐겨보세요.
              </p>
            </div>
          </section>
        </div>

        <!-- 주요 기능 소개 -->
        <div class="col-lg-6">
          <section class="features-section content-card h-100">
            <div class="row g-4">
              <div class="col-12">
                <div class="feature-card h-100">
                  <i class="bi bi-robot feature-icon"></i>
                  <h3 class="gradient-text">AI 기반 결말 생성</h3>
                  <p>인공지능이 여러분의 상상대로<br>영화의 새로운 결말을 만들어드립니다.</p>
                </div>
              </div>
              
              <div class="col-12">
                <div class="feature-card h-100">
                  <i class="bi bi-people feature-icon"></i>
                  <h3 class="gradient-text">커뮤니티 활동</h3>
                  <p>다른 사용자들과 함께 자유로운 생각들을 나누고<br>새로운 관점을 발견하세요.</p>
                </div>
              </div>
              
              <div class="col-12">
                <div class="feature-card h-100">
                  <i class="bi bi-heart feature-icon"></i>
                  <h3 class="gradient-text">공유와 소통</h3>
                  <p>나만의 결말을 공유하고<br>다른 사용자들의 창의적인 아이디어를 확인해보세요.</p>
                </div>
              </div>
            </div>
          </section>
        </div>
      </div>

      <!-- 시작하기 섹션 -->
      <section class="cta-section content-card text-center mt-3">
        <h2 class="gradient-text mb-4">지금 시작해보세요</h2>
        <div class="cta-buttons">
          <RouterLink :to="{ name: 'SignUp' }" class="btn btn-primary mx-2">회원가입</RouterLink>
          <RouterLink :to="{ name: 'Login' }" class="btn btn-warning mx-2">로그인</RouterLink>
        </div>
      </section>
    </div>

    <!-- 회원가입 모달 추가 -->
    <Teleport to="body">
      <div v-if="showSignUpModal" class="modal-overlay" @click.self="showSignUpModal = false">
        <div class="modal-container">
          <button class="modal-close" @click="showSignUpModal = false">
            <i class="bi bi-x-lg"></i>
          </button>
          <SignUpForm @close="showSignUpModal = false" />
        </div>
      </div>
    </Teleport>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import SignUpForm from '@/components/SignUpForm.vue';

const showSignUpModal = ref(false);
</script>

<style scoped>
.content-card {
  background: rgba(255, 255, 255, 0.05) !important;
  backdrop-filter: blur(10px);
  border: none;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
}

.gradient-text {
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 700;
}

.intro:hover {
  transform: translateY(-10px);
  transition: transform 0.3s ease;
}

.intro-logo {
  width: 100%;
  max-width: 300px;
  height: auto;
  margin: 10px auto;
  display: block;
}

.lead {
  color: #e0e0e0;
  font-size: 1.2rem;
  line-height: 1.8;
}

.feature-card {
  text-align: center;
  transition: transform 0.3s ease;
  word-break: keep-all;
  word-wrap: break-word;
  padding: 1rem;
  margin-bottom: 1rem;
}

.feature-card:hover {
  transform: translateY(-10px);
}

.feature-icon {
  font-size: 2.5rem;
  color: #ffb88c;
  margin-bottom: 1rem;
}

.feature-card p {
  color: #e0e0e0;
  font-size: 1.1rem;
  white-space: pre-line;
}

.btn {
  padding: 0.8rem 2rem;
  font-weight: 600;
  transition: all 0.3s ease;
}

.btn:hover {
  transform: scale(1.05);
}

.btn-primary {
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  border: none;
}

.btn-warning {
  background: rgba(255, 255, 255, 0.1);
  border: 2px solid #ffb88c;
  color: white;
}

.btn-warning:hover {
  background: rgba(255, 255, 255, 0.2);
}

@media (max-width: 768px) {
  .content-card {
    padding: 1.5rem;
  }
  
  .lead {
    font-size: 1.1rem;
  }
  
  .feature-card {
    margin-bottom: 1rem;
  }
}

.container {
  margin-top: 1.4rem;
}

@media (max-width: 992px) {
  .col-lg-6 {
    margin-bottom: 2rem;
  }
}
</style> 