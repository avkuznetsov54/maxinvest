<template>
  <b-container>
    <el-container class="page-container">
      <el-header height="100px">
        <app-top-line />
        <app-nav-menu />
      </el-header>
      <el-main>
        <nuxt />
      </el-main>
      <el-footer>Footer</el-footer>
    </el-container>
  </b-container>
</template>

<script>
import AppTopLine from '@/components/front/header/TopLine'
import AppNavMenu from '@/components/front/header/NavMenu'
export default {
  components: {
    AppTopLine,
    AppNavMenu
  }
}
</script>

<style lang="sass" scoped></style>
