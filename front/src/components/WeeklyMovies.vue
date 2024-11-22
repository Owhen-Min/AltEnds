<template>
  <div class="movie-section">
    <h2 class="card-header">주간 영화 목록</h2>
    <!-- Bootstrap Carousel -->
    <div id="movieCarousel" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div
          class="carousel-item"
          :class="{ active: index === 0 }"
          v-for="(movie, index) in weeklyMovies"
          :key="movie.id"
        >
          <div class="d-flex flex-column align-items-center">
            <img
              @click="goDetail(movie.id)"
              class="d-block w-50"
              :src="store.BASE_URL + movie.poster"
              :alt="`${movie.title}의 포스터`"
            />
          </div>
        </div>
      </div>

      <!-- Carousel Controls -->
      <button
        class="carousel-control-prev"
        type="button"
        data-bs-target="#movieCarousel"
        data-bs-slide="prev"
      >
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">이전</span>
      </button>
      <button
        class="carousel-control-next"
        type="button"
        data-bs-target="#movieCarousel"
        data-bs-slide="next"
      >
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">다음</span>
      </button>
    </div>
  </div>
</template>

<script setup>
import { useMovieStore } from "@/stores/counter";
import { onMounted } from "vue";
import { useRouter } from 'vue-router';

const store = useMovieStore();
const router = useRouter();
const weeklyMovies = store.weeklyMovie;

const goDetail = (movieid) => {
  router.push({ name: 'MovieListDetail', params: { movieid } });
}

onMounted(() => {
  store.getMovies();
});
</script>

<style scoped>
@import url('https://rsms.me/inter/inter-ui.css');

::selection {
  background: #2D2F36;
}

::-webkit-selection {
  background: #2D2F36;
}

::-moz-selection {
  background: #2D2F36;
}

.card-header {
  border-radius: 20px;
  background-color: #f8f9fa;
  font-weight: bold;
  text-align: center;
  padding: 17px;
  margin-bottom: 20px;
}

.page {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-radius: 20px;
}

.carousel-inner {
  display: flex;
  justify-content: start;
  align-items: center;
}

.carousel-item img {
  border-radius: 10px;
  transition: transform 0.3s;
  cursor: pointer;
}

.carousel-item img:hover {
  transform: scale(1.05);
}

.carousel-control-prev-icon,
.carousel-control-next-icon {
  background-color: rgba(0, 0, 0, 0.5);
  border-radius: 50%;
  padding: 10px;
}

@media (max-width: 767px) {
  .movie-section {
    padding: 10px;
  }

  .carousel-item img {
    width: 70%;
  }
}
</style>