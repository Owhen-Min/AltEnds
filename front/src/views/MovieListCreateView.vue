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
              <label for="openYear" class="form-label">개봉연도</label>
              <input 
                type="number" 
                id="openYear" 
                v-model.number="openYear" 
                class="form-control" 
                placeholder="개봉연도를 입력하세요"
              />
              <span v-if="openYearError" class="error">{{ openYearError }}</span>
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
                :disabled="isGeneratingPlot"
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
import OpenAI from 'openai';

const store = useMovieStore();
const router = useRouter();
const openai = new OpenAI({apiKey: import.meta.env.VITE_OPENAI_API_KEY, dangerouslyAllowBrowser: true});
import.meta.env.VITE_TMDB_API_KEY

// 폼 데이터
const title = ref('');
const openYear = ref('');
const synopsis = ref('');
const plot = ref('');
const poster = ref(null);

// 에러 상태
const titleError = ref('');
const openYearError = ref('');
const synopsisError = ref('');
const plotError = ref('');
const posterError = ref('');

const isSubmitting = ref(false);

// 검색 관련 상태
const searchResults = ref([]);
const isGeneratingPlot = ref(false);


let searchTimeout = null;

const posterPreview = ref('');

// 영화 상세 정보를 저장할 ref 추가
const movieDetails = ref(null);
const movieCredits = ref(null);

const handleFileUpload = (event) => {
  const file = event.target.files[0];
  if (file) {
    poster.value = file;
    posterPreview.value = URL.createObjectURL(file);
  }
};

const validateForm = () => {
  titleError.value = title.value ? '' : '제목은 필수입니다.';
  openYearError.value = openYear.value ? '' : '개봉연도는 필수입니다.';
  synopsisError.value = synopsis.value ? '' : '시놉시스는 필수입니다.';
  plotError.value = plot.value ? '' : '줄거리는 필수입니다.';

  return !titleError.value && !openYearError.value && !synopsisError.value && !plotError.value;
};

const createMovie = async () => {
  if (!validateForm()) return;

  isSubmitting.value = true;

  try {
    const formData = new FormData();
    formData.append('title', title.value);
    formData.append('openYear', openYear.value);
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
          api_key: import.meta.env.VITE_TMDB_API_KEY
        }
      });
      
      searchResults.value = response.data.results;
    } catch (error) {
      store.showModalMessage('영화 검색에 실패했습니다.', error);
    }
  }, 500);
};

// 영화 선택 시 상세 정보를 함께 가져오도록 수정
const selectMovie = async (movie) => {
  title.value = movie.title;
  openYear.value = parseInt(movie.release_date.substring(0, 4));
  synopsis.value = movie.overview;
  
  // 추가 영화 정보 가져오기
  try {
    const [detailsRes, creditsRes] = await Promise.all([
      // 영화 상세 정보
      axios.get(`https://api.themoviedb.org/3/movie/${movie.id}`, {
        params: {
          api_key: import.meta.env.VITE_TMDB_API_KEY,
          language: 'en',
          append_to_response: 'videos,keywords'
        }
      }),
      // 출연진 및 제작진 정보
      axios.get(`https://api.themoviedb.org/3/movie/${movie.id}/credits`, {
        params: {
          api_key: import.meta.env.VITE_TMDB_API_KEY,
          language: 'en'
        }
      }),
    ]);

    movieDetails.value = detailsRes.data;
    movieCredits.value = creditsRes.data;

    // 데이터를 모두 가져온 후 프롬프트 생성
    const prompt = createMoviePrompt();
    console.log(prompt);
    generatePlot(prompt);

    // 포스터 처리
    if (movie.poster_path) {
      const imageUrl = `https://image.tmdb.org/t/p/original${movie.poster_path}`;
      posterPreview.value = imageUrl;
      
      const response = await fetch(imageUrl);
      const blob = await response.blob();
      const file = new File([blob], `${movie.title}_poster.jpg`, { type: 'image/jpeg' });
      poster.value = file;
    }
  } catch (error) {
    console.error(error);
    store.showModalMessage('영화 정보를 가져오는데 실패했습니다.', error);
  }

  searchResults.value = [];
};

