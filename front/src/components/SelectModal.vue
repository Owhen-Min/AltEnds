<template>
  <div class="modal-overlay" @click="closeModal" v-if="props.isOpen">
    <div class="modal-content card bg-dark text-white" @click.stop>
      <h2 class="gradient-text mb-4">제목으로 쓰일 프롬프트를 골라주세요.</h2>
      <div class="selection-container mb-4">
        <div class="ending-buttons">
          <button
            v-for="index in props.options.length"
            :key="'prompt-' + index"
            @click="selectPromptOption(index)"
            :class="['btn', selectedPromptIndex === index ? 'btn-active' : 'btn-secondary']"
          >
            프롬프트 {{ index }}
          </button>
        </div>
        <div class="content-box mt-3">
          <p>{{ props.options[selectedPromptIndex - 1].prompt }}</p>
        </div>
      </div>

      <h2 class="gradient-text mb-4">결말을 골라주세요.</h2>
      <div class="selection-container">
        <div class="ending-buttons">
          <button
            v-for="index in props.options.length"
            :key="'ending-' + index"
            @click="selectEndingOption(index)"
            :class="['btn', selectedEndingIndex === index ? 'btn-active' : 'btn-secondary']"
          >
            엔딩 {{ index }}
          </button>
        </div>
        <div class="content-box mt-3" v-if="selectedEndingIndex > 0">
          <p class="alt-ending" v-html="props.options[selectedEndingIndex - 1].content"></p>
        </div>

        <div class="modal-actions mt-4">
          <button @click="createEnding" class="btn btn-primary me-2">확인</button>
          <button @click="closeModal" class="btn btn-warning">취소</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import axios from 'axios';
import { useMovieStore } from '@/stores/counter';
import { useRouter } from 'vue-router';

const store = useMovieStore();  
const router = useRouter(); 

const props = defineProps({
  isOpen: Boolean,
  options: Array, // 프롬프트와 결말 리스트
  movieid: String,
});

const selectedPromptIndex = ref(1);
const selectedEndingIndex = ref(1);

watch (() => props.isOpen, (newVal) => {
  selectedEndingIndex.value = props.options.length;
})

const emit = defineEmits(['cancel']);


const selectPromptOption = (index) => {
  selectedPromptIndex.value = index;
};

const selectEndingOption = (index) => {
  selectedEndingIndex.value = index;
};

const closeModal = () => {
  emit('cancel');
};

const createEnding = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/movies/altends/`,
    data: {
      movie_id: props.movieid,
      prompt: props.options[selectedPromptIndex.value - 1].prompt,
      content: props.options[selectedEndingIndex.value - 1].content,
    }, 
    headers: { Authorization: `Token ${store.token}` },
    })
    .then(response => {
      router.push({ name: 'EndingList'});
    })
      .catch((error)=> {
        store.errorTitle = '대체 결말을 업로드 하는 데 실패하였습니다.'
        store.showModal = true;
    })
};

</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  position: fixed;
  top: calc(90% - 200px);
  left: 50%;
  transform: translate(-50%, -50%);
  background: rgba(255, 255, 255, 0.05) !important;
  backdrop-filter: blur(10px);
  padding: 2rem;
  border-radius: 12px;
  width: 90%;
  max-width: 70%;
  height: 80vh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.gradient-text {
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 700;
  font-size: 1.5rem;
}

.ending-buttons {
  display: flex;
  gap: 10px;
  justify-content: center;
  flex-wrap: wrap;
}

.btn {
  padding: 0.5rem 1.5rem;
  transition: transform 0.3s ease;
}

.btn-active {
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  border: none;
  color: white;
}

.btn-secondary {
  background: rgba(255, 255, 255, 0.1);
  border: 2px solid #6c757d;
  color: white;
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

.btn:hover {
  transform: scale(1.05);
}

.content-box {
  background: rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  padding: 1.5rem;
  margin-top: 1rem;
  color: #e0e0e0;
  flex: 1;
  overflow-y: auto;
}

.selection-container {
  margin-bottom: 1rem;
  flex: 1;
  height: 20%;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.selection-container.mb-4 {
  flex: 0 0 auto;
  max-height: 200px;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: scale(0.9);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.modal-actions {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-top: auto;
  padding-top: 1rem;
}

.alt-ending {
  white-space: pre-line;
}
</style>