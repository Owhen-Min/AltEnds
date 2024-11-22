<template>
  <div class="modal-overlay" v-if="isVisible">
    <div class="modal-content">
      <h3 class="modal-title">{{ title }}</h3>
      <p class="modal-message" v-for="message in messages">
        {{ message }}
      </p>
      <button class="btn btn-primary" @click="closeModal">확인</button>
    </div>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/counter';

const store = useMovieStore()


const props = defineProps({
  title: String,
  messages: Array,
  isVisible: Boolean,
});


const closeModal = () => {
  store.showModal = false
};
</script>

<style scoped>
/* Fullscreen semi-transparent background */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent black */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000; /* Ensure it appears above all other content */
}

/* Modal box styling */
.modal-content {
  background-color: #fff;
  padding: 20px;
  border-radius: 8px;
  width: 90%;
  max-width: 400px;
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
