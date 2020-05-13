<template>
  <div class="top-line">
    <div class="container">
      <Row>
        <i-col :xs="24" :sm="16" :md="16" :lg="12">
          <h1><nuxt-link to="/">Brokernsk.pro</nuxt-link></h1>
        </i-col>
        <i-col :xs="24" :sm="8" :md="8" :lg="{ span: 4, offset: 8 }">
          <Button type="error"><b>ОСТАВИТЬ ЗАЯВКУ</b></Button>
        </i-col>
      </Row>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TopLine'
}
</script>

<style lang="sass" scoped>
.top-line
  display: flex
  justify-content: space-between
  align-items: center
  height: 50px
  border-bottom: 1px solid #e6e6e6
</style>
