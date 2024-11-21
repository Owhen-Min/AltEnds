<template>
  <div class="community-board">
    <!-- Board Header -->
    <header class="board-header d-flex justify-content-between align-items-center mb-4">
      <h2>AI 게시판</h2>
      <RouterLink :to="{ name: 'MovieSelect' }" class="btn btn-primary">결말 비틀러 가기</RouterLink>
    </header>

    <!-- Table Header -->
    <div class="d-flex table-header">
      <div class="col-1 text-center font-weight-bold">번호</div>
      <div class="col-7 text-center font-weight-bold">제목</div>
      <div class="col-2 text-center font-weight-bold">작성자</div>
      <div class="col-1 text-center font-weight-bold">조회수</div>
      <div class="col-1 text-center font-weight-bold">좋아요</div>
    </div>

    <!-- Posts List -->
    <div v-for="ending in endings" :key="ending.id" class="post-item" @click="goDetail(ending.id)">
      <div class="col-1 text-center">{{ ending.id }}</div>
      <div class="col-7 text-left">{{ ending.prompt }}</div>
      <div class="col-2 text-center">{{ ending.user_nickname }}</div>
      <div class="col-1 text-center">{{ ending.view }}</div>
      <div class="col-1 text-center">{{ ending.like_users.length }}</div>
    </div>

    <!-- Board Footer -->
    <footer class="board-footer d-flex justify-content-between mt-4">
      <RouterLink to="/" class="btn btn-light">이전 페이지로</RouterLink>
      <RouterLink :to="{ name: 'MovieSelect' }" class="btn btn-primary">결말 비틀러 가기</RouterLink>
      <RouterLink to="/" class="btn btn-light">다음 페이지로</RouterLink>
    </footer>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/counter';
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { RouterLink, useRouter } from 'vue-router';

const router = useRouter()
const store = useMovieStore()
const API_URL = store.API_URL + '/movies/altends/'
const endings = ref([])

const goDetail = ((endingid) => {
  router.push({ name: 'EndingListDetail', params: { endingid: endingid }})
})

onMounted(() => {
  axios
    .get(API_URL, {
    })
    .then((response) => {
      endings.value = response.data
    })
    .catch((error) => {
      console.error('Error fetching posts:', error)
    })
})

</script>

<style scoped>
.community-board {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f8f9fa;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.board-header {
  margin-bottom: 20px;
}

.table-header {
  background-color: #e9ecef;
  padding: 10px 5px;
  font-size: 15px;
}

.post-item {
  display: flex;
  align-items: center;
  padding: 10px;
  cursor: pointer;
  border-bottom: 1px solid #dee2e6;
  transition: background-color 0.2s;
}

.post-item:hover {
  background-color: #e2e6ea;
}

.board-footer {
  margin-top: 20px;
}

.font-weight-bold {
  font-weight: bold;
}
</style>