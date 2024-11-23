<template>
  <div class="like-button-container">
    <button 
      @click="pushLikes" 
      :class="['like-button', isLiked ? 'liked' : '']"
    >
      {{ isLiked ? '좋아요 취소' : '좋아요' }}
    </button>
  </div>
</template>


<script setup>
import { useMovieStore } from '@/stores/counter';
import axios from 'axios';
import { ref, defineProps, watch } from 'vue';

const store = useMovieStore()
const props = defineProps({
  pk: Number,
  nextUrl: String,
  isLiked: Boolean,
})

const isLiked = ref(false)

watch(() => props.isLiked, (newValue) => {
  isLiked.value = newValue
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
    })

}

</script>

<style scoped>
.like-button-container {
  margin: 10px 0;
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
  border: 2px solid #ffb88c;
}
</style>