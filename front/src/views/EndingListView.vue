<template>
  <div>
    <div 
      class="container p-1 flex"
      v-for="(ending, index) in endings"
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
        <p>원본영화 제목: {{ ending.title }}</p>
        <p>대체결말 제목: {{ ending.altEndTitle }}</p>
        <p>입력 파라미터: {{ ending.params }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import router from '@/router';
import { ref } from 'vue';

const endings = ref([
  { title: '리얼', altEndTitle: '리얼 개웃김', params: '개그코드를 넣어줘' },
  { title: '성냥팔이 소녀의 재림', altEndTitle: '성냥팔이 소녀의 재림 실화냐?', params: '개그코드를 넣어줘' },
  { title: '클레멘타인', altEndTitle: '클레멘타인의 모험', params: '개그코드를 넣어줘' },
  { title: '웃겨야 사는 영화', altEndTitle: '웃겨야 사는 영화인데 안웃김', params: '개그코드를 넣어줘' },
  { title: '영화 5', altEndTitle: '성냥팔이 소녀의 재림 실화냐?', params: '개그코드를 넣어줘' },
  { title: '영화 6', altEndTitle: '성냥팔이 소녀의 재림 실화냐?', params: '개그코드를 넣어줘' },
])

const goDetail = ((index) => {
  router.push({ name: 'EndingListDetail', params: { endingid: index }})
})

</script>

<style scoped>
.container {
    display : flex;
    justify-content: space-between;
}
</style>