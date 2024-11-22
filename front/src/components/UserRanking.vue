<template>
  <div class="card mb-4 p-3">
    <h5>사용자 랭킹</h5>
    <div @click="goProfile(user.user_id)" v-for="(user, index) in userRanking" :key="user.username" class="card mb-2 p-2">
      <p>{{ index }}위: {{ user.user_name }}</p>
      <p>좋아요 수: {{ user.total_likes }}</p>
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

const userRanking = ref([]);
const props = defineProps({
  userRanking: Array
})

const goProfile = (userid) => {
  router.push({ name: 'Profile', params: { userid: userid } })
}

onMounted(() => {
  userRanking.value = props.userRanking;
  axios({
    method: 'GET',
    url: `${store.API_URL}/movies/ranking/user/`,
  })
  .then((res) => {
    console.log(res);
    userRanking.value = res.data;
  })
})
</script>

<style scoped>

</style>