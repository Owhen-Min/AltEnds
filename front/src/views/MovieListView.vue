<template>
  <div class="container-fluid bg-dark py-5">
    <div class="container">
      <h3 class="display-4 text-center my-5 gradient-text">이번 주 영화 정보</h3>
      
      <div class="row g-4">
        <div 
          class="col-lg-3 col-md-4 col-sm-6" 
          v-for="movie in movies" 
          :key="movie.id"
        >
          <div class="card h-100 bg-dark movie-card border-0" @click="showMovieDetail(movie.id)">
            <div class="card-img-wrapper position-relative">
              <img 
                :src="store.BASE_URL + movie.poster" 
                :alt="movie.title" 
                class="card-img-top rounded-3"
              >
              <div class="overlay d-flex align-items-center justify-content-center">
                <button class="btn btn-outline-light btn-hover-effect">
                  상세보기 <i class="bi bi-arrow-right-short"></i>
                </button>
              </div>
            </div>
            <div class="card-body text-center">
              <h5 class="card-title text-white mb-0">{{ movie.title }}</h5>
            </div>
          </div>
        </div>
      </div>
    </div>
    <MovieDetailModal 
      v-if="showModal"
      :movieid="selectedMovie"
      @close="closeModal"
    />
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movieStore';
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import MovieDetailModal from '@/components/MovieDetailModal.vue';

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'

const store = useMovieStore()
const movies = ref(null)
const API_URL = store.API_URL + '/movies'

const router = useRouter()

const selectedMovie = ref(null)
const showModal = ref(false)

const showMovieDetail = function (movieId) {
  selectedMovie.value = movieId
  showModal.value = true
}

const closeModal = function () {
  showModal.value = false
  selectedMovie.value = null
}

onMounted(() => {
  axios({
    method: 'get',
    url: `${API_URL}/`
  })
    .then((response) => {
      movies.value = response.data
      
    })
    .catch((error) => {
      store.showModalMessage('영화들을 가져오는 데 실패했습니다.', error)
    })
})

</script>

<style scoped>
.gradient-text {
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 700;
  letter-spacing: 1px;
}

.movie-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: pointer;
  background: rgba(255, 255, 255, 0.05) !important;
  backdrop-filter: blur(10px);
}

.movie-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 10px 20px rgba(255, 107, 107, 0.2);
}

.card-img-wrapper {
  overflow: hidden;
  border-radius: 12px;
}

.card-img-top {
  transition: transform 0.3s ease;
  height: 400px;
  object-fit: cover;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.movie-card:hover .overlay {
  opacity: 1;
}

.btn-hover-effect {
  border: 2px solid white;
  padding: 8px 20px;
  font-weight: 500;
  transition: all 0.3s ease;
}

.btn-hover-effect:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: scale(1.05);
}

.card-title {
  font-size: 1.1rem;
  font-weight: 600;
}

@media (max-width: 768px) {
  .card-img-top {
    height: 300px;
  }
  
  .gradient-text {
    font-size: 2rem;
  }
}

.modal-content {
  background: rgba(33, 37, 41, 0.95) !important;
  backdrop-filter: blur(10px);
}

.movie-poster {
  max-width: 100%;
  height: auto;
  border-radius: 12px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

.movie-title {
  margin: 15px 0;
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 700;
}

.section-title {
  font-size: 1.8rem;
  margin-bottom: 1rem;
  color: #ff6b6b;
}

.movie-synopsis {
  font-size: 1.1rem;
  line-height: 1.8;
  color: #e0e0e0;
  background: rgba(0, 0, 0, 0.2);
  padding: 1.5rem;
  border-radius: 8px;
}
</style>