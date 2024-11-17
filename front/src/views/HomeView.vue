<template>

    <div class="container p-1 flex">
        <div class="row col-9">
          <div class="card">
            <h2>이번주의 영화</h2>
            <div v-for="(movie, index) in movies" :key="index" class="card">
                {{movie}}
            </div>
          </div>
          <div class="ranking card">
            <h2>랭킹입니다.</h2>
          </div>
        </div>
        <div class="col-3">
            <div class="card">
            <div class="card" id="user-management" v-if=isLoggedIn>
                <p>회원 정보를 간단하게 보여줍니다.</p>
            </div>
            <div class="card" id="user-login" v-else>
                <RouterLink :to="{name:'login'}">로그인</RouterLink>
                <RouterLink :to="{name: 'signup'}">회원가입</RouterLink> 
            </div>
            <div class="card">
                사용자 랭킹
            </div>
        </div>
    </div>
    </div>
</template>

<script setup>
    const movies = ['리얼', '성냥팔이 소녀의 재림', '클레멘타인', '웃겨야 사는 영화'];
    const isLoggedIn = false; // 실제 로그인 기능을 구현할 경우 대체될 placeholder
</script>

<style scoped>
    .container {
        display : flex;
        justify-content: space-between;
    }
</style>