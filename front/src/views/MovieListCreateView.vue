<template>
  <div class="container-fluid bg-dark py-5">
    <div class="container card bg-dark text-white py-5">
      <div class="row justify-content-center">
        <div class="col-lg-8 col-md-10 col-sm-12">
          <h2 class="gradient-text text-center mb-4">영화 등록하기</h2>
          
          <form @submit.prevent="createMovie" class="movie-form bg-dark card p-4">
            <div class="form-group mb-4">
              <label for="title" class="form-label">제목</label>
              <div class="position-relative">
                <input 
                  type="text" 
                  id="title" 
                  v-model.trim="title" 
                  @input="debouncedSearch"
                  class="form-control" 
                  placeholder="영화 제목을 입력하세요"
                />
                <div v-if="searchResults.length" class="dropdown-results">
                  <div v-for="movie in searchResults" 
                       :key="movie.id" 
                       class="dropdown-item"
                       @click="selectMovie(movie)">
                    {{ movie.title }} ({{ movie.release_date.substring(0, 4) }})
                    <div class="small text-muted">{{ movie.overview?.substring(0, 50) }}...</div>
                  </div>
                </div>
              </div>
              <span v-if="titleError" class="error">{{ titleError }}</span>
            </div>

            <div class="form-group mb-4">
              <label for="director" class="form-label">감독</label>
              <input 
                type="text" 
                id="director" 
                v-model.trim="director" 
                class="form-control" 
                placeholder="감독 이름을 입력하세요"
              />
              <span v-if="directorError" class="error">{{ directorError }}</span>
            </div>

            <div class="form-group mb-4">
              <label for="openYear" class="form-label">개봉년도</label>
              <input 
                type="number" 
                id="openYear" 
                v-model.number="openYear" 
                class="form-control" 
                placeholder="개봉년도를 입력하세요"
              />
              <span v-if="openYearError" class="error">{{ openYearError }}</span>
            </div>

            <div class="form-group mb-4">
              <label for="genre" class="form-label">장르</label>
              <input 
                type="text" 
                id="genre" 
                v-model.trim="genre" 
                class="form-control" 
                placeholder="장르를 입력하세요"
              />
              <span v-if="genreError" class="error">{{ genreError }}</span>
            </div>

            <div class="form-group mb-4">
              <label for="synopsis" class="form-label">시놉시스</label>
              <textarea 
                id="synopsis" 
                v-model.trim="synopsis" 
                class="form-control" 
                placeholder="시놉시스를 입력하세요"
                rows="3"
              ></textarea>
              <span v-if="synopsisError" class="error">{{ synopsisError }}</span>
            </div>

            <div class="form-group mb-4">
              <label for="plot" class="form-label">줄거리</label>
              <textarea 
                id="plot" 
                v-model.trim="plot" 
                class="form-control" 
                placeholder="줄거리를 입력하세요"
                rows="5"
              ></textarea>
              <span v-if="plotError" class="error">{{ plotError }}</span>
            </div>

            <div class="form-group mb-4">
              <label for="poster" class="form-label">포스터</label>
              <input 
                type="file" 
                id="poster" 
                @change="handleFileUpload" 
                class="form-control" 
                accept="image/*"
              />
              <div v-if="posterPreview" class="mt-2">
                <img :src="posterPreview" class="poster-preview" alt="Movie poster preview">
              </div>
              <span v-if="posterError" class="error">{{ posterError }}</span>
            </div>

            <div class="d-flex justify-content-between">
              <RouterLink :to="{ name: 'MovieList' }" class="btn btn-warning">
                이전으로
              </RouterLink>
              <button type="submit" class="btn btn-primary" :disabled="isSubmitting">
                {{ isSubmitting ? '등록 중...' : '영화 등록하기' }}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/counter';
