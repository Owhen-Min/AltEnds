<template>
  <div class="container-fluid bg-dark py-5">
    <div class="container card bg-dark text-white py-5" v-if="altending">
      <div class="row gx-5 justify-content-evenly">
        <!-- Movie Poster Section -->
        <div class="col-lg-3 col-md-6 col-sm-12 text-center card movie-info p-3">
          <img 
            :src="store.BASE_URL + altending.movie_info.poster" 
            alt="Movie Poster" 
            class="movie-poster mb-3"
          >
          <h3 class="gradient-text mb-4">원본 영화</h3>
          <h3 class="text-warning mb-4">{{ altending.movie_info.title }}</h3>
        </div>

        <!-- Alternative Ending Section -->
        <div class="col-lg-7 col-md-6 col-sm-12 card content-card p-4">
          <h2 class="gradient-text mb-4"> {{ altending.prompt }}</h2>
          <div class="ending-box">
            <p class="movie-summary">{{ altending.content }}</p>
          </div>
          <div class="button-container d-flex justify-content-end mt-4 gap-3">
            <button @click="$router.go(-1)" class="btn btn-warning">이전으로</button>
            <RouterLink 
              :to="{ name: 'EndingListCreate', params: { movieid: altending.movie_info.id } }" 
              class="btn btn-primary"
            >
              나도 비틀러 가기
            </RouterLink>
          </div>
        </div>

        <Like
          :pk="altending.id"
          :isLiked="isLiked"
          nextUrl="movies/altends"
          class="mt-4"
        />
        <Comments 
          :pk="altending.id" 
          nextUrl="movies/altends"
          class="mt-4"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import Comments from '@/components/Comments.vue';
import Like from '@/components/Like.vue';
import { useMovieStore } from '@/stores/counter';
import axios from 'axios';
import { onMounted, ref, watch } from 'vue';
import { RouterLink, useRoute, useRouter } from 'vue-router';


const route = useRoute()
const router = useRouter()
const store = useMovieStore()
const altending = ref(null)
const isLiked = ref(false)
const API_URL = store.API_URL + '/movies/altends'

watch(() => altending.value?.like_users, (newValue) => {
  if (newValue) {
    const likeUsers = Array.from(newValue)
    isLiked.value = likeUsers.includes(store.user.pk)
  }
}, { immediate: true })

const fetchAltEnding = async () => {
  try {
    const response = await axios({
      method: 'get',
      url: `${API_URL}/${route.params.endingid}/`,
      headers: {
        Authorization: `Token ${store.token}`,
      },
    })
    altending.value = response.data
  } catch (error) {
    store.showModalMessage('조회한 대체 결말이 없습니다.')
    router.push({ name: 'EndingList' })
  }
}

onMounted(fetchAltEnding)
</script>

<style scoped>
.card {
  background: rgba(255, 255, 255, 0.05) !important;
  backdrop-filter: blur(10px);
  border: none;
}

.gradient-text {
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 700;
  letter-spacing: 1px;
}

.movie-poster {
  max-width: 100%;
  height: auto;
  border-radius: 12px;
  transition: transform 0.3s ease;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

.movie-info {
  background: rgba(255, 255, 255, 0.05) !important;
}

.movie-details h6 {
  color: #ffb88c;
  margin-bottom: 1rem;
}

.content-card {
  background: rgba(255, 255, 255, 0.05) !important;
}

.ending-box {
  background: rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  padding: 1.5rem;
  margin-top: 1rem;
}

.movie-summary {
  line-height: 1.8;
  color: #e0e0e0;
  font-size: 1.2rem;
  white-space: pre-line;
}

.btn {
  padding: 0.5rem 1.5rem;
  transition: transform 0.3s ease;
}

.btn:hover {
  transform: scale(1.05);
}

.btn-primary {
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  border: none;
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
  .movie-summary {
    font-size: 1rem;
  }
  
  .gradient-text {
    font-size: 1.5rem;
  }
}
</style>