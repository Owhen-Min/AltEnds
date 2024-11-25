<template>
  <div class="container-fluid bg-dark py-5">
    <div v-if="store.user.is_admin" class="container">
      <h3 class="display-4 text-center my-5 gradient-text">메인 페이지 영화 관리</h3>
      
      <div class="d-flex justify-content-end mb-4">
        <button 
          class="btn btn-primary"
          @click="saveSelections"
          :disabled="!hasChanges"
        >
          변경사항 저장
        </button>
      </div>

      <div v-if="movies" class="row g-4">
        <div 
          class="col-lg-3 col-md-4 col-sm-6" 
          v-for="movie in movies" 
          :key="movie.id"
        >
          <div 
            class="card h-100 bg-dark movie-card border-0"
            @click="toggleLocalSelection(movie)"
            @mousedown="startDrag"
            @mouseenter="handleDragOver(movie)"
            :class="{ 'selected': movie.isSelected }"
          >
            <div class="card-img-wrapper position-relative">
              <img 
                :src="store.BASE_URL + movie.poster" 
                :alt="movie.title" 
                class="card-img-top rounded-3"
                draggable="false"
              >
              <div class="selection-overlay" :class="{ 'active': movie.isSelected }">
                <i class="bi bi-check-circle-fill"></i>
              </div>
            </div>
            <div class="card-body text-center">
              <h5 class="card-title text-white mb-2">{{ movie.title }}</h5>
            </div>
          </div>
        </div>
      </div>
      
      <!-- 로딩 상태 표시 -->
      <div v-else class="text-center text-white">
        <div class="spinner-border" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
      </div>
    </div>
    
    <!-- 관리자가 아닌 경우 -->
    <div v-else class="container text-center text-white">
      <h3 class="display-4 my-5">접근 권한이 없습니다</h3>
      <p>이 페이지는 관리자만 접근할 수 있습니다.</p>
      <router-link to="/" class="btn btn-primary">
        메인으로 돌아가기
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/counter';
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';

const store = useMovieStore()
const router = useRouter()
const movies = ref(null)
const isAdmin = ref(false)
const API_URL = store.API_URL + '/movies'

const originalSelections = ref({})
const hasChanges = ref(false)

const isDragging = ref(false)
const lastSelectedMovie = ref(null)

const startDrag = () => {
  isDragging.value = true
  window.addEventListener('mouseup', stopDrag)
}

const stopDrag = () => {
  isDragging.value = false
  lastSelectedMovie.value = null
  window.removeEventListener('mouseup', stopDrag)
}

const handleDragOver = (movie) => {
  if (isDragging.value) {
    if (lastSelectedMovie.value !== movie) {
      toggleLocalSelection(movie)
      lastSelectedMovie.value = movie
    }
  }
}

const toggleLocalSelection = (movie) => {
  movie.isSelected = !movie.isSelected
  checkForChanges()
}

const saveOriginalSelections = () => {
  originalSelections.value = movies.value.reduce((acc, movie) => {
    acc[movie.id] = movie.isSelected
    return acc
  }, {})
}

const checkForChanges = () => {
  hasChanges.value = movies.value.some(movie => 
    originalSelections.value[movie.id] !== movie.isSelected
  )
}

const saveSelections = async () => {
  try {
    // 선택된 영화들의 ID만 추출
    const selectedMovieIds = movies.value
      .filter(movie => movie.isSelected)
      .map(movie => movie.id)

    // 한 번의 요청으로 모든 선택 상태 업데이트
    await axios({
      method: 'put',
      url: `${API_URL}/select/`,
      data: {
        selected_movies: selectedMovieIds
      },
      headers: {
        Authorization: `Token ${store.token}`
      }
    })

    saveOriginalSelections()
    hasChanges.value = false
    store.showModalMessage('영화 선택이 성공적으로 업데이트되었습니다.', null, 'success')
  } catch (error) {
    if (error.response?.data?.['Access Denied']) {
      store.showModalMessage('권한이 없습니다.', '관리자만 접근 가능합니다.')
      router.push('/')
    } else {
      store.showModalMessage('영화 선택 업데이트에 실패했습니다.', error)
    }
  }
}

onMounted(async () => {
  try {
    const response = await axios({
      method: 'get',
      url: `${API_URL}/select/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    movies.value = response.data
    isAdmin.value = true
    saveOriginalSelections()
  } catch (error) {
    if (error.response?.data?.['Access Denied']) {
      isAdmin.value = false
      store.showModalMessage('권한이 없습니다.', '관리자만 접근 가능합니다.')
      router.push('/')
    } else {
      store.showModalMessage('영화들을 가져오는 데 실패했습니다.', error)
    }
  }
})
</script>

<style scoped>
.gradient-text {
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 700;
  letter-spacing: 1px;
}

.movie-card {
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  cursor: pointer;
  user-select: none;
}

.movie-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}

.movie-card.selected {
  border: 3px solid #28a745 !important;
}

.selection-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(40, 167, 69, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.2s ease;
  border-radius: 12px;
}

.selection-overlay.active {
  opacity: 1;
}

.selection-overlay i {
  color: white;
  font-size: 3rem;
}

/* 드래그 중일 때 텍스트 선택 방지 */
.movie-card * {
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

@media (max-width: 768px) {
  .card-img-top {
    height: 300px;
  }
  
  .gradient-text {
    font-size: 2rem;
  }
}
</style>