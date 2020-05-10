<template>
  <b-container>
    <el-container class="page-container">
      <el-header>
        <AppNavigation />
      </el-header>
      <el-main>
        <nuxt />
      </el-main>
      <el-footer>Footer</el-footer>
    </el-container>
  </b-container>
</template>

<script>
// import { BContainer } from 'bootstrap-vue'
import AppNavigation from '@/components/front/header/AppNavigation'
export default {
  components: {
    AppNavigation
  }
}
</script>

<style lang="sass" scoped></style>
