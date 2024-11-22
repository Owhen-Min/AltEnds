<template>
  <div class="d-flex modal-overlay align-items-between" @click="closeModal" v-if="isVisible">
    <div class="modal-content" @click.stop>
      <h2 class="modal-title">{{ title }}</h2>
      <p v-html="message" class="modal-message" ></p>
      <button class="btn btn-primary" @click="closeModal">확인</button>
    </div>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/counter';

const store = useMovieStore()


const props = defineProps({
  title: String,
  message: String,
  isVisible: Boolean,
});


const closeModal = () => {
  store.showModal = false
  store.errorTitle = ''
  store.errorMessage = ''
};
</script>

<style scoped>
/* Fullscreen semi-transparent background */
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

/* Modal box styling */
.modal-content {
  background-color: #fff;
  padding: 20px;
  border-radius: 8px;
  width: auto;
  max-width: 500px;
  text-align: center;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25); /* Subtle shadow */
  animation: fadeIn 0.3s ease-out;
}

/* Title styling */
.modal-title {
  margin-bottom: 10px;
  font-size: 20px;
  font-weight: bold;
  color: #333;
}

/* Button styling */
.btn {
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  background-color: #007bff;
  color: white;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
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
</style>