import axios from 'axios';
import { ref, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';

const store = useMovieStore();
const router = useRouter();

// 폼 데이터
const title = ref('');
const director = ref('');
const openYear = ref(2024);
const genre = ref('');
const synopsis = ref('');
const plot = ref('');
const poster = ref(null);

// 에러 상태
const titleError = ref('');
const directorError = ref('');
const openYearError = ref('');
const genreError = ref('');
const synopsisError = ref('');
const plotError = ref('');
const posterError = ref('');

const isSubmitting = ref(false);

// 검색 관련 상태
const searchTitle = ref('');
const searchResults = ref([]);

let searchTimeout = null;

const posterPreview = ref('');

const handleFileUpload = (event) => {
  const file = event.target.files[0];
  if (file) {
    poster.value = file;
    posterPreview.value = URL.createObjectURL(file);
  }
};

const validateForm = () => {
  titleError.value = title.value ? '' : '제목은 필수입니다.';
  directorError.value = director.value ? '' : '감독은 필수입니다.';
  openYearError.value = openYear.value ? '' : '개봉년도는 필수입니다.';
  genreError.value = genre.value ? '' : '장르는 필수입니다.';
  synopsisError.value = synopsis.value ? '' : '시놉시스는 필수입니다.';
  plotError.value = plot.value ? '' : '줄거리는 필수입니다.';

  return !titleError.value && !directorError.value && !openYearError.value && 
         !genreError.value && !synopsisError.value && !plotError.value;
};

const debouncedSearch = () => {
  if (searchTimeout) clearTimeout(searchTimeout);
  
  if (title.value.length < 2) {
    searchResults.value = [];
    return;
  }

  searchTimeout = setTimeout(async () => {
    try {
      const response = await axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/search/movie`,
        params: {
          query: title.value,
          language: 'ko-KR',
          api_key: 'dde7dc64da0d0ca43e44ed462199a312'
        }
      });
      
      searchResults.value = response.data.results;
    } catch (error) {
      console.error('영화 검색 중 오류 발생:', error);
      store.showModalMessage('영화 검색에 실패했습니다.', error);
    }
  }, 500);
};

const selectMovie = async (movie) => {
  title.value = movie.title;
  openYear.value = parseInt(movie.release_date.substring(0, 4));
  synopsis.value = movie.overview;
  
  if (movie.poster_path) {
    try {
      const imageUrl = `https://image.tmdb.org/t/p/original${movie.poster_path}`;
      posterPreview.value = imageUrl;
      
      const response = await fetch(imageUrl);
      const blob = await response.blob();
      const file = new File([blob], `${movie.title}_poster.jpg`, { type: 'image/jpeg' });
      poster.value = file;
    } catch (error) {
      console.error('포스터 이미지 가져오기 실패:', error);
      store.showModalMessage('포스터 이미지를 가져오는데 실패했습니다.', error);
    }
  }

  searchResults.value = [];
};

// 컴포넌트가 언마운트될 때 타임아웃 정리
onUnmounted(() => {
  if (searchTimeout) clearTimeout(searchTimeout);
  if (posterPreview.value) {
    URL.revokeObjectURL(posterPreview.value);
  }
});

const createMovie = async () => {
  if (!validateForm()) return;

  isSubmitting.value = true;

  try {
    const formData = new FormData();
    formData.append('title', title.value);
    formData.append('director', director.value);
    formData.append('openYear', openYear.value);
    formData.append('genre', genre.value);
    formData.append('synopsis', synopsis.value);
    formData.append('plot', plot.value);
    if (poster.value) {
      formData.append('poster', poster.value);
    }

    const response = await axios.post(`${store.API_URL}/movies/`, formData, {
      headers: {
        'Authorization': `Token ${store.token}`,
        'Content-Type': 'multipart/form-data'
      }
    });
    
    router.push({ name: 'MovieList' });
  } catch (error) {
    store.showModalMessage('영화 등록에 실패했습니다.', error);
  } finally {
    isSubmitting.value = false;
  }
};
</script>

<style scoped>
.container {
  background: rgba(255, 255, 255, 0.05) !important;
  backdrop-filter: blur(10px);
  border: none;
}

.gradient-text {
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 700;
  letter-spacing: 1px;
}

.article-form {
  background: rgba(255, 255, 255, 0.05) !important;
  backdrop-filter: blur(10px);
  border: none;
}

.form-label {
  color: #ffb88c;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.form-control {
  background: rgba(255, 255, 255, 0.1);
  border: 2px solid rgba(255, 255, 255, 0.1);
  color: white;
  transition: all 0.3s ease;
}

.form-control:focus {
  background: rgba(255, 255, 255, 0.15);
  border-color: #ffb88c;
  box-shadow: none;
  color: white;
}

.form-control::placeholder {
  color: rgba(255, 255, 255, 0.5);
}

.error {
  color: #ff6b6b;
  font-size: 0.9rem;
  margin-top: 0.5rem;
}

.btn {
  padding: 0.5rem 1.5rem;
  transition: transform 0.3s ease;
}

.btn:hover {
  transform: scale(1.05);
}

.btn-primary {
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  border: none;
}

.btn-warning {
  background: rgba(255, 255, 255, 0.1);
  border: 2px solid #ffb88c;
  color: white;
}

.btn-warning:hover {
  background: rgba(255, 255, 255, 0.2);
}

.btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

@media (max-width: 768px) {
  .gradient-text {
    font-size: 1.5rem;
  }
}

.cursor-pointer {
  cursor: pointer;
}

.hover-bg-light:hover {
  background: rgba(255, 255, 255, 0.1);
}

.position-relative {
  position: relative;
}

.dropdown-results {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  background: #2c3e50;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 4px;
  max-height: 200px;
  overflow-y: auto;
  z-index: 1000;
}

.dropdown-item {
  padding: 8px 12px;
  cursor: pointer;
  color: white;
}

.dropdown-item:hover {
  background: rgba(255, 255, 255, 0.1);
}

.poster-preview {
  max-width: 200px;
  height: auto;
  border-radius: 4px;
  margin-top: 10px;
}
</style>