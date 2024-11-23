<template>
    <div class="container-fluid bg-dark py-5">
        <div class="container card bg-dark text-white py-5" v-if="movie">
        <div class="row gx-5 justify-content-evenly">
            <div class="col-lg-3 col-md-6 col-sm-12 text-center card p-2">
                <img :src="store.BASE_URL + movie.poster" alt="Movie Poster" class="movie-poster">
                <div class="movie-details">
                    <h3 class="text-warning mb-4">{{ movie.title }}</h3>
                    <h6>감독: <span class="text-light">{{ movie.director }}</span></h6>
                    <h6>개봉연도: <span class="text-light">{{ movie.openYear }}</span></h6>
                    <h6>장르: <span class="text-light">{{ movie.genre }}</span></h6>
                </div>
            </div>
            <div class="col-lg-7 col-md-6 col-sm-12 card p-3">
                <h1 class="text-white">영화 줄거리</h1>
                <p class="movie-summary">
                    {{ movie.plot }}
                </p>
                <div class="button-container row justify-content-around p-2">
                    <button @click="$router.go(-1)" class="btn btn-warning col-sm-12 col-md-5 my-2">이전으로</button>
                    <button class="btn btn-primary col-sm-12 col-md-5 my-2">
                      <RouterLink :to="{ name: 'EndingListCreate', params: { movieid: movie.id } }" class="col-12">영화 비틀러 가기</RouterLink>
                    </button>
                </div>
            </div>
        </div>
        <br>
      </div>
    </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/counter';
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';

const store = useMovieStore()
const route = useRoute()

const movieid = route.params.movieid
const movie = ref(null)
const API_URL = store.API_URL + '/movies'


onMounted(() => {
    axios({
        method: 'get',
        url: `${API_URL}/${movieid}/`,
    })
    .then((response) => {
        movie.value = response.data
    })
    .catch((error) => {
    store.showModalMessage('조회한 영화가 없습니다.')
    })
})

</script>

<style scoped>
.container {
    justify-content: start;
    text-align: start;
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

</style>
