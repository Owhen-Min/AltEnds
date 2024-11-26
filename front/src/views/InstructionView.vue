<template>
  <div class="container-fluid bg-dark instruction-container">
    <div class="slides-container" :style="{ transform: `translateY(-${currentSection * 100}vh)` }">
      <!-- 섹션 1: 소개 -->
      <div class="slide-section">
        <section class="intro-section content-card">
          <div class="intro-content text-center">
            <h1 class="intro gradient-text text-center mb-4 feature-card">비틀러 이용 가이드</h1>
            <p class="intro lead mb-4 text-white">
              AI 영화 결말 생성 서비스 비틀러를<br>
              재미있게 이용하는 방법을 알려드릴게요!<br>
              스크롤을 내리거나 키보드 방향키를 눌러<br>
              페이지를 이동할 수 있어요!</p>
          </div>
        </section>
      </div>

      <!-- 섹션 2: 영화 검색 -->
      <div class="slide-section">
        <div class="content-card">
          <i class="bi bi-search feature-icon"></i>
          <h3 class="gradient-text">1. 영화 선택</h3>
          <div class="instruction-image">
            <img src="@/assets/images/movieselect1.gif" alt="영화 검색 방법" />
          </div>
          <p class="lead text-white">홈화면에서 원하는 영화를 선택하세요.<br>원하는 영화가 없다면, 커뮤니티 게시판에 남겨보세요!</p>
        </div>
      </div>

      <div class="slide-section">
        <div class="content-card">
          <i class="bi bi-search feature-icon"></i>
          <h3 class="gradient-text">1. 영화 선택</h3>
          <div class="instruction-image">
            <img src="@/assets/images/movieselect2.gif" alt="영화 검색 방법" />
          </div>
          <p class="lead text-white">아니면... 영화 목록에서 선택해도 되구요.</p>
        </div>
      </div>


      <!-- 섹션 3: 프롬프트 작성 -->
      <div class="slide-section">
        <div class="content-card">
          <i class="bi bi-pencil-square feature-icon"></i>
          <h3 class="gradient-text">2. 프롬프트 작성</h3>
          <div class="instruction-image">
            <img src="@/assets/images/promptinput.gif" alt="프롬프트 작성 방법" />
          </div>
          <p class="lead text-white">원하는 추가 상황을 입력해주세요.<br>매 생성 때마다 5개의 토큰이 소모된답니다!<br>그리고... 조금만 기다려주실래요?</p>
        </div>
      </div>

      <div class="slide-section">
        <div class="content-card">
          <i class="bi bi-pencil-square feature-icon"></i>
          <h3 class="gradient-text">2. 프롬프트 작성</h3>
          <div class="instruction-image">
            <img src="@/assets/images/promptreinput.gif" alt="프롬프트 작성 방법" />
          </div>
          <p class="lead text-white">결과가 마음에 안 든다면 수정사항을 알려주세요.<br>이 경우에도 5개의 토큰이 소모됩니다!<br>AI가 선택한 엔딩을 기반으로 다시 만들어줄거에요!</p>
        </div>
      </div>

      <!-- 섹션 4: 결과 확인 -->
      <div class="slide-section">
        <div class="content-card">
          <i class="bi bi-share feature-icon"></i>
          <h3 class="gradient-text">3. 결과 확인 및 공유</h3>
          <div class="instruction-image">
            <img src="@/assets/images/postending.gif" alt="결과 확인 및 공유 방법" />
          </div>
          <p class="lead text-white">결말이 마음에 든다면<br>제목으로 쓸 프롬프트와 내용이 될 엔딩을 골라<br>다른 사용자들과 공유해보세요.</p>
        </div>
      </div>

      <!-- 섹션 5: CTA -->
      <div class="slide-section">
        <section class="cta-section content-card text-center">
          <h2 class="text-white align-items-center">지금 바로 <RouterLink :to="{ name: 'MovieSelect' }" class="btn btn-primary mx-2">비틀러</RouterLink> 가기</h2>
        </section>
      </div>
    </div>

    <!-- 네비게이션 버튼 -->
    <div class="navigation-buttons">
      <button class="nav-btn prev" @click="prevSection" :disabled="currentSection === 0">
        <i class="bi bi-chevron-up"></i>
      </button>
      <button class="nav-btn next" @click="nextSection" :disabled="currentSection === 4">
        <i class="bi bi-chevron-down"></i>
      </button>
    </div>

    <!-- 페이지 인디케이터 -->
    <div class="page-indicators">
      <div v-for="n in 7" :key="n" 
           class="indicator" 
           :class="{ active: currentSection === n - 1 }"
           @click="goToSection(n - 1)">
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const currentSection = ref(0);
const totalSections = 7;

