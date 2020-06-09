<template>
  <div class="thumb-example">
    <v-gallery
      :images="images"
      :index="index"
      @close="index = null"
    ></v-gallery>
    <!-- swiper1 -->
    <swiper
      ref="swiperTop"
      class="swiper gallery-top"
      :options="swiperOptionTop"
    >
      <!--        <img-->
      <!--          v-img:name-->
      <!--          src="https://avatarko.ru/img/kartinka/33/multfilm_lyagushka_32117.jpg"-->
      <!--        />-->
      <swiper-slide
        v-for="(image, imageIndex) in images"
        :key="imageIndex"
        class="image"
        :style="{
          width: '300px',
          height: '200px'
        }"
        @click.native="index = imageIndex"
      >
        <img :src="image" alt="eqwew" />
      </swiper-slide>
      <div
        slot="button-next"
        class="swiper-button-next swiper-button-white"
      ></div>
      <div
        slot="button-prev"
        class="swiper-button-prev swiper-button-white"
      ></div>
    </swiper>
    <!-- swiper2 Thumbs -->
    <swiper
      ref="swiperThumbs"
      class="swiper gallery-thumbs"
      :options="swiperOptionThumbs"
    >
      <swiper-slide class="slide-1"></swiper-slide>
      <swiper-slide class="slide-2"></swiper-slide>
      <swiper-slide class="slide-3"></swiper-slide>
      <swiper-slide class="slide-4"></swiper-slide>
      <swiper-slide class="slide-5"></swiper-slide>
    </swiper>
  </div>
</template>

<script>
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import 'swiper/css/swiper.css'

export default {
  title: 'Thumbs gallery with Two-way control',
  components: {
    Swiper,
    SwiperSlide
  },
  data() {
    return {
      swiperOptionTop: {
        loop: true,
        loopedSlides: 5, // looped slides should be the same
        spaceBetween: 10,
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev'
        }
      },
      swiperOptionThumbs: {
        loop: true,
        loopedSlides: 5, // looped slides should be the same
        spaceBetween: 10,
        centeredSlides: true,
        slidesPerView: 'auto',
        touchRatio: 0.2,
        slideToClickedSlide: true
      },

      images: [
        'https://avatarko.ru/img/kartinka/33/multfilm_lyagushka_32117.jpg',
        'https://static8.depositphotos.com/1145675/836/i/450/depositphotos_8369327-stock-photo-networks-internet-and-here-wireless.jpg',
        'https://klike.net/uploads/posts/2019-03/1551516106_1.jpg',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcR867rZj08uvTILL_IhBgNiMpug4sLfphXnDVlTgff7QJlIB7LV&usqp=CAU',
        'https://avatars.mds.yandex.net/get-pdb/1649258/d7747967-9aa8-410a-9dbd-8fbbf199e8e5/s600'
      ],
      index: null
    }
  },
  mounted() {
    this.$nextTick(() => {
      const swiperTop = this.$refs.swiperTop.$swiper
      const swiperThumbs = this.$refs.swiperThumbs.$swiper
      swiperTop.controller.control = swiperThumbs
      swiperThumbs.controller.control = swiperTop
    })
  }
}
</script>

<style lang="scss" scoped>
.thumb-example {
  height: 480px;
  /*background-color: #000;*/
}

.swiper {
  .swiper-slide {
    background-size: cover;
    background-position: center;

    &.slide-1 {
      background-image: url('https://avatarko.ru/img/kartinka/33/multfilm_lyagushka_32117.jpg');
    }
    &.slide-2 {
      background-image: url('https://static8.depositphotos.com/1145675/836/i/450/depositphotos_8369327-stock-photo-networks-internet-and-here-wireless.jpg');
    }
    &.slide-3 {
      background-image: url('https://klike.net/uploads/posts/2019-03/1551516106_1.jpg');
    }
    &.slide-4 {
      background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcR867rZj08uvTILL_IhBgNiMpug4sLfphXnDVlTgff7QJlIB7LV&usqp=CAU');
    }
    &.slide-5 {
      background-image: url('https://avatars.mds.yandex.net/get-pdb/1649258/d7747967-9aa8-410a-9dbd-8fbbf199e8e5/s600');
    }
  }

  &.gallery-top {
    height: 80%;
    width: 100%;
  }
  &.gallery-thumbs {
    height: 20%;
    box-sizing: border-box;
    padding: 10px 0;
  }
  &.gallery-thumbs .swiper-slide {
    width: 15%;
    height: 100%;
    opacity: 0.4;
  }
  &.gallery-thumbs .swiper-slide-active {
    opacity: 1;
  }
}
</style>
