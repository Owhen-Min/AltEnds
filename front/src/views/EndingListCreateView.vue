<template>
  <div class="container">
    <h1 class="title">AltEnding</h1>
    <form @submit.prevent="generateEnding" class="article-form" v-if="!isPrompt">
      <div class="form-group">
        <label for="prompt">원하는 변경사항을 입력해주세요. </label>
        <textarea id="prompt" v-model.trim="prompt" required placeholder="프롬프트를 입력하세요"></textarea>
        <span v-if="promptError" class="error">{{ promptError }}</span>
      </div>
      <button type="submit" class="btn btn-primary" :disabled="isSubmitting">
        {{ isSubmitting ? '작성 중...' : '대체결말 생성하기' }}
      </button>
    </form>
    <form @submit.prevent="generateEnding" class="article-form" v-else>
      <div class="row">
        <p>엔딩 목록</p>
        <button @click="selectContent(index)" class="d-flex col-1 justify-content-center" v-for="index in altendings.length" :key="'content-'+index">
          {{ index }}
        </button>
        <p v-if="altendings[selected-1]">프롬프트 : {{ altendings[selected-1].prompt }}</p>
        <p v-if="altendings[selected-1]">대체 결말</p>
        <p v-if="altendings[selected-1]">{{ altendings[selected-1].content }}</p>
      </div>
      <div class="form-group">
        <label for="prompt">마음에 안드는 부분이 있다면 알려주세요. : </label>
        <textarea id="prompt" v-model.trim="prompt" required placeholder="프롬프트를 입력하세요"></textarea>
        <span v-if="promptError" class="error">{{ promptError }}</span>
      </div>
      <button type="submit" class="btn btn-primary" :disabled="isSubmitting">
        {{ isSubmitting ? '작성 중...' : '대체결말 다시 생성하기' }}
      </button>
    </form>
    <button @click="createEnding(altendings[count - 1])" v-if="!isPrompt" class="btn btn-warning">글 작성하기</button>
  </div>

</template>

<script setup>
import { useMovieStore } from '@/stores/counter';
import axios from 'axios';
import { ref, watch, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const store = useMovieStore()
const prompt = ref('')
const promptError = ref('')
const isSubmitting = ref(false)
const router = useRouter()
const route = useRoute()
const altendings = ref([]);
const isPrompt = ref(false)
const selected = ref(null);
const movie = ref(null)

watch(altendings.value, (array) => {
  selected.value = array.length
})

const selectContent = (index) => {
  selected.value = index;
};

const movieid = route.params.movieid

const validateForm = () => {
  promptError.value = prompt.value ? '' : '프롬프트는 필수입니다.'
  return !promptError.value
}

const generateEnding = (() => {
  isSubmitting.value = true
  if (!validateForm()) {
    return
  }
  
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/movies/${movieid}/altends/`,
    data: {
      prompt : prompt.value,
      content : altendings.value[selected-1]
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
  .then((response) => {
    prompt.value = '',
    altendings.value.push({prompt: prompt.value, content: response.data.alt_ending})
    isPrompt.value = true
    isSubmitting.value = false // Reset loading state
  })
  .catch ((error) => {
    console.error('Error creating article:', error);
  })
})

const createEnding = function (altending) {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/movies/altends/`,
    data: {
      movie_id: movieid,
      prompt: altending.prompt,
      content: altending.content,
    },
    headers: {
        Authorization: `Token ${store.token}`,
      },
  })
    .then((response) => {
      router.push({ name: 'EndingList' })
    })
    .catch((error) => {
      console.error('Error creating article:', error)
    })
}

onMounted(() => {
    axios({
        method: 'get',
        url: `${API_URL}/${movieid}/`,
    })
    .then((response) => {
        movie.value = response.data
    })
    .catch((error) => {
        console.log(error)
    })
})

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