<template>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <div class="container">
    <NavBar />
    <RouterView />
    <Modal
      v-model:isVisible="store.showModal"
      :title="store.errorTitle"
      :message="store.errorMessage"
    />
  </div>
</template>
<script setup>
import { RouterView } from 'vue-router';
import NavBar from './components/NavBar.vue';
import Modal from './components/Modal.vue';
import { useMovieStore } from './stores/counter';

const store = useMovieStore();
</script>

<style scoped>

</style>