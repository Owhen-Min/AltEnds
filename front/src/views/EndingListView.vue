<template>
  <div class="container-fluid bg-dark py-5">
    <div class="container card bg-dark text-white py-5">
      <!-- Board Header -->
      <header class="board-header d-flex justify-content-between align-items-center mb-4">
        <h2 class="gradient-text">AI 게시판</h2>
        <div class="d-flex align-items-center gap-3">
          <select 
            v-model="sortOption" 
            class="form-select sort-select"
            aria-label="정렬 옵션"
          >
            <option value="recent">최신순</option>
            <option value="views">조회수순</option>
            <option value="likes">좋아요순</option>
          </select>
          <EndingTwistButton class="twist-button" />
        </div>
      </header>

      <!-- Table Header -->
      <div class="d-flex table-header rounded">
        <div class="col-1 text-center font-weight-bold">번호</div>
        <div class="col-7 text-center font-weight-bold">제목 </div>
        <div class="col-2 text-center font-weight-bold">작성자</div>
        <div class="col-1 text-center font-weight-bold">조회수</div>
        <div class="col-1 text-center font-weight-bold">좋아요</div>
      </div>

      <!-- Posts List -->
      <div v-for="ending in paginatedEndings" :key="ending.id" class="post-item" @click="goDetail(ending.id)">
        <div class="col-1 text-center">{{ ending.id }}</div>
        <div class="col-7 text-left ending-prompt"> {{ ending.prompt }} <span class="comment-count">[{{ ending.comment_set.length }}]</span></div>
        <div class="col-2 text-center">{{ ending.user_nickname }}</div>
        <div class="col-1 text-center">{{ ending.view }}</div>
        <div class="col-1 text-center">{{ ending.like_users.length }}</div>
      </div>

      <!-- Pagination Footer -->
      <footer class="board-footer d-flex justify-content-between align-items-center mt-4">
        <button 
          class="btn btn-warning" 
          @click="goToPage('prev')"
          :disabled="currentPage === 1"
        >
          이전 페이지로
        </button>
        
        <div class="page-info text-white">
          {{ currentPage }} / {{ totalPages }}
        </div>
        
        <button 
          class="btn btn-warning" 
          @click="goToPage('next')"
          :disabled="currentPage === totalPages"
        >
          다음 페이지로
        </button>
      </footer>
    </div>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movieStore';
import axios from 'axios';
import { onMounted, ref, computed, watch } from 'vue';
import { useRouter } from 'vue-router';
import EndingTwistButton from '@/components/EndingTwistButton.vue';

const router = useRouter()
const store = useMovieStore()
const API_URL = store.API_URL + '/movies/altends/'
const endings = ref([])
const currentPage = ref(1)
const itemsPerPage = 20
const totalPages = ref(0)
const sortOption = ref('recent') // 기본값은 최신순

const sortedEndings = computed(() => {
  if (!endings.value) return []
  
  const sorted = [...endings.value]
  switch (sortOption.value) {
    case 'views':
      return sorted.sort((a, b) => b.view - a.view)
    case 'likes':
      return sorted.sort((a, b) => b.like_users.length - a.like_users.length)
    case 'recent':
      return sorted.sort((a, b) => b.id - a.id)
    default:
      return sorted
  }
})

// paginatedEndings computed 속성 수정
const paginatedEndings = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  const end = start + itemsPerPage
  return sortedEndings.value.slice(start, end)
})

// 정렬 옵션 변경시 첫 페이지로 이동
watch(sortOption, () => {
  currentPage.value = 1
})

// 페이지 이동 함수
const goToPage = (direction) => {
  if (direction === 'prev' && currentPage.value > 1) {
    currentPage.value--
  } else if (direction === 'next' && currentPage.value < totalPages.value) {
    currentPage.value++
  }
}

const goDetail = ((endingid) => {
  router.push({ name: 'EndingListDetail', params: { endingid: endingid }})
})

onMounted(() => {
  axios
    .get(API_URL, {
    })
    .then((response) => {
      endings.value = response.data.sort((a, b) => b.id - a.id);
      totalPages.value = Math.ceil(endings.value.length / itemsPerPage);
    })
    .catch((error) => {
      store.showModalMessage('대체 결말들을 가져오는 데 실패했습니다.', error)
    })
})

</script>

<style scoped>
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

.table-header {
  background: rgba(255, 255, 255, 0.08);
  padding: 15px 10px;
  font-size: 15px;
}

.post-item {
  display: flex;
  align-items: center;
  padding: 15px 10px;
  cursor: pointer;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  transition: background-color 0.3s ease;
}

.post-item:hover {
  background: rgba(255, 255, 255, 0.1);
}

.btn-primary {
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  border: none;
  transition: transform 0.3s ease;
}

.btn-primary:hover {
  transform: scale(1.05);
}

.btn-warning {
  background: rgba(255, 255, 255, 0.1);
  border: 2px solid #ffb88c;
  color: white;
  transition: transform 0.3s ease;
}

.btn-warning:hover {
  transform: scale(1.05);
  background: rgba(255, 255, 255, 0.2);
}

.ending-prompt {
  font-size: 1rem;
  color: #e0e0e0;
  max-height: 3em;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.comment-count {
  color: #ffb88c;
  font-size: 0.9rem;
  margin-left: 5px;
}

.page-info {
  font-size: 1.1rem;
  padding: 0.5rem 1rem;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 8px;
}

.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none !important;
}

.board-footer {
  padding: 1rem 0;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  margin-top: 2rem;
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

.gap-3 {
  gap: 1rem;
}

.twist-button {
  margin-left: auto;
  min-width: 150px;
  padding: 1rem 0rem;  /* 좌우 패딩 추가 */
}
</style>