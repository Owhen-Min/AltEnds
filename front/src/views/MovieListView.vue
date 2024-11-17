vue
<template>
  <div class="container py-2 my-3">
    <div class="col-12">
      <h3>이번 주 영화 정보</h3>
    </div>
    <div class="row justify-content-center">
        <div 
          class="card align-items-center justify-content-center m-2 col-3" 
          v-for="(movie, index) in movies" 
          :key="index" 
          @click="goDetail(index+1)"
        >
          <img 
            src="https://m.media-amazon.com/images/I/81EBp0vOZZL.jpg" 
            alt="Movie Poster" 
            class="movie-poster"
          >
          <br>
          <h4>{{ movie.title }}</h4>
        </div>
      </div>
    </div>
</template>

<script setup>
import router from '@/router';
import { ref } from 'vue';

// Sample movie data for demonstration
const movies = ref([
  { title: '리얼', description: 'A gripping thriller about reality.' },
  { title: '성냥팔이 소녀의 재림', description: 'A touching story about hope.' },
  { title: '클레멘타인', description: 'A drama about love and loss.' },
  { title: '웃겨야 사는 영화', description: 'A hilarious comedy that will make you laugh.' },
  { title: '영화 5', description: 'Description for movie 5.' },
  { title: '영화 6', description: 'Description for movie 6.' }
]);

const selectedMovie = ref(null);

const goDetail = ((index) => {
  router.push(`/movielist/${index}`)
})
</script>

<style scoped>
.container {
  text-align: center;
}

.card {
  padding: 1rem; /* Add padding inside each card */
  cursor: pointer; /* Change cursor to pointer on hover */
}

.movie-poster {
  max-width: 100%; /* Ensure the image fits within the card */
  height: auto; /* Maintain aspect ratio of the image */
}

.row {
  display: flex; /* Use flexbox for the row */
  flex-wrap: wrap; /* Allow wrapping of cards */
}

.movie-detail {
  padding: 1rem;
}
</style>