<template>
  <div class="container-fluid">
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
.container-fluid {
  background-color: #212529;
}
</style>