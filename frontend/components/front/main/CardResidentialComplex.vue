<template>
  <el-card
    shadow="hover"
    :body-style="{ padding: 0 }"
    class="card-obj"
    @click.native="openCard"
  >
    <div class="card-obj-badge">
      <b-badge variant="warning">{{ resComplex.class_of_housing }}</b-badge>
    </div>
    <!--    <img :src="resComplex.main_image" alt="hamburger" class="image" />-->
    <b-img
      :src="resComplex.main_image"
      class="image"
      alt="Responsive image"
    ></b-img>
    <div class="object-item__info-content">
      <nuxt-link to="openCard">{{ resComplex.name }}</nuxt-link>
      <!--      <span>{{ resComplex.name }}</span>-->
      <!--      <div class="bottom clearfix">-->
      <!--        <time class="time">{{ currentDate }}</time>-->
      <!--      </div>-->
      <small>{{ resComplex.city }}</small>
      <small>{{ resComplex.district }}</small>
      <small>{{ resComplex.address }}</small>
    </div>
    <div style="padding: 14px;">
      <el-button type="primary" plain size="small">Узнать подробнее</el-button>
    </div>
  </el-card>
</template>

<script>
export default {
  name: 'CardResidentialComplex',
  props: {
    resComplex: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      currentDate: new Date()
    }
  },

  methods: {
    openCard() {
      // const id = 'test-id'
      this.$router.push(`/novostroyki/${this.resComplex.url_name}`)
    }
  }
}
</script>

<style lang="sass" scoped>

.card-obj
  height: 420px
  /*border: 1px solid black*/
  /*margin-bottom: 2rem*/
  cursor: pointer
  margin-bottom: 15px

.card-obj-badge
  position: absolute
  right: 18px
  top: 5px

.bottom
  margin-top: 13px
  line-height: 12px

.button
  padding: 0
  float: right

.image
  /*width: 100%*/
  height: 160px
  display: block

.object-item__info-content
  padding: 14px
  display: flex
  flex-grow: 1
  flex-direction: column
  align-items: flex-start

.clearfix:before,
.clearfix:after
  display: table
  content: ""

.clearfix:after
  clear: both
</style>
