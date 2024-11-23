<template>
  <div class="container-fluid bg-dark py-5">
    <div class="container card bg-dark text-white py-5" v-if="article">
      <!-- Article Content -->
      <div class="row gx-5 justify-content-center">
        <div class="col-lg-10 col-md-11 col-sm-12 article-content-wrapper">
          <!-- Article Header -->
          <div class="article-header card p-4 mb-4">
            <h2 class="gradient-text mb-4">{{ article.title }}</h2>
            <div class="article-meta d-flex justify-content-between align-items-center">
              <div class="meta-left">
                <div class="meta-item">
                  <i class="bi bi-person-fill"></i>
                  <span>작성자: <strong>{{ article.user_nickname }}</strong></span>
                </div>
              </div>
              <div class="meta-right">
                <div class="meta-item">
                  <i class="bi bi-clock-fill"></i>
                  <span><em>{{ formatDate(article.created_at) }}</em></span>
                </div>
              </div>
            </div>
          </div>

          <!-- Article Body -->
          <div class="article-body card p-4 mb-4">
            <p class="article-text">{{ article.content }}</p>
          </div>

          <!-- Action Buttons -->
          <div class="action-buttons d-flex justify-content-between mb-4">
            <RouterLink :to="{name:'Community'}" class="btn btn-warning">
              이전으로
            </RouterLink>
            <div class="d-flex gap-3" v-if="store.isLogin && article.user === store.user.pk">
              <button @click="updateArticle(article.id)" class="btn btn-primary">
                수정하기
              </button>
              <button @click="deleteArticle(article.id)" class="btn btn-danger">
                삭제
              </button>
            </div>
          </div>

          <!-- Like Component -->
          <Like
            :pk="article.id"
            nextUrl="communities"
            class="mb-4"
          />

          <!-- Comments Component -->
          <Comments
            :pk="article.id"
            nextUrl="communities"
          />
        </div>
      </div>
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
    store.showModalMessage('삭제에 실패했습니다.', error)
  });
};



onMounted(() => {
  axios.get(`${store.API_URL}/communities/${route.params.articleid}/`)
    .then((res) => {
      article.value = res.data;
    })
    .catch((err) => {
      store.showModalMessage('조회한 게시글이 없습니다.')
      router.push({ name: 'Community' });
    });
});
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
  font-size: 1.1rem;
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

.btn-danger {
  background: rgba(255, 255, 255, 0.1);
  border: 2px solid #dc3545;
  color: #dc3545;
}

.btn-warning:hover {
  background: rgba(255, 255, 255, 0.2);
}

.btn-danger:hover {
  background: rgba(220, 53, 69, 0.1);
}

.gap-3 {
  gap: 1rem;
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
}
</style>