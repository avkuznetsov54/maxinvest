<template>
  <Row>
    <i-col :xs="24" :sm="8" :md="6" :lg="14">
      <client-only>
        <!--        <app-gallery :images-obj="imagesObj" />-->
        <app-fotorama :images-obj="imagesObj" />
      </client-only>
    </i-col>
  </Row>
</template>

<script>
// import AppGallery from './Gallery'
import AppFotorama from './Fotorama'
export default {
  components: {
    // AppGallery,
    AppFotorama
  },
  props: {
    data: {
      type: Object,
      required: true
    }
  },
  computed: {
    imagesObj() {
      // return {
      //   main_image: this.data.main_image,
      //   main_image_thumb: this.data.main_image_thumb,
      //   images_commercial_estate: this.data.images_commercial_estate
      // }
      return [
        {
          image: this.data.main_image,
          image_thumb: this.data.main_image_thumb
        },
        ...this.data.images_commercial_estate
      ]
    }
  },
  mounted() {
    // eslint-disable-next-line no-console
    // console.log(this.data)
  }
}
</script>
