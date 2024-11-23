<template>
  <div class="comments-container">
    <h3 class="comments-title">댓글</h3>
    <div class="comments-list">
      <div 
        v-for="comment in comments"
        :key="comment.id"
        class="comment-item"
      >
        <p class="comment-author">{{ comment.user_nickname }}</p>
        <p class="comment-content">{{ comment.content }}</p>
      </div>
    </div>
    <form @submit.prevent="createComment" class="comment-form">
      <div class="form-group">
        <label for="content">새 댓글 작성</label>
        <textarea 
          id="content" 
          v-model="content"
          class="form-control"
          rows="3"
        ></textarea>
      </div>
      <button type="submit" class="submit-button">댓글 작성</button>
    </form>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/counter';
import axios from 'axios';
import { onMounted, ref } from 'vue';

const store = useMovieStore()

const content = ref(null)
const comments = ref(null)
const props = defineProps({
  pk: Number,
  nextUrl: String,
})

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/${props.nextUrl}/${props.pk}/comments/`,
  })
    .then((response) => {
      comments.value = response.data
    })
    .catch((error) => {
      store.showModalMessage('댓글 불러오기에 실패했습니다.', error)
    })
})

const createComment = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/${props.nextUrl}/${props.pk}/comments/`,
    data: {
      content: content.value
    },
    headers: {
        Authorization: `Token ${store.token}`,
      },
  })
    .then((response) => {
      axios({
        method: 'get',
        url: `${store.API_URL}/${props.nextUrl}/${props.pk}/comments/`,
      })
        .then((response) => {
          comments.value = response.data
        })
        .catch((error) => {
          window.alert(error)
        })
      })
    .then(() => {
      content.value = null
    })
      .catch((error) => {
        store.showModalMessage('댓글 작성에 실패했습니다.', error)
      })
}
</script>

<style scoped>
.comments-container {
  color: white;
}

.comments-title {
  color: #ffb88c;
  margin-bottom: 20px;
}

.comments-list {
  margin-bottom: 20px;
}

.comment-item {
  background: rgba(255, 255, 255, 0.05);
  padding: 15px;
  border-radius: 8px;
  margin-bottom: 10px;
}

.comment-author {
  color: #ff6b6b;
  font-weight: bold;
  margin-bottom: 5px;
}

.comment-content {
  color: white;
}

.comment-form {
  background: rgba(255, 255, 255, 0.05);
  padding: 20px;
  border-radius: 8px;
}

.form-group {
  margin-bottom: 15px;
}

.form-control {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: white;
}

.submit-button {
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  border: none;
  border-radius: 20px;
  padding: 8px 16px;
  color: white;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.submit-button:hover {
  transform: scale(1.05);
}
</style>