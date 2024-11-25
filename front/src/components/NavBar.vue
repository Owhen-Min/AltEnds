<template>
  <nav class="nav-bar">
    <div class="nav-container row justify-content-around">
      <div class="pages col-sm-8 col-md-7 col-lg-5 justify-content-between align-items-center">
        <RouterLink :to="{ name: 'Home' }" class="logo-link">
          <img src="http://127.0.0.1:8000/media/static/logo3.png/" alt="홈" class="col-5 Logo">
        </RouterLink>
        <RouterLink :to="{ name: 'EndingList' }" class="nav-link col-3">AI 게시판</RouterLink>
        <RouterLink :to="{ name: 'Community' }" class="nav-link col-2">커뮤니티</RouterLink>
        <RouterLink :to="{ name: 'MovieList'}" class="nav-link col-2">영화정보</RouterLink>
        <RouterLink 
          v-if="store.user.is_admin" 
          :to="{ name: 'AdminMovieSelect' }" 
          class="nav-link"
        >
          영화관리
        </RouterLink>
      </div>
      <div class="d-none d-md-block col-md-1 col-lg-2"></div>
      <div class="d-flex userpages col-sm-4 col-md-3 justify-content-center align-items-center" v-if="isLogin">
        <button @click="goMyProfile" class="nav-btn">마이 페이지</button>
        <button @click="store.logOut" class="nav-btn">로그아웃</button>
      </div>
      <div class="d-flex userpages col-sm-4 col-md-3 justify-content-center align-items-center" v-else>
        <RouterLink :to="{ name: 'Login' }" class="nav-btn">로그인</RouterLink>
        <RouterLink :to="{ name: 'SignUp' }" class="nav-btn">회원가입</RouterLink>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { useMovieStore } from '@/stores/counter';
import { computed, onMounted, onUnmounted } from 'vue';
import { RouterLink, useRouter } from 'vue-router';

const router = useRouter();
const store = useMovieStore();
const isLogin = computed(() => store.isLogin);

const goMyProfile = function () {
  router.push({ name: 'Profile', params: { userid: store.user.pk } });
}

// 스크롤 이벤트 처리
onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})

const handleScroll = () => {
  const navbar = document.querySelector('.nav-bar')
  if (window.scrollY > 50) {
    navbar.classList.add('scrolled')
  } else {
    navbar.classList.remove('scrolled')
  }
}
</script>

<style scoped>
.nav-bar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background: rgba(17, 17, 17, 0.95);
  backdrop-filter: blur(10px);
  padding: 0.5rem 0;
  z-index: 1000;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
}

.nav-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 1rem;
}

.Logo {
  width: 100%;
  max-width: 80px;
  transition: transform 0.3s ease;
}

.logo-link:hover .Logo {
  transform: scale(1.05);
}

.pages {
  display: flex;
  align-items: center;
}

.nav-link {
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  text-align: center;
  font-weight: 600;
  margin-right: 15px;
  padding: 0.3rem 0.8rem;
  border-radius: 6px;
  font-size: 0.95rem;
  transition: all 0.3s ease;
}

.nav-link:hover, .nav-link.router-link-active {
  color: white;
  background: linear-gradient(45deg, rgba(255, 107, 107, 0.1), rgba(255, 184, 140, 0.1));
  transform: translateY(-2px);
}

.userpages {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.nav-btn {
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  font-weight: 600;
  background: none;
  border: none;
  padding: 0.3rem 0.8rem;
  border-radius: 6px;
  font-size: 0.95rem;
  transition: all 0.3s ease;
  cursor: pointer;
}

.nav-btn:hover {
  color: white;
  background: linear-gradient(45deg, rgba(255, 107, 107, 0.1), rgba(255, 184, 140, 0.1));
  transform: translateY(-2px);
}

/* 반응형 디자인 */
@media (max-width: 768px) {
  .nav-link, .nav-btn {
    padding: 0.2rem 0.5rem;
    font-size: 0.85rem;
  }
  
  .Logo {
    max-width: 60px;
  }
}

/* 스크롤 시 네비게이션 바 스타일 변경을 위한 클래스 */
.nav-bar.scrolled {
  background: rgba(17, 17, 17, 0.98);
  padding: 0.3rem 0;
}
</style>