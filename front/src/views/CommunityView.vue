vue
<template>
  <div class="community-board">
    <header class="board-header d-flex justify-content-between align-items-center mb-4">
      <h2>커뮤니티 게시판</h2>
      <RouterLink to="{ name: 'CommunityCreate' }" class="btn btn-primary">글 작성하기</RouterLink>
    </header>
    </div>

    <div class="posts-container">
      <div>
        <div class="table-header container flex p-3">
          <div class="row justify-content-center align-items-center">
          <div class="header-item col-1">Index</div>
          <div class="header-item col-5">제목</div>
          <div class="header-item col-2">작성자</div>
          <div class="header-item col-2">조회수</div>
          <div class="header-item col-2">좋아요 수</div>
        </div>
      </div>
      <div 
        class="post-item container" 
        v-for="post in posts" 
        :key="post.id" 
        @click="goDetail(post.id)"
      >
        <div class="post-details col-1">{{ post.id }}</div>
        <div class="post-details col-5">{{ post.title }}</div>
        <div class="post-details col-2">{{ post.user_nickname }}</div>
        <div class="post-details col-2">200</div>
        <div class="post-details col-2">500</div>
      </div>
    </div>

    <footer class="board-footer d-flex justify-content-between mt-4">
      <RouterLink to="/" class="btn btn-light">이전 페이지로</RouterLink>
      <RouterLink to="/community/create" class="btn btn-primary">글 작성하기</RouterLink>
      <RouterLink to="/" class="btn btn-light">다음 페이지로</RouterLink>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter, RouterLink } from 'vue-router';
import { useMovieStore } from '@/stores/counter';
import axios from 'axios';

const router = useRouter();
const posts = ref([]);
const store = useMovieStore();

const goDetail = (postId) => {
  router.push({ name: 'CommunityDetail', params: { articleid: postId } });
};

onMounted(() => {
  axios.get(`${store.API_URL}/api/v1/communities/articles/`, {
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
  .then((res) => {
    posts.value = res.data;
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

.table-header,
.posts-container {
  display: flex;
  flex-direction: column;
}

.header-item {
  display: flex;
  justify-content: center;
  font-weight: bold;
  padding: 25 px;
  background-color: #e9ecef;
}

.post-item {
  display: flex;
  padding: 5px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.post-item:hover {
  background-color: #e2e6ea;
}

.post-details {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 10px;
  border-bottom: 1px solid #dee2e6;
}

.board-footer {
  margin-top: 20px;
}
</style>