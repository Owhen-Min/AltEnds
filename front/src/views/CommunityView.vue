<template>
  <div>
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h2 class> 커뮤니티 게시판 </h2>
      <RouterLink :to="{name:'CommunityCreate'}" class="d-flex col-2 justify-content-center btn btn-dark">글 작성하기</RouterLink>
    </div>
    <div class="container justify-content-center p-1 flex">
      <div class="d-flex col-1 justify-content-center"></div>
      <div class="d-flex col-7 justify-content-center">
        <p class="font-weight-bold">제목</p>
      </div>
      <div class="d-flex col-2 justify-content-center">
        <p class="font-weight-bold">작성자</p>
      </div>
      <div class="d-flex col-1 justify-content-center">
        <p class="font-weight-bold">조회수</p>
      </div>
      <div class="d-flex col-1 justify-content-center">
        <p class="font-weight-bold">좋아요 수</p>
      </div>
    </div>
    <div class="container p-1 flex" v-for="post in posts" :key="post.id" @click="goDetail(post.id)">
      <div class="d-flex col-1 justify-content-center">{{ post.id }}</div>
      <div class="d-flex col-7 justify-content-start">
        <p class="font-weight-bold">{{ post.title }}</p>
      </div>
      <div class="d-flex col-2 justify-content-center">
        <p class="font-weight-bold">{{ post.author }}</p>
      </div>
      <div class="d-flex col-1 justify-content-center">
        <p class="font-weight-bold"> 200 </p>
      </div>
      <div class="d-flex col-1 justify-content-center">
        <p class="font-weight-bold"> 500 </p>
      </div>
    </div>
    <div class="d-flex justify-content-end">
      <RouterLink :to="{name:'CommunityCreate'}" class="d-flex col-2 justify-content-center btn btn-dark">글 작성하기</RouterLink>
    </div>
    <div class="container d-flex justify-content-between">
        <RouterLink to="/" class="btn btn-light">이전 페이지로</RouterLink>
        <RouterLink to="/" class="btn btn-light">다음 페이지로</RouterLink>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter, RouterLink } from 'vue-router';
import { useMovieStore } from '@/stores/counter';
import axios from 'axios'

const router = useRouter()
const posts = ref([])
const store = useMovieStore()

const goDetail = ((index) => {
  router.push({ name: 'CommunityDetail', params: { articleid: index }})
})
    console.log(`${store.API_URL}/communities/articles/`)

onMounted(() => {
  axios ({
    method:'get',
    url: `${store.API_URL}/api/v1/communities/articles/`,
    headers: {
      Authorization : `Token ${store.token}`
    }
  })
  .then ((res) => {
    posts.value = res.data
  })
  .catch ((err) => {
    console.log(err)
  })
})


</script>

<style scoped>
.container {
    display : flex;
    justify-content: space-between;
}
</style>