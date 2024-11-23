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
      store.showModalMessage('사용자 랭킹을 불러오는 데 실패했습니다.', error)
    });
});
</script>

<style scoped>
.user-ranking-section {
  background: rgba(255, 255, 255, 0.05);
  padding: 1.5rem;
  border-radius: 12px;
  color: white;
}

.card-header {
  background: none;
  color: white;
  font-weight: 700;
  text-align: center;
  padding: 0;
  margin-bottom: 1.5rem;
}

.ranking-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.ranking-item {
  background: rgba(255, 255, 255, 0.08);
  padding: 0.8rem 1rem;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  color: white;
}

.ranking-item:hover {
  background: rgba(255, 255, 255, 0.12);
  transform: translateX(5px);
}

.ranking-item h5 {
  margin: 0;
  font-size: 0.95rem;
}

.ranking-item p {
  margin: 0;
  font-size: 0.9rem;
  color: #ffb88c;
}
</style>