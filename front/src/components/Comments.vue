<template>
  <div class="comments-container">
    <h3 class="comments-title">댓글</h3>
    <div class="comments-list">
      <div 
        v-for="comment in paginatedComments"
        :key="comment.id"
        class="d-flex comment-item pages col-12 justify-content-between align-items-center"
      >
        <div class="col-8">
          <p class="comment-author">{{ comment.user_nickname }}</p>
          <p v-if="!comment.isEditing" class="comment-content">{{ comment.content }}</p>
          <textarea 
            v-else 
            v-model="comment.editContent" 
            class="form-control" 
            rows="3"
          ></textarea>
        </div>
        <p class="col-2 comment-date">{{ formatDate(comment.created_at) }}</p>
        <button 
        @click="editComment(comment)" 
        class="btn btn-warning col-1" 
        v-if="comment.user_id === store.user.pk && !comment.isEditing"
        >
        수정
      </button>
      <button 
      @click="updateComment(comment)" 
      class="btn btn-success col-1" 
      v-if="comment.user_id === store.user.pk && comment.isEditing"
      >
      완료
    </button>
    <button 
      @click="deleteComment(comment.id)" 
      class="btn btn-danger col-1" 
      v-if="comment.user_id === store.user.pk"
    >
      삭제
    </button>
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
  <!-- Pagination Footer -->
  <footer class="board-footer d-flex justify-content-between align-items-center mt-4">
    <button 
      class="btn btn-warning" 
      @click="goToPage('prev')"
      :disabled="currentPage === 1"
    >
      이전 페이지로
    </button>
    
    <div class="page-info">
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
</template>

<script setup>
import { useMovieStore } from '@/stores/movieStore';
import axios from 'axios';
import { computed, onMounted, ref, watch } from 'vue';
import { useRouter } from 'vue-router';

const store = useMovieStore()

const currentPage = ref(1);
const itemsPerPage = 10;

const sortOption = ref('recent');
const content = ref(null)
const comments = ref([])
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
      comments.value = response.data.map(comment => ({
        ...comment,
        isEditing: false,
        editContent: comment.content,
      }))
    })
    .catch((error) => {
      store.showModalMessage('댓글 불러오기에 실패했습니다.', error)
    })
})

// 정렬된 게시글
const sortedComments = computed(() => {
  if (!comments.value) return [];
  
  const sorted = [...comments.value];
  switch (sortOption.value) {
    case 'recent':
      return sorted.sort((a, b) => b.id - a.id);
    default:
      return sorted;
  }
});

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
      comments.value.push(response.data)
      content.value = null
      store.getMyProfile()
    })
    .catch((error) => {
      store.showModalMessage('댓글 작성에 실패했습니다.', error)
    })
}

const deleteComment = function (commentId) {
  axios.delete(`${store.API_URL}/${props.nextUrl}/${commentId}/comments/manage/`, {})
    .then(() => {
      store.showModalMessage('댓글이 성공적으로 삭제되었습니다.')
      comments.value = comments.value.filter(comment => comment.id !== commentId)
    })
    .catch((error) => {
      store.showModalMessage('댓글 삭제에 실패했습니다.', error)
    })
}

const editComment = function (comment) {
  comment.isEditing = true
}

const updateComment = function (comment) {
  axios({
    method: 'put',
    url: `${store.API_URL}/${props.nextUrl}/${comment.id}/comments/manage/`,
    data: {
      content: comment.editContent
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then(() => {
      comment.content = comment.editContent
      comment.isEditing = false
    })
    .catch((error) => {
      store.showModalMessage('댓글 수정에 실패했습니다.', error)
    })
}

const formatDate = (dateString) => {
  const date = new Date(dateString);
  const dateOptions = { year: 'numeric', month: 'numeric', day: 'numeric' };
  const formattedDate = date.toLocaleDateString('ko-KR', dateOptions);
  const timeOptions = { hour: '2-digit', minute: '2-digit' };
  const formattedTime = date.toLocaleTimeString('ko-KR', timeOptions);
  return `${formattedDate}\n${formattedTime}`;
};



// 페이지네이션된 게시글
const paginatedComments = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage;
  const end = start + itemsPerPage;
  return sortedComments.value.slice(start, end);
});

// 전체 페이지 수
const totalPages = computed(() => 
  Math.ceil(sortedComments.value.length / itemsPerPage)
);


// 페이지 이동
const goToPage = (direction) => {
  if (direction === 'prev' && currentPage.value > 1) {
    currentPage.value--;
  } else if (direction === 'next' && currentPage.value < totalPages.value) {
    currentPage.value++;
  }
};

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

.comment-date {
  font-size: small;
  white-space: pre-line;
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
