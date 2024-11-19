<template>
  <div>
    <h1>커뮤니티 글 작성하기</h1>
    <form @submit.prevent="createArticle" method="post">
      <div>
        <label for="title">제목 : </label>
        <input type="text" id="title" v-model.trim="title">
      </div>
      <div>
        <label for="content">내용 : </label>
        <textarea id="content" v-model.trim="content"></textarea>
      </div>
      <button type="submit" class="btn btn-primary">글 작성하기</button>
    </form>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/counter';
import axios from 'axios';
import { ref } from 'vue'
import { useRouter } from 'vue-router';

const store = useMovieStore()
const title = ref('')
const content = ref('')
const router = useRouter()
const createArticle = function () {
  
  axios.defaults.withCredentials = true;
  
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/communities/articles/`,
    data: {
      title: title.value,
      content: content.value,
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
    
  }, { withCredentials: true })
  .then((res) => {
    router.push({name: 'CommunityDetail', params:{articleid:res.data.id}})
    
  })
  .catch((error) => {
    console.log(error)
})
}
</script>

<style lang="scss" scoped>

</style>