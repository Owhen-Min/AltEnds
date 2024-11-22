<template>
  <div class="ending-ranking-section">
    <h4 class="card-header">결말 랭킹</h4>
    <div class="row justify-content-around">
      <div
        class="ranking-card col-5 col-lg-3 d-flex"
        v-for="(ending, index) in topEndingRanking"
        :key="ending.ending_id"
        @click="goEndingDetail(ending.ending_id)"
      >
        <div class="card-content d-flex flex-column">
          <h5 class="rank d-flex justify-content-between align-items-center">
            <span>{{ index }}위</span>
            <span class="like-count">👍{{ ending.like_count }}</span>
          </h5>
          <p class="movie"><strong>{{ ending.movie }}</strong></p>
          <p class="likes"></p>
          <p class="prompt">{{ ending.prompt }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import { useMovieStore } from '@/stores/counter';
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
      console.error('결말 랭킹을 불러오는 중 오류 발생:', error);
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

.ending-ranking-section {
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

.ranking-card {
  background-color: #f1f1f2;
  padding: 15px;
  border: 1px solid #e2e2e5;
  border-radius: 10px;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.3s;
  height: 200px;
  display: flex;
  margin: 10px;
}

.ranking-card:hover {
  background-color: #e2e2e5;
  transform: scale(1.02);
}

.card-content {
  display: flex;
  flex-direction: column;
  gap: 3px;
  flex-grow: 1;
}

.rank {
  margin: 0;
  color: #474A59;
  font-weight: 600;
}

.movie {
  margin: 0;
  color: #474A59;
  font-size: 1.1em;
}

.likes {
  margin: 0;
  color: #474A59;
  font-weight: 600;
}

.prompt {
  margin: 0;
  color: #474A59;
  font-size: 0.95em;
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 3; /* 원하는 줄 수 */
  -webkit-box-orient: vertical;
}

@media (max-width: 767px) {
  .ending-ranking-section {
    padding: 10px;
  }

  .ranking-card {
    padding: 10px;
  }

  .movie {
    font-size: 1em;
  }

  .prompt {
    font-size: 0.85em;
  }
}
</style>