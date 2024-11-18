import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'


// export const useMovieStore = defineStore('movie', () => {
//   const movies = ref([])
//   const API_URL = 'http://127.0.0.1:8000/api/v1'
//   const getMovies = function () {
//     axios({
//       method: 'get',
//       url: `${API_URL}/movies/`
//     })
//       .then((response) => {
//         console.log('영화목록 가져오기 성공')
//         console.log(response.data)
//         movies.value = response.data
//       })
//       .catch((error) => {
//         console.log('실패')
//         console.log(error)
//       })
//   }
//   return { movies, API_URL, getMovies, }
// })
