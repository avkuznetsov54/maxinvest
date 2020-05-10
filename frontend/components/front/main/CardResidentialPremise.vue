<template>
  <el-card
    shadow="hover"
    :body-style="{ padding: 0 }"
    class="card-obj"
    @click.native="openCard"
  >
    <img
      src="https://cnet4.cbsistatic.com/img/oHmp-E6nkkEO7rCGZUqA6f5vbAk=/1092x0/2019/05/15/6b4688f3-f779-4b21-9b9e-1e27a04d637c/omaha-steaks.jpg"
      alt="hamburger"
      class="image"
    />
    <div style="padding: 14px;">
      <span>Yummy hamburger</span>
      <div class="bottom clearfix">
        <time class="time">{{ currentDate }}</time>
      </div>
    </div>
    <div style="padding: 14px;">
      <el-button type="primary" plain size="small">Узнать подробнее</el-button>
    </div>
  </el-card>
</template>

<script>
export default {
  name: 'CardResidentialPremise',
  data() {
    return {
      currentDate: new Date()
    }
  },
  methods: {
    openCard() {
      // const id = 'test-id'
      // this.$router.push(`/novostroyki/${id}`)
    }
  }
}
</script>

<style lang="sass" scoped>

.card-obj
  /*height: 200px*/
  /*border: 1px solid black*/
  /*margin-bottom: 2rem*/
  cursor: pointer
  margin-bottom: 15px

.time
  font-size: 13px
  color: #999

.bottom
  margin-top: 13px
  line-height: 12px

.button
  padding: 0
  float: right

.image
  width: 100%
  display: block

.clearfix:before,
.clearfix:after
  display: table
  content: ""

.clearfix:after
  clear: both
</style>
