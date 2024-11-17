<template>
    <div class="container">
        <div class="row gx-5 justify-content-evenly">
            <div class="col-3">
                <img src="https://m.media-amazon.com/images/I/81EBp0vOZZL.jpg" alt="Movie Poster" class="movie-poster">
                <hr>
                <h1>{movie.title}</h1>
                <h4>감독 : {movie.director}</h4>
                <h4>개봉연도 : {movie.openYear}</h4>
                <h4>장르 : {movie.genre}</h4>
            </div>
            <div class="col-7">
                
                <h3>영화 줄거리</h3>
                <h4>At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.
                </h4>
            </div>
            <p></p>
            <button class="btn btn-warning col-4">이전으로</button> <button class="btn btn-primary col-4">대체 결말 생성하기</button>
        </div>
    </div>

</template>

<script setup>

</script>

<style scoped>
.container {
        justify-content: start;
        text-align: start;
    }

.movie-poster {
  max-width: 100%; /* Ensure the image fits within the card */
  height: auto; /* Maintain aspect ratio of the image */
}
</style>