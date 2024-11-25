<template>
  <div class="ending-ranking-section" :class="$attrs.class">
    <h4 class="card-header">결말 랭킹</h4>
    <div class="row justify-content-around">
      <div
        class="ranking-card col-5 col-lg-3"
        v-for="(ending, index) in topEndingRanking"
        :key="ending.ending_id"
        @click="goEndingDetail(ending.ending_id)"
      >
        <div class="card-content">
          <div class="rank-header">
            <span class="rank">{{ index }}위</span>
            <span class="like-count">👍 {{ ending.like_count }}</span>
          </div>
          <div class="movie-info">
            <p class="movie"><strong>{{ ending.movie }}</strong></p>
            <p class="prompt">{{ truncatePrompt(ending.prompt, 50) }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import { useMovieStore } from '@/stores/movieStore';
import { useRouter } from 'vue-router';

const store = useMovieStore();
const router = useRouter();

const endingRanking = ref([]);

const topEndingRanking = computed(() => endingRanking.value);

const goEndingDetail = (endingId) => {
  router.push({ name: 'EndingListDetail', params: { endingid: endingId } });
};

const truncatePrompt = (text, maxLength = 100) => {
  if (text.length > maxLength) {
    return text.substring(0, maxLength) + '...';
  }
  return text;
};

onMounted(() => {
  axios({
    method: 'GET',
    url: `${store.API_URL}/movies/ranking/ending/`,
  })
    .then((res) => {
      endingRanking.value = res.data;
    })
    .catch((error) => {
      store.showModalMessage('결말 랭킹을 불러오는 데 실패했습니다.', error)
    });
});
</script>

<style scoped>
.ending-ranking-section {
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

.rank-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.8rem;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.rank {
  color: #ffb88c;
  font-size: 1rem;
  font-weight: 600;
}

.like-count {
  color: #ff6b6b;
  font-size: 0.9rem;
}

.movie-info {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.movie {
  color: white;
  font-size: 1rem;
  margin: 0;
}

.prompt {
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.9rem;
  margin: 0;
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.ranking-card {
  background: rgba(255, 255, 255, 0.08);
  padding: 1rem;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.3s ease;
  margin: 0.5rem;
  min-height: 160px;
}

.ranking-card:hover {
  background: rgba(255, 255, 255, 0.12);
  transform: translateY(-5px);
}
</style>