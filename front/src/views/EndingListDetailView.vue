<template>
  <div class="container-fluid bg-dark py-5">
    <div class="container card bg-dark text-white py-5" v-if="altending">
      <div class="row gx-5 justify-content-center">
        <div class="col-lg-10 col-md-11 col-sm-12 article-content-wrapper">
          <div class="movie-poster-section card p-4 mb-4">
            <div class="d-flex align-items-start gap-4">
              <div class="poster-wrapper">
                <img 
                  :src="store.BASE_URL + altending.movie_info.poster" 
                  :alt="altending.movie_info.title"
                  class="movie-poster"
                >
              </div>
              <div class="movie-info flex-grow-1">
                <h3 class="movie-title">{{ altending.movie_info.title }}</h3>
                <p class="movie-year">{{ altending.movie_info.openYear }}</p>
                <p class="movie-synopsis mt-3">{{ altending.movie_info.synopsis }}</p>
              </div>
            </div>
          </div>

          <div class="article-header card p-4 mb-4">
            <h2 class="gradient-text mb-4">{{ altending.prompt }}</h2>
            <div class="article-meta d-flex justify-content-between align-items-center">
              <div class="meta-left">
                <div class="meta-item">
                  <i class="bi bi-person-fill"></i>
                  <span><img :src="store.BASE_URL + altending.user_profile_picture" alt="프로필 사진" class="profile-picture"> <span class="mx-1"></span> <strong>{{ altending.user_nickname }}</strong></span>
                </div>
              </div>
              <div class="meta-right">
                <div class="meta-item">
                  <i class="bi bi-clock-fill"></i>
                  <span><em>{{ formatDate(altending.created_at) }}</em></span>
                </div>
              </div>
            </div>
          </div>

          <div class="article-body card p-4 mb-4">
            <p class="article-text">{{ altending.content }}</p>
          </div>

          <div class="d-flex justify-content-between align-items-center mb-4">
            <Like
              :pk="altending.id"
              :isLiked="isLiked"
              nextUrl="movies/altends"
            />
            <div class="action-buttons d-flex gap-2">
              <button 
                v-if="store.isLogin && altending.user_id === store.user.pk"
                @click="deleteAltEnding(altending.id)" 
                class="btn btn-danger"
              >
                삭제
              </button>
              <button @click="$router.go(-1)" class="btn btn-warning">이전으로</button>
              <RouterLink 
                :to="{ name: 'EndingListCreate', params: { movieid: altending.movie_info.id } }" 
                class="btn btn-primary"
              >
                나도 비틀러 가기
              </RouterLink>
            </div>
          </div>

          <Comments 
            :pk="altending.id" 
            nextUrl="movies/altends"
          />
        </div>
      </div>
    </div>
  </div>
  <p class="text-white">{{ altending }}</p>
</template>

<script setup>
import Comments from '@/components/Comments.vue';
import Like from '@/components/Like.vue';
import { useMovieStore } from '@/stores/movieStore';
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

// 날짜 포맷팅 함수 추가
const formatDate = (dateString) => {
  const options = { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' };
  return new Date(dateString).toLocaleDateString('ko-KR', options);
};

// 삭제 함수 추가
const deleteAltEnding = async (endingId) => {
  try {
    await axios({
      method: 'delete',
      url: `${API_URL}/${endingId}/`,
      headers: {
        Authorization: `Token ${store.token}`,
      },
    })
    router.push({ name: 'EndingList' })
  } catch (error) {
    store.showModalMessage('삭제에 실패했습니다.')
  }
}

</script>

<style scoped>
.profile-picture {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  object-fit: cover;
}

.container {
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

.article-content-wrapper {
  max-width: 1000px;
}

.card {
  background: rgba(255, 255, 255, 0.05) !important;
  backdrop-filter: blur(10px);
  border: none;
  transition: transform 0.3s ease;
}

.article-header {
  border-left: 4px solid #ffb88c;
}

.article-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  color: #e0e0e0;
  font-size: 0.95rem;
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.meta-item i {
  color: #ffb88c;
}

.article-body {
  min-height: 200px;
}

.article-text {
  color: #e0e0e0;
  line-height: 1.8;
  font-size: 1.2rem;
  white-space: pre-line;
}

.btn {
  padding: 0.6rem 1.8rem;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  border-radius: 8px;
  font-weight: 600;
  letter-spacing: 0.5px;
  z-index: 1;
}

.btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  transition: all 0.4s ease;
  z-index: -1;
}

.btn:hover::before {
  left: 0;
}

.btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}

.btn-primary {
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  border: none;
  box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3);
}

.btn-primary::before {
  background: linear-gradient(45deg, #ffb88c, #ff6b6b);
}

.btn-warning {
  background: transparent;
  border: 2px solid #ffb88c;
  color: #ffb88c;
}

.btn-warning::before {
  background: rgba(255, 184, 140, 0.15);
}

.btn-danger {
  background: transparent;
  border: 2px solid #dc3545;
  color: #dc3545;
}

.btn-danger::before {
  background: rgba(220, 53, 69, 0.15);
}

.gap-3 {
  gap: 1rem;
}

.movie-poster-section {
  border-left: 4px solid #ff6b6b;
}

.poster-wrapper {
  position: relative;
  cursor: pointer;
  width: 200px;
  height: 300px;
  overflow: hidden;
  border-radius: 8px;
  transition: transform 0.3s ease;
  flex-shrink: 0;
}

.poster-wrapper:hover {
  transform: scale(1.05);
}

.movie-poster {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.poster-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.poster-overlay span {
  color: white;
  font-size: 0.9rem;
  text-align: center;
  padding: 0.5rem;
}

.movie-info {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  min-width: 0;
}

.movie-title {
  font-size: 1.5rem;
  margin: 0;
  color: #ffb88c;
}

.movie-year {
  font-size: 1.1rem;
  color: #e0e0e0;
  margin: 0;
}

.movie-synopsis {
  line-height: 1.6;
  overflow-y: auto;
  max-height: 300px;
  color: #c0c0c0;
  font-size: 1.05rem;
  letter-spacing: 0.3px;
}

@media (max-width: 768px) {
  .article-meta {
    flex-direction: column;
    gap: 0.5rem;
  }

  .gradient-text {
    font-size: 1.5rem;
  }

  .article-text {
    font-size: 1rem;
  }

  .action-buttons {
    flex-direction: column;
    gap: 1rem;
  }

  .action-buttons .d-flex {
    justify-content: center;
  }

  .movie-poster-section > div {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
  
  .poster-wrapper {
    width: 160px;
    height: 240px;
  }

  .movie-synopsis {
    max-height: none;
    font-size: 1rem;
  }
}
</style>