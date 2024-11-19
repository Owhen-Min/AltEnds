<template>
  <article>
    <div class="container p-1 flex">
      <div class="row col-3">
        <div class="profile card">
          <p>프로필사진</p>
        </div>
        <div class="info card">
          <p>닉네임</p>
          <p>가입날짜</p>
        </div>
      </div>
      <div class="row col-9">
        <div class="card">
          <p>좋아요 개수 : </p>
          <p>작성 게시글 목록 : </p>
          <p>작성 댓글 목록 : </p>
          <p>코인 개수 : </p>
        </div>
      </div>
    </div>
    <button @click="$router.go(-1)">이전으로</button>
    <button>정보변경</button>
  </article>
</template>

<script setup>
import { useMovieStore } from '@/stores/counter';
import { ref } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute()
const user_pk = route.params.pk
const store = useMovieStore()
</script>

<style scoped>
    .container {
        display : flex;
        justify-content: space-between;
    }
</style>