<template>
  <div>
    <app-main-view />
    <app-main-page-content />
  </div>
</template>

<script>
import AppMainView from '@/components/front/content/main-page/MainView'
import AppMainPageContent from '@/components/front/content/main-page/MainPageContent'
export default {
  components: {
    AppMainView,
    AppMainPageContent
  }
}
</script>

<style lang="sass" scoped>
.iit
  margin: 0 8px
  height: 50px
  background-color: #47494e
</style>
