<template>
  <div class="container-fluid bg-dark py-5">
    <div class="container card bg-dark text-white py-5">
      <div class="row justify-content-center">
        <div class="col-lg-8 col-md-10 col-sm-12">
          <h2 class="gradient-text text-center mb-4">커뮤니티 글 수정하기</h2>
          
          <form @submit.prevent="updateArticle" class="article-form card p-4">
            <div class="form-group mb-4">
              <label for="title" class="form-label">제목</label>
              <input 
                type="text" 
                id="title" 
                v-model.trim="title" 
                class="form-control" 
                placeholder="게시글 제목을 입력하세요"
              />
              <span v-if="titleError" class="error">{{ titleError }}</span>
            </div>

            <div class="form-group mb-4">
              <label for="content" class="form-label">내용</label>
              <textarea 
                id="content" 
                v-model.trim="content" 
                class="form-control" 
                placeholder="게시글 내용을 입력하세요"
                rows="10"
              ></textarea>
              <span v-if="contentError" class="error">{{ contentError }}</span>
            </div>

            <div class="d-flex justify-content-between">
              <RouterLink 
                :to="{ name: 'CommunityDetail', params: { articleid: route.params.articleid }}" 
                class="btn btn-warning"
              >
                이전으로
              </RouterLink>
              <button type="submit" class="btn btn-primary" :disabled="isSubmitting">
                {{ isSubmitting ? '수정 중...' : '글 수정하기' }}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/counter';
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const store = useMovieStore();
const title = ref('');
const content = ref('');
const titleError = ref('');
const contentError = ref('');
const isSubmitting = ref(false);
const router = useRouter();
const route = useRoute()

const validateForm = () => {
  titleError.value = title.value ? '' : '제목은 필수입니다.';
  contentError.value = content.value ? '' : '내용은 필수입니다.';
  return !titleError.value && !contentError.value;
};

const updateArticle = async () => {
  if (!validateForm()) return;

  isSubmitting.value = true; // Indicate loading state

  axios ({
    method : 'put',
    url : `${store.API_URL}/communities/${route.params.articleid}/`,
    data : {
      title: title.value,
      content: content.value,
    }, 
    headers: {
        Authorization: `Token ${store.token}`,
      },
    })
    .then((response) => {
    router.replace({
      name: 'CommunityDetail',
      params: {
        articleid: response.data.id
      }
    })
  })
    .catch ((error) => {
      store.errorTitle = '게시글 업데이트에 실패하였습니다.'
      store.errorMessage = Object.values(error.response.data).flat().join('<br>')
      showModal.value = true;
  })
    .finally(() => {
      isSubmitting.value = false
    })
};

onMounted(() => {
  axios.get(`${store.API_URL}/communities/${route.params.articleid}/`)
    .then((res) => {
      title.value = res.data.title;
      content.value = res.data.content
    })
    .catch((err) => {
      store.errorTitle = '불러오려 한 게시글이 없습니다.'
      store.showModal = true;
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

.article-form {
  background: rgba(255, 255, 255, 0.05) !important;
  backdrop-filter: blur(10px);
  border: none;
}

.form-label {
  color: #ffb88c;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.form-control {
  background: rgba(255, 255, 255, 0.1);
  border: 2px solid rgba(255, 255, 255, 0.1);
  color: white;
  transition: all 0.3s ease;
}

.form-control:focus {
  background: rgba(255, 255, 255, 0.15);
  border-color: #ffb88c;
  box-shadow: none;
  color: white;
}

.form-control::placeholder {
  color: rgba(255, 255, 255, 0.5);
}

.error {
  color: #ff6b6b;
  font-size: 0.9rem;
  margin-top: 0.5rem;
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

.btn-warning:hover {
  background: rgba(255, 255, 255, 0.2);
}

.btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

@media (max-width: 768px) {
  .gradient-text {
    font-size: 1.5rem;
  }
}
</style>