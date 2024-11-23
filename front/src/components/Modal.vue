<template>
  <div class="modal-overlay" @click="closeModal" v-if="store.showModal">
    <div class="modal-content" @click.stop>
      <h2 class="modal-title gradient-text">{{ store.modalConfig.title }}</h2>
      <p v-html="store.modalConfig.message" class="modal-message"></p>
      <button class="btn btn-primary" @click="store.closeModal">확인</button>
    </div>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/counter';

const store = useMovieStore()
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(5px);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: rgba(28, 28, 28, 0.95);
  padding: 2rem;
  border-radius: 12px;
  width: 90%;
  max-width: 500px;
  text-align: center;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.1);
  animation: fadeIn 0.3s ease-out;
}

.gradient-text {
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 700;
}

.modal-title {
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
}

.modal-message {
  color: rgba(255, 255, 255, 0.9);
  font-size: 1.1rem;
  line-height: 1.6;
  margin-bottom: 2rem;
}

.btn {
  padding: 0.5rem 2rem;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 1rem;
  transition: all 0.3s ease;
}

.btn:hover {
  transform: scale(1.05);
}

.btn-primary {
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  color: white;
  border: none;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

@media (max-width: 768px) {
  .modal-content {
    padding: 1.5rem;
    width: 95%;
  }

  .modal-title {
    font-size: 1.3rem;
  }

  .modal-message {
    font-size: 1rem;
  }
}
</style>
