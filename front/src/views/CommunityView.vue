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
        <p class="font-weight-bold">{{ post.view }}</p>
      </div>
      <div class="d-flex col-1 justify-content-center">
        <p class="font-weight-bold">{{ post.likes }}</p>
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
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { RouterLink } from 'vue-router';

const router = useRouter()

const posts = [{
  id: 1,
  title: '사실 윤상흠은 개쩌는 천재였고 컴퓨터의 억까로 인해서 슬퍼지게 된 사람이다!',
  content: '내용1',
  author: 'user1',
  view: 20,
  likes: 0
},
{
  id: 2,
  title: '아무말이나 열심히 해서 제목을 열심히 늘려보면 좀 글이 이뻐지지 않을까',
  content: '내용2',
  author: 'user2',
  view: 30,
  likes: 10
},
{
  id: 3,
  title: 'ㅇ',
  content: '내용3',
  author: 'user3',
  view: 50,
  likes: 20
}
]

const goDetail = ((index) => {
  router.push({ name: 'CommunityDetail', params: { articleid: index }})
})

</script>

<style scoped>
.container {
    display : flex;
    justify-content: space-between;
}
</style>