<template>
  <div class="d-flex modal-overlay align-items-between" @click="closeModal" v-if="props.isOpen">
    <div class="modal-content" @click.stop>
      <h2 class="modal-title">제목으로 쓰일 프롬프트를 골라주세요.</h2>
      <div class="ending-buttons row">
        <button
          v-for="index in props.options.length"
          :key="'content-' + index"
          @click="selectPromptOption(index)"
          :class="['btn btn-primary', selectedPromptIndex === index ? 'btn-prompt-active' : 'btn-secondary'] "
        >
          프롬프트 {{ index }}
        </button>
        <p>{{ props.options[selectedPromptIndex - 1].prompt }}</p>
      </div>

      <h2 class="modal-title">결말을 골라주세요.</h2>
      <div class="ending-buttons row">
        <button
          v-for="index in props.options.length"
          :key="'content-' + index"
          @click="selectEndingOption(index)"
          :class="['btn', selectedEndingIndex === index ? 'btn-ending-active' : 'btn-secondary']"
        >
          엔딩 {{ index }}
        </button>
        <p v-if="selectedEndingIndex > 0" v-html="props.options[selectedEndingIndex - 1].content" class="modal-message"></p>

        <div class="modal-actions row mx-2">
          <button @click="createEnding" class="btn btn-primary col-6">확인</button>
          <button @click="closeModal" class="btn btn-secondary col-6">취소</button>
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
      console.log(response);
      router.push({ name: 'EndingList'});
    })
      .catch((error)=> {
        console.log(error);
        store.errorTitle = '대체 결말을 업로드 하는 데 실패하였습니다.'
        store.showModal = true;
    })
};

</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: -50vh; /* 상단 위치를 조정하여 중앙에 배치 */
  left: -50vw;
  width: 200%;
  height: 200%;
  background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent black */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000; /* Ensure it appears above all other content */
  max-width: none; /* 최대 너비 제한 제거 */
}

.modal-content {
  background-color: #fff;
  padding: 20px;
  border-radius: 8px;
  width: auto;
  max-width: 500px;
  text-align: center;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25); /* Subtle shadow */
  animation: fadeIn 0.3s ease-out;
  transition: fadeOut 0.3s ease-out;
}

.modal-title {
  margin-bottom: 10px;
  font-size: 20px;
  font-weight: bold;
  color: #333;
}

.btn:hover {
  background-color: #0056b3;
}

/* Fade-in animation */
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

@keyframes fadeOut {
  from {
    opacity: 1;
    transform: scale(0.9);
  }
  to {
    opacity: 0;
    transform: scale(1);
  }
}

.btn-prompt-active {
  background-color: #17a2b8;
}

.btn-ending-active {
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
