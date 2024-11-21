<template>
  <div>
    <button @click="pushLikes" v-show="isLiked === false">좋아요</button>
      <button @click="pushLikes" v-show="isLiked === true">좋아요 취소</button>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/counter';
import axios from 'axios';
import { ref } from 'vue';

const store = useMovieStore()

const props = defineProps({
  pk: Number,
  nextUrl: String,
})
const isLiked = ref(false)

const pushLikes = function() {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/${props.nextUrl}/${props.pk}/likes/`,
    headers: {
        Authorization: `Token ${store.token}`,
      },
  })
    .then((response) => {
      isLiked.value = response.data.is_liked
    })

}

</script>

<style lang="scss" scoped>

</style>