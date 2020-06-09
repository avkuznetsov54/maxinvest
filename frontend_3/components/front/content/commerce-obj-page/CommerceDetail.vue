<template>
  <Row>
    <i-col :xs="24" :sm="8" :md="6" :lg="16">
      <client-only>
        <app-gallery />
      </client-only>
    </i-col>
  </Row>
</template>

<script>
import AppGallery from './Gallery'
export default {
  components: {
    AppGallery
  },
  props: {
    data: {
      type: Object,
      required: true
    }
  },
  mounted() {
    // eslint-disable-next-line no-console
    console.log(this.data)
  }
}
</script>
