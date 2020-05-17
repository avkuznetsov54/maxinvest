<template>
  <div class="hero-image">
    <div class="container">
      <div class="title text-center">
        <h1>Все коммерческие помещени на brokernsk.pro</h1>
      </div>
    </div>
  </div>
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
    url('/media/main_bg.jpg');
  background-position: center center;
  background-repeat: no-repeat;
  background-size: cover;
  color: #fff;
}
.title h1 {
  font-size: 36px;
  line-height: 47px;
}
</style>
