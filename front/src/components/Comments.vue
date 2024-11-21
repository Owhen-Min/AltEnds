<template>
  <h1>comment</h1>
  <div>
    <ul
      v-for="comment in comments"
      :key="comment.id"
    >
      <li>
        <p>작성자 : {{ comment.user_nickname }}</p>
        <p>내용 : {{ comment.content }}</p>
      </li>
    </ul>
    <form @submit.prevent="createComment">
      <label for="content">댓글 내용</label>
      <textarea name="" id="content" v-model="content"></textarea>
      <input type="submit" value="댓글 생성하기">
    </form>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/counter';
import axios from 'axios';
import { onMounted, ref } from 'vue';

const store = useMovieStore()

const content = ref(null)
const comments = ref(null)
const props = defineProps({
  pk: Number,
  nextUrl: String,
})

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/${props.nextUrl}/${props.pk}/comments/`,
  })
    .then((response) => {
      comments.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
})

const createComment = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/${props.nextUrl}/${props.pk}/comments/`,
    data: {
      content: content.value
    },
    headers: {
        Authorization: `Token ${store.token}`,
      },
  })
    .then((response) => {
      axios({
        method: 'get',
        url: `${store.API_URL}/${props.nextUrl}/${props.pk}/comments/`,
      })
        .then((response) => {
          comments.value = response.data
        })
        .catch((error) => {
          console.log(error)
        })
      })
    .then(() => {
      content.value = null
    })
      .catch((error) => {
        console.log(error)
      })
}
</script>

<style lang="scss" scoped>

</style>