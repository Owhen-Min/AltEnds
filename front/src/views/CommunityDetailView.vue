  <div class="container card py-5" v-if="article">
      <p>{{ article.id }} 번째 게시글</p>
      <p>작성 시간 : {{ article.created_at }}</p>
      <p>제목 : {{ article.title }}</p>
      <p>내용 : {{ article.content }}</p>

      <RouterLink :to="{ name: 'Community' }" class="col-3 mx-2">
          <button class="btn btn-warning col-12">이전으로</button>
      </RouterLink>
      <br>
      
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/counter';
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
const route = useRoute()
const article = ref(null)
const store = useMovieStore()

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/communities/articles/${route.params.articleid}/`
  })
    .then((res) => {
      article.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
})
</script>

<style scoped>
</style>