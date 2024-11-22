<template>
  <article v-if="profile">
    <div class="container p-1 flex">
      <div class="row col-3">
        <div class="profile card">
          <p>프로필사진</p>
          <img :src="store.BASE_URL + profile.profile_picture" alt="">
        </div>
        <div class="info card">
          <p>닉네임 : {{ profile.nickname }}</p>
          <p>가입날짜 : {{ profile.join_date }}</p>
        </div>
      </div>
      <div class="row col-9">
        <div class="card">
          <p>좋아요 개수 : </p>
          <p>작성 게시글 목록 : </p>
          <p>작성 댓글 목록 : </p>
          <p>코인 개수 : {{ profile.token }}</p>
        </div>
      </div>
    </div>
    <button @click="$router.go(-1)">이전으로</button>
    <RouterLink :to="{ name: 'ProfileChange', params: { userid: user_pk } }">
      <button>정보변경</button>
    </RouterLink>
  </article>
</template>

<script setup>
import { useMovieStore } from '@/stores/counter';
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { RouterLink, useRoute } from 'vue-router';

const route = useRoute()
const user_pk = route.params.userid
const store = useMovieStore()
const profile = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/accounts/${user_pk}/`
  })
    .then((response) => {
      profile.value = response.data
      console.log(profile.value)
    })
})
</script>

<style scoped>
    .container {
        display : flex;
        justify-content: space-between;
    }
</style>