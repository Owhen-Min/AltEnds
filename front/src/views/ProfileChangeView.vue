<template>
  <div class="container-fluid bg-dark py-5">
    <div class="container">
      <div class="content-card">
        <h3 class="gradient-text mb-4">프로필 정보 변경</h3>
        <form @submit.prevent="profileChange" class="profile-form">
          <div class="form-group">
            <label class="form-label" for="nickname">닉네임</label>
            <input 
              type="text" 
              id="nickname" 
              v-model.trim="nickname"
              class="form-control"
              placeholder="변경할 닉네임을 입력하세요"
            >
          </div>

          <div class="form-group">
            <label class="form-label" for="picture">프로필 사진</label>
            <input 
              type="file" 
              id="picture" 
              ref="picture" 
              accept="image/png, image/jpeg"
              class="form-control"
            />
          </div>

          <div class="button-group">
            <button 
              type="button" 
              @click="$router.go(-1)" 
              class="btn btn-warning"
            >
              취소
            </button>
            <button 
              type="submit" 
              class="btn btn-primary"
            >
              변경하기
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movieStore';
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
  const formData = new FormData()
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

<style scoped>
.container-fluid {
  margin-top: 100px;
  min-height: 100vh;
}

.content-card {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  border-radius: 12px;
  padding: 2rem;
  color: white;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
  max-width: 600px;
  margin: 0 auto;
}

.gradient-text {
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 700;
  text-align: center;
}

.profile-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form-label {
  color: rgba(255, 255, 255, 0.8);
  font-size: 1rem;
}

.form-control {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 6px;
  padding: 0.8rem;
  color: white;
  transition: all 0.3s ease;
}

.form-control:focus {
  outline: none;
  border-color: #ffb88c;
  background: rgba(255, 255, 255, 0.15);
}

.form-control::file-selector-button {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  margin-right: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.form-control::file-selector-button:hover {
  background: rgba(255, 255, 255, 0.2);
}

.button-group {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin-top: 1rem;
}

.btn {
  padding: 0.8rem 2rem;
  transition: all 0.3s ease;
  font-size: 1rem;
}

.btn:hover {
  transform: scale(1.05);
}

.btn-primary {
  background: linear-gradient(45deg, #ff6b6b, #ffb88c);
  border: none;
  color: white;
}

.btn-warning {
  background: rgba(255, 255, 255, 0.1);
  border: 2px solid #ffb88c;
  color: white;
}

@media (max-width: 768px) {
  .content-card {
    padding: 1.5rem;
    margin: 0 1rem;
  }

  .btn {
    padding: 0.6rem 1.5rem;
  }
}
</style>