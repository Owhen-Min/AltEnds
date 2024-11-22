<template>
  <div class="container card py-5" v-if="altending">
      <div class="row gx-5 justify-content-evenly">
        <div class="col-lg-3 col-md-6 col-sm-12 text-center card p-2">
          <img 
            :src="store.API_URL + '/movies' + altending.movie_info.poster" 
            alt="Movie Poster" 
            class="movie-poster"
          >
          <h1 class="movie-title">{{ altending.movie_info.title }}</h1>
          <h4>감독: <span>{{ altending.movie_info.director }}</span></h4>
          <h4>개봉연도: <span>{{ altending.movie_info.openYear }}</span></h4>
          <h4>장르: <span>{{ altending.movie_info.genre }}</span></h4>
        </div>
        <div class="col-lg-7 col-md-6 col-sm-12 card p-3">
          <h1>대체결말</h1>
          <p class="movie-summary">{{ altending.content }}</p>
          <div class="button-container d-flex justify-content-end">
            <button @click="$router.go(-1)" class="btn btn-warning col-12">이전으로</button>
            <RouterLink :to="{ name: 'EndingListCreate', params: { movieid: 1 } }" class="col-3 mx-2">
                <button class="btn btn-primary col-12">영화 비틀러 가기</button>
            </RouterLink>
          </div>
        </div>
        <Like
          :pk="altending.id"
          nextUrl="movies/altends"
        />
        <Comments
          :pk="altending.id"
          nextUrl="movies/altends"
        />
      </div>
      <br>
      
  </div>
</template>

<script setup>
import Comments from '@/components/Comments.vue';
import Like from '@/components/Like.vue';
import { useMovieStore } from '@/stores/counter';
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { RouterLink, useRoute, useRouter } from 'vue-router';


const route = useRoute()
const router = useRouter()
const store = useMovieStore()
// Sample movie data for demonstration. Replace with actual data as needed.
const altending = ref(null)
const API_URL = store.API_URL + '/movies/altends'

onMounted(() => {
  axios({
    method: 'get',
    url: `${API_URL}/${route.params.endingid}/`,
    headers: {
        Authorization: `Token ${store.token}`,
      },
  })
    .then((response) => {
      altending.value = response.data
    })
    .catch((error) => {
      store.errorTitle = '조회한 대체 결말이 없습니다.'
      store.showModal = true;
      router.push({ name: 'EndingList' })
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
  font-size: 30px;
}


</style>