const nextSection = () => {
  if (currentSection.value < totalSections - 1) {
    currentSection.value++;
  }
};

const prevSection = () => {
  if (currentSection.value > 0) {
    currentSection.value--;
  }
};

const goToSection = (index) => {
  currentSection.value = index;
};

// 스크롤 관련 변수
let lastScrollTime = 0;
const scrollCooldown = 1000; // 스크롤 쿨다운 시간 (ms)

// 스크롤 이벤트 핸들러
const handleWheel = (e) => {
  const currentTime = new Date().getTime();
  
  // 쿨다운 체크
  if (currentTime - lastScrollTime < scrollCooldown) {
    return;
  }

  // 스크롤 방향 감지
  if (e.deltaY > 0) {
    nextSection();
  } else {
    prevSection();
  }

  lastScrollTime = currentTime;
};

// 터치 이벤트를 위한 변수
let touchStartY = 0;
const touchThreshold = 50; // 터치 민감도

// 터치 이벤트 핸들러
const handleTouchStart = (e) => {
  touchStartY = e.touches[0].clientY;
};

const handleTouchEnd = (e) => {
  const touchEndY = e.changedTouches[0].clientY;
  const touchDiff = touchStartY - touchEndY;

  const currentTime = new Date().getTime();
  if (currentTime - lastScrollTime < scrollCooldown) {
    return;
  }

  if (Math.abs(touchDiff) > touchThreshold) {
    if (touchDiff > 0) {
      nextSection();
    } else {
      prevSection();
    }
    lastScrollTime = currentTime;
  }
};

// 키보드 네비게이션
const handleKeydown = (e) => {
  const currentTime = new Date().getTime();
  if (currentTime - lastScrollTime < scrollCooldown) {
    return;
  }

  if (e.key === 'ArrowDown' || e.key === 'ArrowRight') {
    nextSection();
    lastScrollTime = currentTime;
  } else if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') {
    prevSection();
    lastScrollTime = currentTime;
  }
};

onMounted(() => {
  window.addEventListener('wheel', handleWheel, { passive: false });
  window.addEventListener('keydown', handleKeydown);
  window.addEventListener('touchstart', handleTouchStart);
  window.addEventListener('touchend', handleTouchEnd);
});

onUnmounted(() => {
  window.removeEventListener('wheel', handleWheel);
  window.removeEventListener('keydown', handleKeydown);
  window.removeEventListener('touchstart', handleTouchStart);
  window.removeEventListener('touchend', handleTouchEnd);
});
</script>

<style scoped>
.instruction-container {
  height: 100vh;
  overflow: hidden;
  position: relative;
  touch-action: none; /* 모바일에서 기본 스크롤 동작 방지 */
}

.slides-container {
  height: 100%;
  transition: transform 0.8s cubic-bezier(0.645, 0.045, 0.355, 1);
  will-change: transform; /* 성능 최적화 */
}

.slide-section {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 2rem;
}

.navigation-buttons {
  position: fixed;
  right: 2rem;
  top: 50%;
  transform: translateY(-50%);
  display: flex;
  flex-direction: column;
  gap: 1rem;
  z-index: 100;
}

.nav-btn {
  background: rgba(255, 255, 255, 0.1);
  border: none;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  cursor: pointer;
  transition: all 0.3s ease;
}

.nav-btn:hover:not(:disabled) {
  background: rgba(255, 255, 255, 0.2);
}

.nav-btn:disabled {
  opacity: 0.3;
  cursor: not-allowed;
}

.page-indicators {
  position: fixed;
  right: 2rem;
  top: 50%;
  transform: translateY(-50%);
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  z-index: 100;
}

.indicator {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.3);
  cursor: pointer;
  transition: all 0.3s ease;
}

.indicator.active {
  background: #ffb88c;
  transform: scale(1.2);
}

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

.instruction-image {
  margin: 1.5rem 0;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.instruction-image img {
  width: 100%;
  max-width: 500px;
  height: auto;
  display: block;
  margin: 0 auto;
}

.content-card {
  max-width: 600px;
  width: 90%;
  margin: 0 auto;
}

/* 모바일 대응을 위한 추가 스타일 */
@media (max-width: 768px) {
  .navigation-buttons {
    right: 1rem;
  }

  .page-indicators {
    right: 1rem;
  }

  .instruction-image img {
    max-width: 100%;
  }
}

.btn-primary {
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  border: none;
  transition: transform 0.3s ease;
  padding: 0rem 2rem;
  text-decoration: none;
  text-align: center;
  font-size: 2rem;
}

.btn-primary:hover {
  transform: scale(1.05);
}

</style> 