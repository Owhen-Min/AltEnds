<template>
  <div>
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
              :alt="movie.title + '의 포스터'"
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
const router = useRouter()
const weeklyMovies = store.weeklyMovie;

const goDetail = ((movieid) => {
  router.push({ name: 'MovieListDetail', params: { movieid: movieid }})
})

onMounted(() => {
  store.getMovies();
})

</script>

<style scoped>
.carousel-item img {
  border: 1px solid black;
  border-radius: 10px;
}
.card-header {
  background-color: #f8f9fa;
  font-weight: bold;
  text-align: center;
}
</style>
