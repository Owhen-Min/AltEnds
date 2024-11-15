<template>
    <div>
        <h1>이번주의 영화</h1>
            <div v-for="movie in movies">
                {{movie}}
            </div>
    </div>
</template>

<script setup>
    const movies = ['리얼', '성냥팔이 소녀의 재림', '클레멘타인', '웃겨야 사는 영화']
</script>

<style scoped>

</style>