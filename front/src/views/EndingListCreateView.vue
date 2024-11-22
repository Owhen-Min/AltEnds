<template>
  <div class="container">
    <h1 class="title">AltEnding</h1>

    <!-- Movie Information -->
    <div class="movie-info row" v-if="movie">
      <div class="poster col-3 align-items-center justify-content-center">
        <span>원본 영화 정보</span>
        <img :src="store.BASE_URL + movie.poster" :alt="movie.title" />
        <p class="center">{{ movie.title }}</p>
      </div>
      <div class="details col-8">
        <h6>시놉시스</h6>
        <p>{{ movie.plot }}</p>
      </div>
    </div>

    <!-- Prompt Form -->
    <form @submit.prevent="generateEnding" v-if="!isPrompt" class="form">
      <div class="form-group">
        <label for="prompt">원하는 변경사항을 입력해주세요:</label>
        <textarea
          id="prompt"
          v-model.trim="prompt"
          placeholder="프롬프트를 입력하세요"
          required
        ></textarea>
        <span v-if="promptError" class="error">{{ promptError }}</span>
      </div>
      <button type="submit" class="btn btn-primary" :disabled="isSubmitting">
        {{ isSubmitting ? '작성 중...' : '대체결말 생성하기' }}
      </button>
    </form>

    <!-- Alternative Endings -->
    <div v-if="isPrompt" class="alt-endings">
      <h2>엔딩 목록</h2>
      <div class="ending-buttons">
        <button
          v-for="index in altendings.length"
          :key="'content-' + index"
          @click="selectContent(index)"
          :class="['btn', selected === index ? 'btn-active' : 'btn-secondary']"
        >
          엔딩 {{ index }}
        </button>
      </div>

      <div v-if="altendings[selected - 1]" class="ending-content">
        <h5>프롬프트</h5>
        <p>{{ altendings[selected - 1].prompt }}</p>
        <h5>대체 결말</h5>
        <p>{{ altendings[selected - 1].content }}</p>
      </div>

      <!-- Re-Prompt Form -->
      <form @submit.prevent="generateEnding" class="form">
        <div class="form-group">
          <label for="re-prompt">마음에 안드는 부분이 있다면 알려주세요:</label>
          <textarea
            id="re-prompt"
            v-model.trim="prompt"
            placeholder="프롬프트를 입력하세요"
            required
          ></textarea>
          <span v-if="promptError" class="error">{{ promptError }}</span>
        </div>
        <button type="submit" class="btn btn-primary" :disabled="isSubmitting">
          {{ isSubmitting ? '작성 중...' : '대체결말 다시 생성하기' }}
        </button>
      </form>

      <button @click="openModal" class="btn btn-warning">글 작성하기</button>

      <SelectModal
        :isOpen="isModalOpen"
        title="글 작성 확인"
        message="작성할 프롬프트를 선택하세요"
        :options="altendings"
        @confirm="handleModalConfirm"
        @cancel="handleModalCancel"
      />


      <!-- <button @click="createEnding" class="btn btn-warning">글 작성하기</button> -->
    </div>
  </div>
</template>

<script setup>
import SelectModal from '@/components/SelectModal.vue';
import { useMovieStore } from '@/stores/counter';
import axios from 'axios';
import { ref, onMounted, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';


const isModalOpen = ref(false);
const selectedEndingIndex = ref(null); // 선택한 인덱스
const store = useMovieStore();
const prompt = ref('');
const promptError = ref('');
const isSubmitting = ref(false);
const isPrompt = ref(false);
const selected = ref(null);
const movie = ref(null);
const altendings = ref([]);
const route = useRoute();
const router = useRouter();
const movieid = route.params.movieid;

const selectContent = (index) => {
  selected.value = index;
};

watch(altendings.value, (array) => {
  selected.value = array.length
})

const validateForm = () => {
  promptError.value = prompt.value ? '' : '프롬프트는 필수입니다.';
  return !promptError.value;
};

const generateEnding = async () => {
  if (!validateForm()) return;
  isSubmitting.value = true;

  try {
    const { data } = await axios.post(`${store.API_URL}/movies/${movieid}/altends/`, {
      prompt: prompt.value,
      content: altendings.value[selected.value - 1]?.content || null,
    }, {
      headers: { Authorization: `Token ${store.token}` },
    });

    altendings.value.push({ prompt: prompt.value, content: data.alt_ending });
    prompt.value = '';
    isPrompt.value = true;
  } catch (error) {
    console.error('Error generating ending:', error);
  } finally {
    isSubmitting.value = false;
  }
};

const createEnding = async () => {
  try {
    await axios.post(`${store.API_URL}/movies/altends/`, {
      movie_id: movieid,
      prompt: altendings.value[selected.value - 1].prompt,
      content: altendings.value[selected.value - 1].content,
    }, {
      headers: { Authorization: `Token ${store.token}` },
    });
    router.push({ name: 'EndingList' });
  } catch (error) {
    console.error('Error creating ending:', error);
  }
};

onMounted(async () => {
  try {
    const { data } = await axios.get(`${store.API_URL}/movies/${movieid}/`);
    movie.value = data;
  } catch (error) {
    console.error('Error fetching movie:', error);
  }
});

const openModal = () => {
  if (!altendings.value.length) {
    alert('먼저 프롬프트를 생성해주세요.');
    return;
  }
  isModalOpen.value = true;
};

const handleModalConfirm = async (index) => {
  isModalOpen.value = false;
  selectedEndingIndex.value = index; // 선택한 인덱스 저장
  const selectedEnding = altendings.value[selectedEndingIndex.value];

  try {
    await axios.post(`${store.API_URL}/movies/altends/`, {
      movie_id: movieid,
      prompt: selectedEnding.prompt,
      content: selectedEnding.content,
    }, {
      headers: { Authorization: `Token ${store.token}` },
    });
    router.push({ name: 'EndingList' });
  } catch (error) {
    console.error('Error creating ending:', error);
  }
};

const handleModalCancel = () => {
  isModalOpen.value = false;
};


</script>

<style scoped>
.container {
  max-width: 800px;
  margin: auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.title {
  text-align: center;
  margin-bottom: 30px;
  color: #222;
}

.movie-info {
  display: flex;
  gap: 20px;
  margin-bottom: 30px;
}

.poster img {
  max-width: 100%;
  border-radius: 8px;
}

.details p {
  color: #555;
}

.form {
  margin-bottom: 30px;
}

.form-group {
  margin-bottom: 20px;
}

textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  resize: vertical;
}

.error {
  color: red;
  font-size: 14px;
}

.btn {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  color: white;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn-primary:hover {
  background-color: #0056b3;
}

.btn-warning:hover {
  background-color: #ec971f;
}

.btn-secondary {
  background-color: #6c757d;
}

.btn-secondary:hover {
  background-color: #5a6268;
}

.btn-active {
  background-color: #17a2b8;
}

.alt-endings {
  text-align: center;
}

.ending-buttons {
  display: flex;
  gap: 10px;
  justify-content: center;
  margin-bottom: 20px;
}
</style>
