<template>
  <div class="container-fluid bg-dark py-5">
    <div class="container">
      <div class="row gx-5">
        <!-- 메인 컨텐츠 영역 -->
        <div class="col-lg-9 col-md-8 col-sm-12">
          <WeeklyMovies/>
          <EndingRanking class="content-card"/>
        </div>

        <!-- 사이드바 영역 -->
        <div class="col-lg-3 col-md-4 col-sm-12">
          <!-- 유저 정보 카드 -->
          <div class="content-card user-card mb-4">
            <div class="card-body" id="user-management" v-if="isLogin">
              <h4 class="gradient-text mb-4">회원 정보</h4>
              <img 
                :src="store.BASE_URL + store.user.profile_picture" 
                alt="" 
                class="profile-image mb-3"
              >
              <p class="user-name"><strong>{{store.user.nickname}}</strong>님 안녕하세요!</p>
              <p class="token-info">남은 토큰 : <strong>{{ store.user.token }}</strong></p>
              <div class="button-group">
                <button @click="goProfile(store.user.pk)" class="btn btn-primary">마이 페이지</button>
                <button class="btn btn-warning" @click="logOut">로그아웃</button>
              </div>
            </div>
            <div class="card-body text-center" id="user-login" v-else>
              <RouterLink :to="{ name: 'Login' }" class="btn btn-primary">로그인</RouterLink> <br>
              <RouterLink :to="{ name: 'SignUp' }" class="btn btn-warning">회원가입</RouterLink>
            </div>
          </div>

          <!-- 랭킹 & 버튼 -->
          <UserRanking class="content-card mb-4"/>
          <EndingTwistButton class="col-12"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import router from '@/router';
import { useMovieStore } from '@/stores/movieStore';
import { computed } from 'vue';

import UserRanking from '@/components/UserRanking.vue';
import EndingRanking from '@/components/EndingRanking.vue';
import WeeklyMovies from '@/components/WeeklyMovies.vue';
import EndingTwistButton from '@/components/EndingTwistButton.vue';
import { onMounted } from 'vue';
const store = useMovieStore()

const isLogin = computed(() => store.isLogin)

onMounted(() => {
  store.getMyProfile()
})
const goProfile = function (userid) {
  router.push({ name: 'Profile', params: { userid: userid } })
}

const logOut = store.logOut
</script>

<style scoped>
.content-card {
  background: rgba(255, 255, 255, 0.05) !important;
  backdrop-filter: blur(10px);
  border: none;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
}

.gradient-text {
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 700;
}

.user-card {
  text-align: center;
  color: white;
  margin-top: 1.8rem;
}

.profile-image {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid rgba(255, 184, 140, 0.5);
}

.user-name {
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
}

.token-info {
  color: #ffb88c;
  font-size: 0.95rem;
  margin-bottom: 1.5rem;
}

.button-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.btn {
  padding: 0.5rem 1.5rem;
  transition: all 0.3s ease;
}

.btn:hover {
  transform: scale(1.05);
}

.btn-primary {
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  border: none;
  padding: 8px 33px;
  margin-bottom: 10px;
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
    padding: 1rem;
  }
  
  .profile-image {
    width: 80px;
    height: 80px;
  }
}
</style>