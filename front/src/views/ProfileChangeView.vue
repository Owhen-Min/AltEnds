<template>
  <div>
    회원정보 변경
    <form @submit.prevent="profileChange">
      <label for="nickname">변경할 닉네임을 작성하세요</label>
      <input type="text" id="nickname" v-model.trim="nickname"><br>

      <label for="picture">프로필사진을 선택하세요</label>
      <input type="file" id="picture" ref="picture" accept="image/png, image/jpeg" />

      <input type="submit" value="정보변경하기">

    </form>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/counter';
import axios from 'axios';
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const router = useRouter()
const route = useRoute()
const user_pk = route.params.userid
const store = useMovieStore()
const nickname = ref('')
const picture = ref(null)
const profileChange = function () {
  const formData = new FormData
  // 닉네임 추가
  if (!nickname.value && !picture.value?.files?.length) {
    store.showModalMessage('둘 중에 하나는 입력해주세요')
  }

  if (nickname.value) {
    formData.append('nickname', nickname.value) // nickname의 실제 값 추가
  }
  
  if (picture.value?.files?.length) {
    const file = picture.value.files[0];
    formData.append('profile_picture', file) // 파일 추가
  }
  
  axios({
    method: 'put',
    url: `${store.API_URL}/accounts/${user_pk}/`,
    data: formData,
    headers: {
      Authorization: `Token ${store.token}`,
      'Content-Type': 'multipart/form-data',
    },
  })
    .then((response) => {
      router.push({ name: 'Profile', params: { userid: user_pk } })
    })
    .catch((error) => {
      store.showModalMessage('회원정보 변경에 실패했습니다.', error)
    })
  }
</script>

<style lang="scss" scoped>

</style>