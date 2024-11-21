<template>
    <div
        class="container card py-5"
        v-if="movie"
    >
        <div class="row gx-5 justify-content-evenly">
            <div class="col-lg-3 col-md-6 col-sm-12 text-center card p-2">
                <img :src="API_URL + movie.poster" alt="Movie Poster" class="movie-poster">
                <h1 class="movie-title">{{ movie.title }}</h1>
                <h4>감독: <span>{{ movie.director }}</span></h4>
                <h4>개봉연도: <span>{{ movie.openYear }}</span></h4>
                <h4>장르: <span>{{ movie.genre }}</span></h4>
            </div>
            <div class="col-lg-7 col-md-6 col-sm-12 card p-3">
                <h1>영화 줄거리</h1>
                <p class="movie-summary">
                    {{ movie.plot }}
                </p>
                <div class="button-container d-flex justify-content-end">
                    <button @click="$router.go(-1)" class="btn btn-warning col-12">이전으로</button>
                    <!-- <RouterLink :to="{ name: 'MovieList' }" class="col-3 mx-2">
                    </RouterLink> -->
                    <RouterLink :to="{ name: 'EndingListCreate', params: { movieid: movie.id } }" class="col-3 mx-2">
                        <button class="btn btn-primary col-12">영화 비틀러 가기</button>
                    </RouterLink>
                </div>
            </div>
        </div>
        <br>
        
    </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/counter';
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';

// Sample movie data for demonstration. Replace with actual data as needed.
const route = useRoute()
const movieid = route.params.movieid
const store = useMovieStore()

// const movie = ref({
//     title: '영화 제목',
//     director: '감독 이름',
//     openYear: 2023,
//     genre: '장르'
// });
const movie = ref(null)
const API_URL = store.API_URL + '/api/v1/movies'

onMounted(() => {
    axios({
        method: 'get',
        url: `${API_URL}/${movieid}/`,
    })
    .then((response) => {
        movie.value = response.data
    })
    .catch((error) => {
        console.log(error)
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
}

.movie-summary {
    line-height: 1.6; /* Improve readability of the summary */
    text-align: justify; /* Justify text for a cleaner look */
}

.btn {
    padding: 10px; /* Increase padding for better button appearance */
}

.movie-summary {
    font-size: 15px;
}

</style>