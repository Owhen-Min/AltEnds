<template>
  <div class="container py-2 my-3">
    <div class="col-12">
      <h3>이번 주 영화 정보</h3>
    </div>
    <div class="row justify-content-center">
      <div 
        class="card align-items-center justify-content-center m-2 col-3" 
        v-for="movie in movies" 
        :key="movie.id" 
        @click="goDetail(movie.id)"
      >
        <img 
          :src="API_URL + movie.poster" 
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
import axios from 'axios';
import { computed, onMounted, ref } from 'vue';
// Sample movie data for demonstration
const movies = ref(null)
const API_URL = 'http://127.0.0.1:8000/api/v1/movies'

const goDetail = ((movieid) => {
  router.push({ name: 'EndingListCreate', params: { movieid: movieid } })
})

onMounted(() => {
  axios({
    method: 'get',
    url: `${API_URL}/`
  })
    .then((response) => {
      console.log('영화목록 가져오기 성공')
      console.log(response.data)
      movies.value = response.data
      
    })
    .catch((error) => {
      console.log('실패')
      console.log(error)
    })
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