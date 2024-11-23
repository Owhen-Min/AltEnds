<template>
  <div class="container-fluid py-3">
    <div class="row gx-5">
      <div class="col-lg-9 col-md-8 col-sm-12">
        <!-- 주간 영화 컴포넌트 -->
        <WeeklyMovies class="card"/>

        <div class="card mb-4">
          <EndingRanking />
        </div>
      </div>

      <div class="col-lg-3 col-md-4 col-sm-12">
        <div class="card mb-4 flex-grow-1">
          <div class="card-body row justify-content-center" id="user-management" v-if="isLogin">
            <div class="card-header">
              <h4>회원 정보</h4>
            </div>
            
            <img :src="store.BASE_URL + store.user.profile_picture" alt="" class="col-5">
            <p><strong>{{store.user.nickname}}</strong>님 안녕하세요!</p>
            <p>남은 토큰 : <strong>{{ store.user.token }}</strong></p>
            <button @click="goProfile(store.user.pk)" class="btn btn-link">마이 페이지</button>
            <button class="btn btn-link" @click="logOut">로그아웃</button>
          </div>
          <div class="card-body row" id="user-login" v-else>
            <RouterLink :to="{ name: 'Login' }" class="d-flex justify-content-center col-6">
              <button class="btn btn-link">로그인</button>
            </RouterLink>
            <RouterLink :to="{ name: 'SignUp' }" class="d-flex justify-content-center col-6">
              <button class="btn btn-link">회원가입</button>
            </RouterLink>
          </div>
        </div>

        <UserRanking class="card"/>
      </div>
    </div>
    <RouterLink :to="{ name: 'MovieSelect' }">
      <button class="btn btn-link">결말 비틀러 가기</button>
    </RouterLink>
  </div>
</template>

<script setup>
import router from '@/router';
import { useMovieStore } from '@/stores/counter';
import { computed } from 'vue';

import UserRanking from '@/components/UserRanking.vue';
import EndingRanking from '@/components/EndingRanking.vue';
import WeeklyMovies from '@/components/WeeklyMovies.vue';

const store = useMovieStore()

const isLogin = computed(() => store.isLogin)

const goProfile = function (userid) {
  router.push({ name: 'Profile', params: { userid: userid } })
}

const logOut = store.logOut
</script>

<style scoped>
.container-fluid {
  display: flex;
  flex-direction: column;
  background-color: #a0a0a57e; /* 배경색을 어둡게 변경 */
  padding: 20px; /* 패딩 추가 */
}

.container {
  display: flex;
  flex-direction: column;
  background-color: #a0a0a57e; /* 배경색을 어둡게 변경 */
  padding: 20px; /* 패딩 추가 */
}

.movie-section {
  margin-bottom: 20px;
}

.card-header {
  border-radius: 20px;
  background-color: #f8f9fa;
  font-weight: bold;
  text-align: center;
  padding: 17px;
  margin-bottom: 20px;
}

.card {
  background-color: #a0a0a5; /* 카드 배경색은 유지 */
  border: none;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.btn-link {
  color: #474A59; /* Consistent color with NavBar.vue */
  text-decoration: none;
  font-weight: 600;
}

.btn-link:hover {
  color: #007bff; /* Hover color */
}

@media (max-width: 767px) {
  .container {
    padding: 10px;
  }

}
#user-management {
    justify-content: center;
    text-align: center;
    padding-top: 0px;
    padding-bottom: 25px;
  }
</style>