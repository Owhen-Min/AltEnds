<template>
    <div class="container flex flex-wrap py-2 my-3">
      <div class="col-12">
        <h3>이번 주 영화 정보</h3>
      </div>
      <div class="card row col-4 align-items-center justify-content-center" v-for="movie in movies">
        <img src="https://static.wikia.nocookie.net/jaws/images/d/da/Jaws-movie-poster.jpg/revision/latest/scale-to-width-down/1545?cb=20131015071208" alt="까꿍">
        <h4> 영화 제목</h4>
      </div>
    </div>
</template>

<script setup>
    const movies = 6
</script>

<style scoped>
    .container {
        display : flex;
        justify-content: space-between;
        text-align: center;
    }
</style>