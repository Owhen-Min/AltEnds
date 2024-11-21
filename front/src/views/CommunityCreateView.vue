<template>
  <div class="container">
    <h1 class="title">커뮤니티 글 작성하기</h1>
    <form @submit.prevent="createArticle" class="article-form">
      <div class="form-group">
        <label for="title">제목:</label>
        <input type="text" id="title" v-model.trim="title" required placeholder="게시글 제목을 입력하세요" />
        <span v-if="titleError" class="error">{{ titleError }}</span>
      </div>
      <div class="form-group">
        <label for="content">내용:</label>
        <textarea id="content" v-model.trim="content" required placeholder="게시글 내용을 입력하세요"></textarea>
        <span v-if="contentError" class="error">{{ contentError }}</span>
      </div>
      <button type="submit" class="btn btn-primary" :disabled="isSubmitting">
        {{ isSubmitting ? '작성 중...' : '글 작성하기' }}
      </button>
    </form>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/counter';
import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const store = useMovieStore();
const title = ref('');
const content = ref('');
const titleError = ref('');
const contentError = ref('');
const isSubmitting = ref(false);
const router = useRouter();

const validateForm = () => {
  titleError.value = title.value ? '' : '제목은 필수입니다.';
  contentError.value = content.value ? '' : '내용은 필수입니다.';
  return !titleError.value && !contentError.value;
};

const createArticle = async () => {
  if (!validateForm()) return;

  isSubmitting.value = true; // Indicate loading state

  try {
    const response = await axios.post(`${store.API_URL}/communities/`, {
      title: title.value,
      content: content.value,
    }, {
      headers: {
        Authorization: `Token ${store.token}`,
      },
    })
    router.push({ name: 'CommunityDetail', params: { articleid: response.data.id } });
  } catch (error) {
    console.error('Error creating article:', error);
  } finally {
    isSubmitting.value = false; // Reset loading state
  }
};
</script>

<style lang="scss" scoped>
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.title {
  text-align: center;
  margin-bottom: 20px;
  color: #333;
}

.article-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

label {
  margin-bottom: 5px;
  font-weight: bold;
}

input[type="text"],
textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
}

textarea {
  resize: vertical;
  min-height: 100px;
}

.error {
  color: red;
  font-size: 14px;
}

.btn {
  padding: 10px;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  background-color: #007bff;
  color: white;
  transition: background-color 0.3s;

  &:hover {
    background-color: #0056b3;
  }

  &:disabled {
    background-color: #007bff;
    opacity: 0.6;
    cursor: not-allowed;
  }
}
</style>