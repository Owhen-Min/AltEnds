<template>
  <div class="container py-3">
    <div class="row gx-5">
      <div class="col-lg-9 col-md-8 col-sm-12">
        <div class="card mb-4">
          <h2 class="card-header">이번 주 영화</h2>
          <div class="card-body">
            <div v-for="(movie, index) in movies" :key="index" class="movie-card">
              <RouterLink :to="{ name: 'MovieListDetail', params: { movieid: 1 } }">
                <h4>{{ movie }}</h4>
              </RouterLink>
              <hr />
            </div>
          </div>
        </div>

        <div class="card mb-4">
          <h2 class="card-header">대체 결말 랭킹</h2>
          <div class="card-body">
            <div class="row">
              <div @click="goEndingDetail(1)" class="ranking-card col-4" v-for="altend in altEndRanking" :key="altend.movie">
                <h5>영화: {{ altend.movie }}</h5>
                <p>대체 결말: {{ altend.content }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="col-lg-3 col-md-4 col-sm-12">
        <div class="card mb-4">
          <div class="card-body" id="user-management" v-if="isLoggedIn">
            <h5>회원 정보</h5>
            <p>회원 정보를 간단하게 보여줍니다.</p>
            <RouterLink :to="{ name: 'Profile' }">
              <button class="btn btn-link">마이페이지</button>
            </RouterLink>
            <button class="btn btn-link" @click="isLoggedIn=!isLoggedIn">로그아웃</button>
          </div>
          <div class="card-body" id="user-login" v-else>
            <h5>로그인</h5>
            <RouterLink :to="{ name: 'Login' }">
              <button class="btn btn-link" @click="isLoggedIn=!isLoggedIn">로그인</button>
            </RouterLink>
            <RouterLink :to="{ name: 'SignUp' }">
              <button class="btn btn-link">회원가입</button>
            </RouterLink>
          </div>
        </div>

        <div class="card mb-4 p-3">
          <h5>사용자 랭킹</h5>
          <div @click="goProfile()" v-for="(user, index) in userRanking" :key="user.username" class="card mb-2 p-2">
            <p>{{ index + 1 }}위: {{ user.username }}</p>
            <p>받은 좋아요 수: {{ user.likes }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
  <RouterLink :to="{ name: 'MovieSelect' }">
    <button class="btn btn-link" >결말 비틀러 가기</button>
  </RouterLink>
</template>

<script setup>
import router from '@/router';
import { pushScopeId, ref } from 'vue';

const movies = ref(['리얼', '성냥팔이 소녀의 재림', '클레멘타인', '웃겨야 사는 영화']);
const isLoggedIn = ref(true); // 실제 로그인 기능을 구현할 경우 대체될 placeholder
const userRanking = ref([
  { username: '윤상흠', likes: 1000000 },
  { username: '민경현', likes: 999999 },
  { username: '신기욱', likes: 999998 }
]);
const altEndRanking = ref([
  {
    movie: '리얼',
    content: '대체 결말 내용 1...'
  },
  {
    movie: '죽어야 사는 영화',
    content: '대체 결말 내용 2...'
  },
  {
    movie: '클레멘타인',
    content: '대체 결말 내용 3...'
  }
]);

const goEndingDetail = function (endingid) {
  router.push({ name: 'EndingListDetail', params: { endingid: endingid } })
}

const goProfile = function (userid) {
  router.push({ name: 'Profile' })
}
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
}

.movie-card {
  padding: 10px;
}

.card-header {
  background-color: #f8f9fa; /* Light background for header */
  font-weight: bold; /* Make header text bold */
}

.ranking-card {
  background-color: #e9ecef; /* Light background for ranking cards */
  padding: 10px;
  border-radius: 5px; /* Rounded corners */
  margin-bottom: 10px; /* Space between ranking cards */
  border: solid black 1px;
}

.card-link {
  text-decoration: none; /* Remove underline from links */
  color: #007bff; /* Bootstrap primary color */
}

.card-link:hover {
  text-decoration: underline; /* Underline on hover */
}
</style>