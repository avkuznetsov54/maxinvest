<template>
  <div class="hero-image"></div>
</template>

<script>
export default {
  name: 'MainView'
}
</script>

<style lang="scss" scoped>
.hero-image {
  position: relative;
  /*height: 100vh;*/
  /*min-height: 700px;*/
  height: 500px;
  max-height: 600px;
  background: linear-gradient(rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.2)),
    url('https://www.restate.ru/attachment/ee9f94fab094a9f3b0dea7d647626f9e992b10f9/proportional/1920x760/sk6.jpg');
  background-position: center center;
  background-repeat: no-repeat;
  background-size: cover;
}
</style>
