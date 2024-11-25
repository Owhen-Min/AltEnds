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

<style>
@font-face {
  font-family: 'GmarketSansMedium';
  src: url('assets/fonts/GmarketSansMedium.otf') format('opentype');
}

@font-face {
  font-family: 'GmarketSansBold';
  src: url('assets/fonts/GmarketSansBold.otf') format('opentype');
}

@font-face {
  font-family: 'GmarketSansLight';
  src: url('assets/fonts/GmarketSansLight.otf') format('opentype');
}

* {
  font-family: 'GmarketSansMedium', sans-serif;
}

.container-fluid {
    background-color: #212529;
  }

body {
  background-color: #212529 !important;
  margin: 0;
  min-height: 100vh;
}

#app {
  min-height: 100vh;
  background-color: #212529;
}
</style>