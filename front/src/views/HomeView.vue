<template>

    <div class="container p-1 flex">
        <div class="row col-9">
          <div class="card">
            <h2>이번주의 영화</h2>
            <div v-for="movie in movies" class="card">
                {{movie}}
            </div>
          </div>
          <div class="ranking card">
            <h2>랭킹입니다.</h2>
          </div>
        </div>
        <div class="row col-3">
        <div class="card">
            <div class="card">로그인 페이지</div>
            <div class="card">사용자 랭킹</div>
        </div>
    </div>
    </div>
</template>

<script setup>
    const movies = ['리얼', '성냥팔이 소녀의 재림', '클레멘타인', '웃겨야 사는 영화']
</script>

<style scoped>
    .container {
        display : flex;
        justify-content: space-between;
    }
</style>