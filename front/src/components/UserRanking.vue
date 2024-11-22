<template>
  <div class="user-ranking-section">
    <h4 class="card-header">사용자 랭킹</h4>
    <div class="ranking-list">
      <div
        class="ranking-item flex row mx-1 justify-content-between"
        v-for="(user, index) in userRanking"
        :key="user.username"
        @click="goProfile(user.user_id)"
      >
        <h5 class="col-8">{{ index }}위: <strong>{{ user.user_name }}</strong></h5>
        <p class="col-4">👍 {{ user.total_likes }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useMovieStore } from '@/stores/counter';
import { useRouter } from 'vue-router';

const store = useMovieStore();
const router = useRouter();

const userRanking = ref([]);

const goProfile = (userid) => {
  router.push({ name: 'Profile', params: { userid: userid } });
};

onMounted(() => {
  axios({
    method: 'GET',
    url: `${store.API_URL}/movies/ranking/user/`,
  })
    .then((res) => {
      userRanking.value = res.data;
    })
    .catch((error) => {
      console.error('사용자 랭킹을 불러오는 중 오류 발생:', error);
    });
});
</script>

<style scoped>
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

.user-ranking-section {
  background: #ffffff;
  padding: 20px;
  border-radius: 10px;
  margin-bottom: 20px;
}

.card-header {
  background-color: #f8f9fa;
  font-weight: bold;
  text-align: center;
  padding: 15px;
  border-radius: 5px;
  margin-bottom: 20px;
}

.ranking-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.ranking-item {
  display: flex; /* 플렉스 박스로 설정 */
  flex-direction: row; /* 가로 방향 정렬 */
  align-items: center; /* 수직 정렬 */
  justify-content: space-between; /* 양 끝 정렬 */
  white-space: nowrap; /* 텍스트 줄바꿈 방지 */
  background-color: #f1f1f2;
  padding: 10px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.3s;
}

.ranking-item:hover {
  background-color: #e2e2e5;
  transform: scale(1.02);
}

.ranking-item p {
  margin: 0;
  color: #474A59;
  font-weight: 600;
}

@media (max-width: 767px) {
  .user-ranking-section {
    padding: 10px;
  }

  .ranking-item p {
    font-size: 14px;
  }
}
</style>