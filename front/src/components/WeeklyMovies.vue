<template>
  <div class="movie-section">
    <h2 class="card-header">주간 영화 목록</h2>
    <div class="slick-carousel"
      @mousedown="handleMouseDown($event)"
      @mousemove="handleMouseMove"
      @click="handleClick($event)">
      <div v-for="movie in weeklyMovies" :key="movie.id" class="movie-item" :data-movieid="movie.id">
        <img
          draggable="false"
          :src="store.BASE_URL + movie.poster"
          :alt="`${movie.title}의 포스터`"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { useMovieStore } from "@/stores/counter";
import { onMounted, nextTick } from "vue";
import { useRouter } from 'vue-router';
import $ from 'jquery';
import 'slick-carousel';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';

const store = useMovieStore();
const router = useRouter();
const weeklyMovies = store.weeklyMovie;

let isDragging = false;
let startX = 0;

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
  router.push({ name: 'MovieListDetail', params: { movieid: movieid }})
})

onMounted(() => {
  store.getMovies();
  nextTick(() => {
    $('.slick-carousel').slick({
      centerMode: true,
      centerPadding: '60px',
      autoplay: true,
      autoplaySpeed: 2000,
      slidesToShow: 4,
      dots: true,
      infinite: true,
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
  });
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
  color: #fff;
  font-size: 2rem;
  font-weight: 700;
  text-align: center;
  padding: 1.5rem;
  margin-bottom: 2rem;
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  border-radius: 12px;
  text-transform: uppercase;
  letter-spacing: 2px;
  box-shadow: 0 4px 15px rgba(255, 107, 107, 0.2);
}

.movie-card {
  position: relative;
  overflow: hidden;
  border-radius: 12px;
  transition: transform 0.3s ease;
}

.movie-card:hover {
  transform: translateY(-10px);
}

.movie-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
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

img {
  width: 100%;
  height: auto;
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
</style>