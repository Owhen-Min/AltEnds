vue
<template>
  <div class="article-container" v-if="article">
    <div class="article-card">
      <h2 class="article-title">{{ article.title }}</h2>
      <div class="article-meta">
        <p>작성자: <strong>{{ article.user_nickname }}</strong></p>
        <p>작성 시간: <em>{{ formatDate(article.created_at) }}</em></p>
      </div>
      <p class="article-content">{{ article.content }}</p>
      <div class="row button-group">
        <button @click="goBack" class="col-3 btn btn-warning">이전으로</button>
        <div class="col-3"></div>
        <button @click="confirmDelete(article.id)" class="col-3 btn btn-lg btn-danger" v-if="article.user===store.user.pk">삭제</button>
        <button @click="confirmDelete(article.id)" class="col-3 btn btn-lg btn-primary" v-if="article.user===store.user.pk">수정하기</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/counter';
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();
const article = ref(null);
const store = useMovieStore();

const formatDate = (dateString) => {
  const options = { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' };
  return new Date(dateString).toLocaleDateString('ko-KR', options);
};

const goBack = () => {
  router.go(-1);
};

const confirmDelete = (articleId) => {
  if (confirm('정말 이 게시글을 삭제하시겠습니까?')) {
    deleteArticle(articleId);
  }
};

const deleteArticle = (articleId) => {
  axios.delete(`${store.API_URL}/api/v1/communities/articles/${articleId}/`, {
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
  .then(() => {
    router.push({ name: 'Community' });
  })
  .catch((error) => {
    console.error("Error deleting article:", error);
  });
};

onMounted(() => {
  axios.get(`${store.API_URL}/api/v1/communities/articles/${route.params.articleid}/`)
    .then((res) => {
      article.value = res.data;
    })
    .catch((err) => {
      console.error("Error fetching article:", err);
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
</style>