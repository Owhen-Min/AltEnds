<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-content">
      <div class="container card bg-dark text-white py-5" v-if="movie">
        <div class="row gx-5 justify-content-evenly">
            <div class="col-lg-3 col-md-6 col-sm-12 text-center card p-4">
                <img :src="store.BASE_URL + movie.poster" alt="Movie Poster" class="movie-poster mb-4">
                <div class="movie-details">
                    <h2 class="movie-title">{{ movie.title }}</h2>
                    <p class="text-muted mb-2">개봉연도: {{ movie.openYear }}</p>
                </div>
            </div>
            <div class="col-lg-7 col-md-6 col-sm-12 card p-4">
                <h2 class="section-title mb-4">영화 시놉시스</h2>
                <p class="movie-summary mb-4">
                    {{ movie.synopsis }}
                </p>
                <div class="button-container row justify-content-around p-2">
                    <button @click.self="$emit('close')" class="btn btn-warning col-sm-12 col-md-5 my-2">이전으로</button>
                    <button class="btn btn-primary col-sm-12 col-md-5 my-2">
                      <RouterLink :to="{ name: 'EndingListCreate', params: { movieid: movie.id } }" class="col-12 text-white text-decoration-none">영화 비틀러 가기</RouterLink>
                    </button>
                </div>
            </div>
        </div>
        <br>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/counter';
import axios from 'axios';
import { watch, ref } from 'vue';
import { useRoute } from 'vue-router';

const store = useMovieStore()
const route = useRoute()

const props = defineProps({
  movieid: {
    type: String,
    required: true
  }
})

const movie = ref(null)
const API_URL = store.API_URL + '/movies'

watch(() => props.movieid, (newVal) => {
  if (newVal) {
    axios({
      method: 'get',
      url: `${API_URL}/${newVal}/`,
    })
    .then((response) => {
      movie.value = response.data
    })
    .catch((error) => {
      store.showModalMessage('조회한 영화가 없습니다.')
    })
  }
}, { immediate: true })

</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.75);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  overflow-y: auto;
  backdrop-filter: blur(5px);
}

.modal-content {
  width: 90%;
  max-width: 1200px;
  margin: 2rem auto;
  animation: modal-fade 0.3s ease-in-out;
}

@keyframes modal-fade {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.container {
  margin: 0 auto;
  background: rgba(255, 255, 255, 0.1) !important;
  backdrop-filter: blur(10px);
}

.movie-poster {
    max-width: 100%; /* Ensure the image fits within the card */
    height: auto; /* Maintain aspect ratio of the image */
    border-radius: 8px; /* Add rounded corners to the poster */
}

.movie-title {
    margin: 10px 0; /* Add space around the title */
    color: lightslategray;
}

.movie-summary {
    line-height: 1.6; /* Improve readability of the summary */
    text-align: justify; /* Justify text for a cleaner look */
    text-wrap: balance;
    text-align-last: left;
    text-indent: 1em;
    color: white;
    line-break: anywhere;
}

.btn {
    padding: 10px; /* Increase padding for better button appearance */
}

.movie-summary {
    font-size: 15px;
}

.card {
  background: rgba(255, 255, 255, 0.05) !important;
  backdrop-filter: blur(10px);
  border: none;
}

.movie-title {
  margin: 15px 0;
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 700;
}

.movie-poster {
  max-width: 100%;
  height: auto;
  border-radius: 12px;
  transition: transform 0.3s ease;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
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

.movie-details {
    padding: 1rem;
    background: rgba(0, 0, 0, 0.2);
    border-radius: 8px;
    margin-top: 1rem;
}

.section-title {
    font-size: 2rem;
    font-weight: 600;
    background: linear-gradient(45deg, #ff6b6b, #ffb88c);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1.5rem;
}

.movie-summary {
    font-size: 1.1rem;
    line-height: 1.8;
    color: #e0e0e0;
    padding: 1rem;
    background: rgba(0, 0, 0, 0.2);
    border-radius: 8px;
    margin-bottom: 2rem;
}

.card {
    padding: 2rem !important;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
}

</style>
