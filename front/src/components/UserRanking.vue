<template>
  <div class="user-ranking-section">
    <h4 class="card-header">사용자 랭킹</h4>
    <div class="ranking-list">
      <div
        class="ranking-item d-flex align-items-center"
        v-for="(user, index) in userRanking"
        :key="user.username"
        @click="goProfile(user.user_id)"
      >
        <div class="profile-image-container me-3">
          <img :src="store.BASE_URL + user.profile_picture" alt="profile" class="profile-picture">
        </div>
        <h5 class="ranking-name mb-0">{{ index }}위<br><strong>{{ user.user_name }}</strong></h5>
        <p class="likes-count ms-auto mb-0">💗 {{ user.total_likes }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import axios from 'axios';
import { useMovieStore } from '@/stores/movieStore';
import { useRouter } from 'vue-router';

const store = useMovieStore();
const router = useRouter();

const userRanking = ref([]);

const goProfile = (userid) => {
  router.push({ name: 'Profile', params: { userid: userid } });
};

const fetchRanking = () => {
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
};

onMounted(() => {
  fetchRanking();
  const interval = setInterval(fetchRanking, 60000);
  
  onUnmounted(() => {
    clearInterval(interval);
  });
});
</script>

<style scoped>
.profile-picture {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  object-fit: cover;
}

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
  width: 100%;
}

.ranking-item:hover {
  background: rgba(255, 255, 255, 0.12);
  transform: translateX(5px);
}

.ranking-name {
  font-size: 0.95rem;
  flex: 1;
}

.likes-count {
  font-size: 0.9rem;
  color: #ffb88c;
  min-width: 60px;
  text-align: right;
}
</style>