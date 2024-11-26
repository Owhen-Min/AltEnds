<template>
  <div class="movie-section">
    <h2 class="card-header">
      <span class="header-text">이번 주 영화</span>
    </h2>
    <div class="slick-carousel"
      @mousedown="handleMouseDown($event)"
      @mousemove="handleMouseMove"
      @click="handleClick($event)">
      <div v-for="movie in weeklyMovies" :key="movie.id" class="movie-item" :data-movieid="movie.id">
        <div class="movie-card">
          <img
            draggable="false"
            :src="store.BASE_URL + movie.poster"
            :alt="`${movie.title}의 포스터`"
          />
          <div class="movie-overlay">
            <span class="view-details">상세보기</span>
          </div>
        </div>
      </div>
    </div>
  </div>
  <MovieDetailModal 
    v-if="showModal" 
    :movieid="selectedMovie"
    @close="showModal = false"
  />
</template>

<script setup>
import { useMovieStore } from "@/stores/movieStore";
import { onMounted, nextTick, ref, watch } from "vue";
import $ from 'jquery';
import MovieDetailModal from '@/components/MovieDetailModal.vue';

import 'slick-carousel';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';

const store = useMovieStore();
const weeklyMovies = ref([]);
const selectedMovie = ref(null);
let isDragging = false;
let startX = 0;

// 모달 표시 여부를 제어하는 상태 추가
const showModal = ref(false);

const handleMouseDown = (event) => {
  isDragging = false;
  startX = event.clientX;
};

const handleMouseMove = () => {
  isDragging = true;
};

const handleClick = (event) => {
  const moveX = Math.abs(event.clientX - startX);
  if (!isDragging || moveX < 5) {
    const movieItem = event.target.closest('.movie-item');
    const movieid = movieItem.dataset.movieid;
    goDetail(movieid);
  }
};

const goDetail = ((movieid) => {
  selectedMovie.value = movieid;
  showModal.value = true;  // 모달 표시
})

// Slick carousel을 초기화하는 함수
const initializeSlick = () => {
  nextTick(() => {
    if ($('.slick-carousel').hasClass('slick-initialized')) {
      $('.slick-carousel').slick('unslick');
    }
    
    // jQuery의 이벤트 핸들러에 passive 옵션 추가
    $.event.special.touchstart = {
      setup: function(_, ns, handle) {
        if (ns.includes('noPreventDefault')) {
          this.addEventListener('touchstart', handle, { passive: true });
        } else {
          this.addEventListener('touchstart', handle, { passive: false });
        }
      }
    };
    
    $.event.special.touchmove = {
      setup: function(_, ns, handle) {
        if (ns.includes('noPreventDefault')) {
          this.addEventListener('touchmove', handle, { passive: true });
        } else {
          this.addEventListener('touchmove', handle, { passive: false });
        }
      }
    };

    if (weeklyMovies.value && weeklyMovies.value.length > 0) {
      $('.slick-carousel').slick({
        centerMode: true,
        centerPadding: '60px',
        autoplay: true,
        autoplaySpeed: 2000,
        slidesToShow: 4,
        dots: true,
        infinite: true,
        touchThreshold: 10,  // 터치 감도 조정
        swipeToSlide: true,  // 스와이프로 슬라이드 이동 활성화
        responsive: [
          {
            breakpoint: 768,
            settings: {
              arrows: false,
              centerMode: true,
              centerPadding: '40px',
              slidesToShow: 3
            }
          },
          {
            breakpoint: 480,
            settings: {
              arrows: false,
              centerMode: true,
              centerPadding: '40px',
              slidesToShow: 2
            }
          }
        ]
      });
    }
  });
};

// store의 weeklyMovie 변경 감시
watch(
  () => store.weeklyMovie,
  (newMovies) => {
    weeklyMovies.value = newMovies;
    initializeSlick();
  },
  { deep: true, immediate: true }
);

onMounted(async () => {
  await store.getMovies();
  initializeSlick();
});

</script>

<style scoped>
.movie-section {
  background: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 100%);
  padding: 2rem;
  border-radius: 15px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

.card-header {
  position: relative;
  text-align: center;
  padding: 1rem;
  margin-bottom: 2rem;
  background: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 100%);
  border-radius: 15px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}

.header-text {
  font-size: 2.5rem;
  font-weight: 700;
  color: #ffffff;
  letter-spacing: 2px;
}

@media (max-width: 768px) {
  .header-text {
    font-size: 2rem;
  }
}

.movie-card {
  position: relative;
  overflow: hidden;
  border-radius: 12px;
  transition: transform 0.3s ease;
  aspect-ratio: 2/3;
  width: 100%;
  margin: 0 auto;
}

.movie-card:hover {
  transform: translateY(-10px);
}

.movie-card:hover .movie-overlay {
  opacity: 1;
}

.view-details {
  color: white;
  font-size: 1.2rem;
  font-weight: bold;
  padding: 10px 20px;
  border: 2px solid white;
  border-radius: 25px;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(5px);
  transition: all 0.3s ease;
}

.view-details:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: scale(1.1);
}

img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 12px;
  transition: transform 0.3s ease;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

/* Slick carousel 커스텀 스타일 */
:deep(.slick-dots) {
  bottom: -35px;
}

:deep(.slick-dots li button:before) {
  color: #fff;
  font-size: 12px;
  opacity: 0.5;
}

:deep(.slick-dots li.slick-active button:before) {
  color: #ff6b6b;
  opacity: 1;
}

:deep(.slick-prev),
:deep(.slick-next) {
  width: 40px;
  height: 40px;
  z-index: 1;
}

:deep(.slick-prev:before),
:deep(.slick-next:before) {
  font-size: 40px;
  color: #ff6b6b;
  opacity: 0.8;
}

@media (max-width: 767px) {
  .movie-section {
    padding: 1rem;
  }
  
  .card-header {
    font-size: 1.5rem;
    padding: 1rem;
  }
}

.movie-item .movie-card {
  position: relative;
  overflow: hidden;
  cursor: pointer;
}

.movie-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.movie-card:hover .movie-overlay {
  opacity: 1;
}

.view-details {
  color: white;
  font-size: 1.2rem;
  font-weight: bold;
  padding: 10px 20px;
  border: 2px solid white;
  border-radius: 25px;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(5px);
  transition: all 0.3s ease;
}

.view-details:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: scale(1.1);
}
</style>