<template>
  <div class="hero-image">
    <div class="container">
      <div class="title text-center">
        <h1>Вся коммерческая недвижимость на brokernsk.pro</h1>
      </div>
      <app-main-search-panel />
    </div>
  </div>
</template>

<script>
import AppMainSearchPanel from './MainSearchPanel'
export default {
  name: 'MainView',
  components: {
    AppMainSearchPanel
  }
}
</script>

<style lang="scss" scoped>
.hero-image {
  position: relative;
  /*height: 100vh;*/
  /*min-height: 700px;*/
  height: 600px;
  max-height: 600px;
  background: linear-gradient(rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.2)),
    url('/media/main_bg.jpg');
  background-position: center center;
  background-repeat: no-repeat;
  background-size: cover;
  color: #fff;
}
.title {
  font-size: 48px;
  line-height: 58px;
  font-weight: 500;
  color: #fff;
  position: relative;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1;
  height: 220px;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  text-align: center;
  margin-bottom: 36px;
}
.title h1 {
  font-size: 48px;
  line-height: 47px;
}
</style>
