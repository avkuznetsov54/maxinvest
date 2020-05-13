<template>
  <!--  <Card :padding="0" class="card" @click.native="openCard">-->
  <!--  <Card :padding="0" class="card">-->
  <div class="card">
    <div class="card-obj-badge">
      <Tag class="card-obj-badge-tag" color="primary">{{
        resComplex.class_of_housing
      }}</Tag>
    </div>

    <div v-if="resComplex.images_residential_complex.length === 0">
      <div class="card-wrap-image" @click="openCard">
        <!--        <img-->
        <!--          class="card-image"-->
        <!--          :src="resComplex.main_image"-->
        <!--          :alt="resComplex.name"-->
        <!--        />-->
        <img
          v-lazy-load
          class="card-image"
          :data-src="resComplex.main_image"
          :alt="resComplex.name"
        />
        <!--        <img-->
        <!--          v-lazy="resComplex.main_image"-->
        <!--          class="card-image"-->
        <!--          :alt="resComplex.name"-->
        <!--        />-->
      </div>
    </div>

    <div v-else>
      <div v-swiper:mySwiper="swiperOption">
        <div class="swiper-wrapper">
          <div class="swiper-slide">
            <div class="card-wrap-image" @click="openCard">
              <!--              <img-->
              <!--                class="card-image"-->
              <!--                :src="resComplex.main_image"-->
              <!--                :alt="resComplex.name"-->
              <!--              />-->
              <img
                v-lazy-load
                class="card-image"
                :data-src="resComplex.main_image"
                :alt="resComplex.name"
              />
              <!--              <img-->
              <!--                v-lazy="resComplex.main_image"-->
              <!--                class="card-image"-->
              <!--                :alt="resComplex.name"-->
              <!--              />-->
            </div>
          </div>
          <div
            v-for="img in resComplex.images_residential_complex"
            :key="img.id"
            class="swiper-slide"
          >
            <div class="card-wrap-image" @click="openCard">
              <!--              <img class="card-image" :src="img.image" :alt="img.alt_attr" />-->
              <img
                v-lazy-load
                class="card-image"
                :data-src="img.image"
                :alt="img.alt_attr"
              />
              <!--              <img v-lazy="img.image" class="card-image" :alt="img.alt_attr" />-->
            </div>
          </div>
        </div>
        <div class="swiper-pagination"></div>
        <div class="swiper-button-prev"></div>
        <div class="swiper-button-next"></div>
      </div>
    </div>

    <div class="card-content" @click="openCard">
      <nuxt-link to="openCard">{{ resComplex.name }}</nuxt-link>
      <!--      <span>{{ resComplex.name }}</span>-->
      <!--      <div class="bottom clearfix">-->
      <!--        <time class="time">{{ currentDate }}</time>-->
      <!--      </div>-->
      <small>{{ resComplex.city }}</small>
      <small>{{ resComplex.district }}</small>
      <small>{{ resComplex.address }}</small>
    </div>
  </div>
  <!--  </Card>-->
</template>

<script>
// import { Swiper, SwiperSlide, directive } from 'vue-awesome-swiper'
import { directive } from 'vue-awesome-swiper'
export default {
  name: 'ResidentialComplexCard',
  components: {},
  directives: {
    swiper: directive
  },
  props: {
    resComplex: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      value1: 0,
      swiperOption: {
        pagination: {
          el: '.swiper-pagination',
          type: 'fraction'
        },
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev'
        }
      }
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

<style lang="scss" scoped>
.card {
  height: 300px;
  margin-bottom: 16px;
  /*border-radius: 8px;*/
  /*z-index: 2;*/
  /*overflow: hidden;*/
  /*-webkit-mask-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAA5JREFUeNpiYGBgAAgwAAAEAAGbA+oJAAAAAElFTkSuQmCC); !* this fixes the overflow:hidden in Chrome/Opera *!*/
}
.card-wrap-image {
  cursor: pointer;
}
.card-obj-badge {
  position: absolute;
  right: 18px;
  top: 5px;
  z-index: 2;
}
.card-obj-badge-tag {
  cursor: default;
}
.swiper-pagination {
  font-size: 14px;
  color: #fff;
}
.swiper-button-prev,
.swiper-button-next {
  background-color: #fff !important;
  border-radius: 26px;
  width: 38px;
  height: 38px;
  opacity: 0.35;
  &:hover {
    background-color: #fff !important;
    opacity: 0.75;
  }
}
.swiper-button-disabled {
  display: none;
}
.swiper-button-prev:after,
.swiper-button-next:after {
  font-size: 18px;
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
      height: 200px;
      /*overflow: hidden;*/
    }
  }
}
.card-content {
  height: 100%;
  padding: 14px;
  display: flex;
  flex-grow: 1;
  flex-direction: column;
  align-items: flex-start;
  cursor: pointer;
}
</style>
