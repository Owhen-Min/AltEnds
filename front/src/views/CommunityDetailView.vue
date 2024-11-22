<template>
  <div class="article-container" v-if="article">
    <div class="article-card">
      <h2 class="article-title">{{ article.title }}</h2>
      <div class="article-meta">
        <p>작성자: <strong>{{ article.user_nickname }}</strong></p>
        <p>작성 시간: <em>{{ formatDate(article.created_at) }}</em></p>
        <p v-if="article.created_at!=article.updated_at">수정 시간: <em>{{ formatDate(article.updated_at) }}</em></p>
      </div>
      <p class="article-content">{{ article.content }}</p>
      <div class="row button-group">
        <RouterLink :to="{name:'Community'}" class="col-3 btn btn-warning">이전으로</RouterLink>
        <div class="col-3"></div>
        <button @click="updateArticle(article.id)" class="col-3 btn btn-lg btn-primary" v-if="store.isLogin&&article.user===store.user.pk">수정하기</button>
        <button @click="confirmDelete(article.id)" class="col-3 btn btn-lg btn-danger" v-if="store.isLogin&&article.user===store.user.pk">삭제</button>
      </div>
      <Like
        :pk="article.id"
        nextUrl="communities"
      />
      <Comments
        :pk="article.id"
        nextUrl="communities"
      />
    </div>
  </div>
</template>

<script setup>
import Comments from '@/components/Comments.vue';
import Like from '@/components/Like.vue';
import { useMovieStore } from '@/stores/counter';
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();
const store = useMovieStore();
const article = ref(null);


const formatDate = (dateString) => {
  const options = { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' };
  return new Date(dateString).toLocaleDateString('ko-KR', options);
};

const confirmDelete = (articleId) => {
  if (confirm('정말 이 게시글을 삭제하시겠습니까?')) {
    deleteArticle(articleId);
  }
};

const updateArticle = (articleId) => {
  router.push({name: 'CommunityUpdate', params:{articleid : articleId}})
};

const deleteArticle = (articleId) => {
  axios.delete(`${store.API_URL}/communities/${articleId}/`, {
  })
  .then(() => {
    router.push({ name: 'Community' });
  })
  .catch((error) => {
    window.alert('삭제에 실패하였습니다.')
  });
};



onMounted(() => {
  axios.get(`${store.API_URL}/communities/${route.params.articleid}/`)
    .then((res) => {
      article.value = res.data;
    })
    .catch((err) => {
      store.errorTitle = '조회한 게시글이 없습니다.'
      store.showModal = true;
      router.push({ name: 'Community' });
    });
});
</script>

<style scoped>
.article-container {
  display: flex;
  justify-content: center;
  padding: 20px;
}

.article-card {
  max-width: 600px;
  width: 100%;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.article-title {
  margin-bottom: 10px;
  color: #333;
}

.article-meta {
  font-size: 14px;
  color: #555;
  margin-bottom: 15px;
}

.article-content {
  margin-bottom: 20px;
  line-height: 1.5;
}

.button-group {
  display: flex;
}

.btn {
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn-warning {
  background-color: #ffc107;
  color: white;
}

.btn-danger {
  background-color: #dc3545;
  color: white;
}

.btn:hover {
  opacity: 0.9;
}

p {
  margin-bottom: 5px;
}

</style>