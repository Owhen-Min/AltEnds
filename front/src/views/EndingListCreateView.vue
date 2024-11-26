<template>
  <div class="container-fluid bg-dark py-5">
    <div class="container card bg-dark text-white py-5">
      <h1 class="gradient-text text-center mb-5">영화 비틀러 가기</h1>

    <!-- Movie Information -->
    <div class="movie-info row justify-content-evenly" v-if="movie">
      <img :src="store.BASE_URL + movie.poster" :alt="movie.title" class="movie-poster poster col-xl-3 col-lg-4 col-md-6 col-sm-12 text-center card p-2"/>
      <div class="details col-lg-7 col-md-5 col-sm-12 card p-3">
        <h6 class="gradient-text">원본 시놉시스</h6>
        <p class="movie-summary text-white">{{ movie.synopsis }}</p>
      </div>
    </div>

    <div class="token-info text-center mb-3">
      <p>현재 토큰 수: <strong>{{ tokens }}</strong></p>
    </div>
    <!-- Prompt Form -->
    <form @submit.prevent="generateEnding" v-if="!isPrompt" class="form">
      <div class="form-group">
        <label for="prompt">원하는 변경사항을 입력해주세요</label><br><br>
        <textarea
          id="prompt"
          v-model.trim="prompt"
          placeholder="프롬프트를 입력하세요"
          required
        ></textarea>
        <span v-if="promptError" class="error">{{ promptError }}</span>
      </div>
      <div class="text-center">
        <button type="submit" class="btn btn-primary btn-lg btn-block mb-3" :disabled="isSubmitting">
          {{ isSubmitting ? '작성 중...' : '대체결말 생성하기' }}
        </button>
      </div>
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

      <div v-if="altendings[selected - 1]" class="ending-content card p-4">
        <div class="prompt-section mb-4">
          <h5 class="gradient-text-small mb-3">프롬프트</h5>
          <div class="prompt-box">
            <p class="mb-0">{{ altendings[selected - 1].prompt }}</p>
          </div>
        </div>
        
        <div class="ending-section">
          <h5 class="gradient-text-small mb-3">대체 결말</h5>
          <div class="ending-box">
            <p v-html="altendings[selected - 1].content" class="alt-ending mb-0"></p>
          </div>
        </div>
      </div>
      
      <!-- Re-Prompt Form -->
      <form @submit.prevent="generateEnding" class="form">
        <div class="form-group">
          <label for="re-prompt">마음에 안드는 부분이 있다면 알려주세요:</label><br>
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
        :options="altendings"
        :movieid="movieid"
        @cancel="handleModalCancel"
      />
      </div>
    </div>
  </div>    
</template>

<script setup>
import SelectModal from '@/components/SelectModal.vue';
import { useMovieStore } from '@/stores/movieStore';
import axios from 'axios';
import { ref, onMounted, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';


const isModalOpen = ref(false);
const store = useMovieStore();
const prompt = ref('');
const promptError = ref('');
const isSubmitting = ref(false);
const isPrompt = ref(false);
const selected = ref(null);
const movie = ref(null);
const altendings = ref([]);
const route = useRoute();
const movieid = route.params.movieid;
const tokens = ref(store.user.token)

const selectContent = (index) => {
  selected.value = index;
};

watch(altendings, (newValue) => {
  if (newValue.length) {
    selected.value = newValue.length
  }
}, { deep: true })

const validateForm = () => {
  promptError.value = prompt.value ? '' : '프롬프트는 필수입니다.';
  return !promptError.value;
};

const generateEnding = async () => {
  if (!validateForm()) return;
  isSubmitting.value = true;

  try {
    const response = await axios.post(`${store.API_URL}/movies/${movieid}/altends/`, {
      prompt: prompt.value,
      content: altendings.value[selected.value - 1]?.content || null,
    }, {
      headers: { Authorization: `Token ${store.token}` },
    });
    altendings.value.push({ prompt: prompt.value, content: response.data.alt_ending });
    tokens.value = response.data.user_token
    prompt.value = '';
    isPrompt.value = true;
  } catch (error) {
    if (error.response?.status === 403) {
      store.showModalMessage('사용 가능한 토큰이 부족합니다.')
      promptError.value = '사용 가능한 토큰이 부족합니다.'
    } else {
      store.showModalMessage('대체 결말을 만드는 데 실패했습니다.', error)
    }
  } finally {
    isSubmitting.value = false;
  }
};

const fetchMovie = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/movies/${movieid}/`);
    movie.value = response.data;
  } catch (error) {
    store.showModalMessage('영화를 가져오는 데 실패했습니다.', error)
  }
};


onMounted(() => {
  store.getMyProfile()
  fetchMovie()
});

const openModal = () => {
  if (!altendings.value.length) {
    alert('먼저 프롬프트를 생성해주세요.');
    return;
  }
  isModalOpen.value = true;
};

const handleModalCancel = () => {
  isModalOpen.value = false;
};


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
  font-size: 2rem;
}

.movie-poster {
  max-width: auto;
  height: 100%;
  border-radius: 12px;
  transition: transform 0.3s ease;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

.movie-title {
  margin: 15px 0;
  color: lightslategray;
}

.movie-summary {
  line-height: 1.6;
  text-align: justify;
  color: white;
  font-size: 1.5rem;
}

.card {
  background: rgba(255, 255, 255, 0.05) !important;
  backdrop-filter: blur(10px);
  border: none;
}

textarea {
  width: 60%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  resize: vertical;
  background: rgba(255, 255, 255, 0.1);
  color: white;
}

.btn-primary {
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  border: none;
  transition: transform 0.3s ease;
}

.btn-primary:hover {
  transform: scale(1.05);
}

.btn-warning {
  background: rgba(255, 255, 255, 0.1);
  border: 2px solid #ffb88c;
  color: white;
  transition: transform 0.3s ease;
}

.btn-warning:hover {
  transform: scale(1.05);
  background: rgba(255, 255, 255, 0.2);
}

.btn-secondary {
  background: rgba(255, 255, 255, 0.1);
  border: 2px solid #6c757d;
}

.btn-active {
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  border: none;
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
  font-size: 1.2rem;
  text-align: center;
}

.error {
  color: red;
  font-size: 14px;
}

.alt-endings {
  text-align: center;
}

.alt-ending {
  white-space: pre-line;
}

.ending-buttons {
  display: flex;
  gap: 10px;
  justify-content: center;
  margin-bottom: 20px;
}


.ending-content {
  margin: 2rem auto;
  max-width: 800px;
}

.gradient-text-small {
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 600;
  font-size: 1.2rem;
}

.prompt-box, .ending-box {
  background: rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  padding: 1.5rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.prompt-box p, .ending-box p {
  color: #e0e0e0;
  line-height: 1.6;
  font-size: 1.1rem;
}

.ending-box {
  background: rgba(255, 255, 255, 0.1);
}
</style>
