<template>
  <div class="container my-40">
    <Row>
      <i-col
        v-for="resComplex in resComplexes"
        :key="resComplex.id"
        :xs="24"
        :sm="8"
        :md="6"
        :lg="6"
      >
        <app-commerce-card :res-complex="resComplex" />
      </i-col>
    </Row>
  </div>
</template>

<script>
import AppCommerceCard from '@/components/front/content/commerce-page/CommerceCard'
export default {
  name: 'CommerceListCard',
  components: {
    AppCommerceCard
  },
  computed: {
    resComplexes() {
      return this.$store.getters['commerce/GET_COMMERCE_OBJ']
    }
  },
  async mounted() {
    // if (this.$store.getters['commerce/GET_COMMERCE_OBJ'].length === 0) {
    await this.$store.dispatch('commerce/FETCH_COMMERCE_OBJ')
    // }
  }
}
</script>

<style scoped></style>
