<template>
  <h2 class="card-header">대체 결말 랭킹</h2>
  <div class="row justify-content-between">
    <div @click="goEndingDetail(altend.ending_id)" class="ranking-card col-12 col-md-6 col-lg-4 text-align-between row" v-for="(altend, index) in altEndRanking" :key="altend.ending_id">
      <h4 class="col-6">{{ index }}위</h4>
      <p class="col-6">좋아요 : {{ altend.like_count }}</p>
      <p class="col-12"> 원본 영화: {{ altend.movie }}</p>
      <p class="col-12">{{ altend.prompt }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useMovieStore } from '@/stores/counter';
import { useRouter } from 'vue-router';

const store = useMovieStore();
const router = useRouter();

const altEndRanking = ref([]);
const props = defineProps({
  altEndRanking: Array
})

const goEndingDetail = (endingid) => {
  router.push({ name: 'EndingListDetail', params: { endingid: endingid } })
}

onMounted(() => {
  altEndRanking.value = props.altEndRanking;
  axios({
    method: 'GET',
    url: `${store.API_URL}/movies/ranking/ending/`,
  })
  .then((res) => {
    altEndRanking.value = res.data;
  })
})
</script>

<style scoped>
.ranking-card {
  background-color: #e9ecef; /* Light background for ranking cards */
  padding: 5px;
  border-radius: 5px; /* Rounded corners */
  margin-right: 10px; /* Space between ranking cards */
  border: solid black 1px;
  cursor: pointer;
}

.card-header {
  background-color: #f8f9fa; /* Light background for header */
  font-weight: bold; /* Make header text bold */
}
</style>