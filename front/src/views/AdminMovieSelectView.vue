<template>
  <div class="container-fluid bg-dark py-5">
    <div v-if="store.user.is_admin" class="container">
      <h3 class="display-4 text-center my-5 gradient-text">메인 페이지 영화 관리</h3>
      
      <div class="d-flex justify-content-end mb-4">
        <div class="d-flex gap-2 align-items-center">
          <div class="search-container">
            <input 
              type="text" 
              v-model="searchQuery" 
              class="form-control search-input bg-dark text-white" 
              placeholder="영화 검색..."
            >
          </div>
          <select 
            v-model="sortOption" 
            class="form-select sort-select small-select"
            aria-label="정렬 옵션"
          >
            <option value="recent">최신순</option>
            <option value="title">제목순</option>
          </select>
          <RouterLink 
            :to="{ name: 'AdminMovieCreate' }" 
            class="btn btn-success custom-btn"
          >
            새 영화 등록
          </RouterLink>
          <button 
            class="btn btn-primary custom-btn"
            @click="saveSelections"
            :disabled="!hasChanges"
          >
            변경사항 저장
          </button>
        </div>
      </div>

      <div v-if="movies" class="row g-4">
        <div 
          class="col-lg-2 col-md-3 col-sm-4" 
          v-for="movie in sortedMovies" 
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
import { onMounted, ref, watch, computed } from 'vue';
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

const sortOption = ref('recent')
const searchQuery = ref('')

// 정렬된 영화 목록
const sortedMovies = computed(() => {
  if (!movies.value) return [];
  
  let filtered = [...movies.value];
  
  // 검색어로 필터링
  if (searchQuery.value.trim()) {
    const query = searchQuery.value.toLowerCase();
    filtered = filtered.filter(movie => 
      movie.title.toLowerCase().includes(query)
    );
  }
  
  // 정렬
  switch (sortOption.value) {
    case 'title':
      return filtered.sort((a, b) => a.title.localeCompare(b.title));
    case 'recent':
    default:
      return filtered.sort((a, b) => b.id - a.id);
  }
});

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

.sort-select {
  color: white;
  padding: 0rem 2rem 0rem 1rem;
  background: rgba(255, 255, 255, 0.1);
  border: 2px solid #ffb88c;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  min-width: 120px;
  font-size: 0.9rem;
  height: 35px;
  
  /* 커스텀 화살표 스타일링 */
  appearance: none;
  background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
  background-repeat: no-repeat;
  background-position: right 0.5rem center;
  background-size: 0.8em;
}

.sort-select:hover {
  background: rgba(255, 255, 255, 0.2);
}

.sort-select:focus {
  outline: none;
  box-shadow: 0 0 0 2px rgba(255, 184, 140, 0.5);
}

.sort-select option {
  background: #343a40;
  color: white;
}

.small-select {
  width: 100px;
  height: 35px;
  font-size: 0.9rem;
  padding: 0.2rem 1.5rem 0.2rem 0.5rem;
}

.custom-btn {
  min-width: 140px;
  height: 45px;
  padding: 0.5rem 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>