// GPT에 전달할 프롬프트 생성 함수
const createMoviePrompt = () => {
  if (!movieDetails.value || !movieCredits.value) return '';

  const details = movieDetails.value;
  const credits = movieCredits.value;

  return `Movie Information:
Title: ${details.title}
Genre: ${details.genres.map(g => g.name).join(', ')}
Release Date: ${details.release_date}
Synopsis: ${details.overview}

Main Cast:
${credits.cast.slice(0, 5).map(actor => `- ${actor.character}: ${actor.name}`).join('\n')}

Production Team:
${credits.crew.filter(c => ['Director', 'Writer', 'Screenplay'].includes(c.job)).map(c => `- ${c.job}: ${c.name}`).join('\n')}

Keywords:
${details.keywords?.keywords?.map(k => k.name).join(', ')}

Please write a plot of the movie based on the above information, concisely.`;
};

// GPT API 호출 함수
const generatePlot = async () => {
  const prompt = createMoviePrompt();
  if (!prompt) {
    store.showModalMessage('영화 정보가 충분하지 않습니다.', '영화를 먼저 선택해주세요.');
    return;
  }

  isGeneratingPlot.value = true;
  try {
    plot.value = prompt;
    const completion = await openai.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [
        { role: "system", content: "You are a Movie Review Youtuber. You will going to explain the plot of the movie concisely. Synopsis, which is given, is just for reference. Give me the whole story of the movie including the ending. No need for any explanation." },
        {
            role: "user",
            content: prompt,
        },
        {
          role: "assistant",
          content: `The fate of Middle-earth hangs in the balance as the forces of good and evil prepare for a climactic battle. Frodo Baggins, accompanied by his steadfast friend Samwise Gamgee and the treacherous creature Gollum, continues their perilous quest to destroy the One Ring in the fires of Mount Doom, deep within the dark land of Mordor. 

Meanwhile, Aragorn, the rightful heir to the throne of men, grapples with his destiny as he rallies the kingdoms of Gondor and Rohan to unite against Sauron's overwhelming army of orcs and wraiths. He gains the support of the noble Éowyn and the brave Merry, who join in the fight despite the odds against them.

As armies clash in the epic Battle of Pelennor Fields, Gandalf leads the defense of Gondor against the forces of darkness, showcasing both valor and sorcery. The battle is brutal, filled with acts of courage and sacrifice. Key characters face pivotal moments—Aragorn embraces his role as king, while Frodo's journey grows increasingly treacherous as Gollum's personality begins to dominate, leading to tension amongst the group.

Ultimately, Frodo reaches Mount Doom but struggles with the Ring's corrupting power, almost succumbing to its allure. In a moment of chaos, Gollum attacks Frodo, biting off his finger to reclaim the Ring. In the struggle, Gollum falls into the lava, inadvertently destroying the Ring and Sauron's power along with it.

As the dark forces scatter, the surviving heroes celebrate their hard-won victory, but the toll of the journey is heavy. Aragorn is crowned King of Gondor, uniting the realms of men, while Frodo and Sam return to the Shire, changed by their experiences. However, Frodo is left with lasting scars and finds it hard to fully reintegrate into his previous life.

Frodo departing Middle-earth for the Undying Lands with Gandalf, Bilbo, and the Elves, seeking peace after the burdens he carried. Sam returns home, cherishing the memory of their journey, and starts a family, ensuring that hope and new beginnings take root in a world forever changed by their bravery.`
        }
    ],
    });
    plot.value = completion.choices[0].message.content;
  } catch (error) {
    store.showModalMessage('줄거리 생성에 실패했습니다.', error);
  } finally {
    isGeneratingPlot.value = false;
  }
};

// 컴포넌트가 언마운트될 때 타임아웃 정리
onUnmounted(() => {
  if (searchTimeout) clearTimeout(searchTimeout);
  if (posterPreview.value) {
    URL.revokeObjectURL(posterPreview.value);
  }
});
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