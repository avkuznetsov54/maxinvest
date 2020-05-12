<template>
  <Card :padding="0" class="card" @click.native="openCard">
    <div class="card-obj-badge">
      <Tag color="primary">{{ resComplex.class_of_housing }}</Tag>
    </div>
    <div class="card-wrap-image">
      <img
        class="card-image"
        :src="resComplex.main_image"
        :alt="resComplex.name"
      />
    </div>
    <div class="card-content">
      <nuxt-link to="openCard">{{ resComplex.name }}</nuxt-link>
      <!--      <span>{{ resComplex.name }}</span>-->
      <!--      <div class="bottom clearfix">-->
      <!--        <time class="time">{{ currentDate }}</time>-->
      <!--      </div>-->
      <small>{{ resComplex.city }}</small>
      <small>{{ resComplex.district }}</small>
      <small>{{ resComplex.address }}</small>
    </div>
  </Card>
</template>

<script>
export default {
  name: 'ResidentialComplexCard',
  props: {
    resComplex: {
      type: Object,
      required: true
    }
  },
  // data() {
  //   return {
  //     currentDate: new Date()
  //   }
  // },

  methods: {
    openCard() {
      // const id = 'test-id'
      this.$router.push(`/novostroyki/${this.resComplex.url_name}`)
    }
  }
}
</script>

<style lang="scss" scoped>
.card {
  margin-bottom: 16px;
  cursor: pointer;
}
.card-obj-badge {
  position: absolute;
  right: 18px;
  top: 5px;
}
.card-wrap-image {
  display: flex;
  justify-content: center; /*центрируем элемент по горизонтали */
  align-items: center; /* и вертикали */
  /*width: auto; !* задали размеры блоку-родителю *!*/
  /*height: 200px;*/
  overflow: hidden; /* если элемент больше блока-родителя – обрезаем лишнее */

  .card-image {
    display: flex;
    flex: 1 1;
    /*padding: 20px;*/
    height: 200px;
    /*border: 1px solid;*/
    align-items: center;

    .card-image img {
      max-width: 100%;
    }
  }
}
.card-content {
  padding: 14px;
  display: flex;
  flex-grow: 1;
  flex-direction: column;
  align-items: flex-start;
}
</style>
