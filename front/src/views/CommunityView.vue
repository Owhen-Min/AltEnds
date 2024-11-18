<template>
  <div>
    <div 
      class="container p-1 flex"
      v-for="(post, index) in posts"
      :key="index"
      @click="goDetail(index+1)"
    >
      <div class="card row col-3">
        <img 
          src="https://m.media-amazon.com/images/I/81EBp0vOZZL.jpg"
          alt="포스터"
          class="movie-poster"
        >
      </div>
      <div class="card row col-9">
        <p>게시글 제목: {{ post.title }}</p>
        <p>게시글 내용: {{ post.description }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter()

const posts = ref([
  { title: '리얼 개웃김', description: 'A gripping thriller about reality.' },
  { title: '성냥팔이 소녀의 재림 실화냐?', description: 'A touching story about hope.' },
  { title: '클레멘타인의 모험', description: 'A drama about love and loss.' },
  { title: '웃겨야 사는 영화인데 안웃김', description: 'A hilarious comedy that will make you laugh.' },
  { title: '영화 5', description: 'Description for movie 5.' },
  { title: '영화 6', description: 'Description for movie 6.' }
])

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