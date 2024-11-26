<template>
  <div class="button-container">
    <button 
      @click="pushLikes" 
      :class="['like-button', isLiked ? 'liked' : '']"
    >
      {{ isLiked ? '안 좋아요' : '좋아요' }}
    </button>
    <button 
      @click="pushDislikes" 
      :class="['dislike-button', isDisliked ? 'disliked' : '']"
      v-if="nextUrl === 'movies/altends'"
    >
      {{ isDisliked ? '안 짜쳐요' : '짜쳐요' }}
    </button>
  </div>
</template>


<script setup>
import { useMovieStore } from '@/stores/movieStore';
import axios from 'axios';
import { ref, watch } from 'vue';

const store = useMovieStore()
const props = defineProps({
  pk: Number,
  nextUrl: String,
  isLiked: Boolean,
  isDisliked: Boolean,
})

const isLiked = ref(false)
const isDisliked = ref(false)
const nextUrl = ref(false)

watch(() => props.isLiked, (newValue) => {
  isLiked.value = newValue
  isDisliked.value = newValue
  nextUrl.value = props.nextUrl
}, { immediate: true })


const pushLikes = function() {
  axios({
    method: 'post',
    url: `${store.API_URL}/${props.nextUrl}/${props.pk}/likes/`,
    headers: {
        Authorization: `Token ${store.token}`,
      },
  })
    .then((response) => {
      isLiked.value = response.data.is_liked
      isDisliked.value = response.data.is_disliked
    })

}

const pushDislikes = function() {
  axios({
    method: 'post',
    url: `${store.API_URL}/${props.nextUrl}/${props.pk}/dislikes/`,
    headers: {
        Authorization: `Token ${store.token}`,
      },
  })
    .then((response) => {
      isDisliked.value = response.data.is_disliked
      isLiked.value = response.data.is_liked
    })
}

</script>

<style scoped>
.button-container {
  margin: 10px 0;
  display: flex;
  gap: 10px;
}

.like-button {
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  border: none;
  border-radius: 20px;
  padding: 8px 16px;
  color: white;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.like-button:hover {
  transform: scale(1.05);
}

.like-button.liked {
  background: rgba(255, 255, 255, 0.1);
}

.dislike-button {
  background: linear-gradient(45deg, #6b6bff, #8cb8ff);
  border: none;
  border-radius: 20px;
  padding: 8px 16px;
  color: white;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.dislike-button:hover {
  transform: scale(1.05);
}

.dislike-button.disliked {
  background: rgba(255, 255, 255, 0.1);
}
</style>