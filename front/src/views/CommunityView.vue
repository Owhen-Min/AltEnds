<template>
  <div class="community-board">
    <!-- Board Header -->
    <header class="board-header d-flex justify-content-between align-items-center mb-4">
      <h2>커뮤니티 게시판</h2>
      <RouterLink :to="{ name: 'CommunityCreate' }" class="btn btn-primary">글 작성하기</RouterLink>
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
    <div v-for="post in posts" :key="post.id" class="post-item" @click="goDetail(post.id)">
      <div class="col-1 text-center">{{ post.id }}</div>
      <div class="col-7 text-left">{{ post.title }}</div>
      <div class="col-2 text-center">{{ post.user_nickname }}</div>
      <div class="col-1 text-center">{{ post.view }}</div>
      <div class="col-1 text-center">{{ post.likes || 0 }}</div>
    </div>

    <!-- Board Footer -->
    <footer class="board-footer d-flex justify-content-between mt-4">
      <RouterLink to="/" class="btn btn-light">이전 페이지로</RouterLink>
      <RouterLink :to="{ name: 'CommunityCreate' }" class="btn btn-primary" >글 작성하기</RouterLink>
      <RouterLink to="/" class="btn btn-light">다음 페이지로</RouterLink>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRouter, RouterLink } from 'vue-router';
import { useMovieStore } from '@/stores/counter';
import axios from 'axios';

const router = useRouter();
const posts = ref([]);
const store = useMovieStore();

// Navigate to post details
const goDetail = (postId) => {
  router.replace({ name: 'CommunityDetail', params: { articleid: postId } });
};

// Fetch posts on component mount
onMounted(() => {
  axios
    .get(`${store.API_URL}/api/v1/communities/articles/`, {
      // headers: {
      //   Authorization: `Token ${store.token}`,
      // },
    })
    .then((res) => {
      posts.value = res.data.sort((a, b) => b.id - a.id);
    })
    .catch((err) => {
      console.error('Error fetching posts:', err);
    });
});

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
