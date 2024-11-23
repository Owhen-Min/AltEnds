<template>
  <nav class="nav-bar">
    <div class="row justify-content-around">
      <div class="pages col-sm-8 col-md-7 col-lg-5 justify-content-between align-items-center">
        <RouterLink :to="{ name: 'Home' }">
          <img src="http://127.0.0.1:8000/media/static/logo2.png/" alt="홈" class="col-5 Logo">
        </RouterLink>
        <RouterLink :to="{ name: 'EndingList' }" class="nav-link col-3">AI 게시판</RouterLink>
        <RouterLink :to="{ name: 'Community' }" class="nav-link col-2">커뮤니티</RouterLink>
        <RouterLink :to="{ name: 'MovieList'}" class="nav-link col-2">영화정보</RouterLink>
      </div>
      <div class="d-none d-md-block col-md-1 col-lg-2"></div>
      <div class="d-flex userpages col-sm-3 col-md-2 justify-content-between align-items-center" v-if="isLogin">
        <button @click="goMyProfile" class="btn btn-link">마이 페이지</button>
        <button @click="store.logOut" class="btn btn-link">로그아웃</button>
      </div>
      <div class="d-flex userpages col-sm-4 col-md-3 justify-content-center align-items-center" v-else>
        <RouterLink :to="{ name: 'Login' }" class="btn btn-link">로그인</RouterLink>
        <RouterLink :to="{ name: 'SignUp' }" class="btn btn-link">회원가입</RouterLink>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { useMovieStore } from '@/stores/counter';
import { computed } from 'vue';
import { RouterLink, useRouter } from 'vue-router';

const router = useRouter();
const store = useMovieStore();
const isLogin = computed(() => store.isLogin);

const goMyProfile = function () {
  router.push({ name: 'Profile', params: { userid: store.user.pk } });
}
</script>

<style scoped>
.Logo {
  width: 100%;
  max-width: 100px;
}

.nav-bar {
  position: sticky; /* Makes the navbar stick to the top */
  top: 0; /* Position the navbar at the top */
  background-color: #e2e2e5; /* 회색 배경으로 변경 */
  padding: 1rem; /* Add some padding */
  z-index: 1000; /* Ensure it stays above other content */
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Add shadow for depth */
}

.pages {
  display: flex;
  align-items: center;
}

.nav-link {
  color: #474A59; /* Consistent color with Sample.vue and LoginView.vue */
  text-decoration: none;
  text-align: center;
  font-weight: 600;
  margin-right: 20px; /* 간격 추가 */
}

.nav-link:hover {
  color: #007bff; /* Hover color */
}

.userpages {
  display: flex;
  align-items: center;
}

.btn-link {
  color: #474A59; /* Consistent color with Sample.vue and LoginView.vue */
  text-decoration: none;
  font-weight: 600;
}

.btn-link:hover {
  color: #007bff; /* Hover color */
}
</style>