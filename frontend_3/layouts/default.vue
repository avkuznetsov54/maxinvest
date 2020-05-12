<template>
  <div>
    <header>
      <app-top-line />
      <app-nav-bar />
    </header>

    <div>
      <nuxt />
    </div>
  </div>
</template>

<script>
import AppTopLine from '@/components/front/header/TopLine'
import AppNavBar from '@/components/front/header/NavBar'
export default {
  components: {
    AppTopLine,
    AppNavBar
  }
}
</script>

<style></style>
