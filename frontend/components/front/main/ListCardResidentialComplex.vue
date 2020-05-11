<template>
  <b-row>
    <b-col
      v-for="resComplex in resComplexes"
      :key="resComplex.id"
      cols="12"
      sm="6"
      md="4"
      lg="3"
    >
      <app-card-residential-complex :res-complex="resComplex" />
    </b-col>
  </b-row>
</template>

<script>
import AppCardResidentialComplex from '@/components/front/main/CardResidentialComplex'
export default {
  name: 'ListCardResidentialComplex',
  components: {
    AppCardResidentialComplex
  },
  computed: {
    resComplexes() {
      return this.$store.getters['real-estate/GET_RESIDENTIAL_COMPLEXES']
    }
  }
}
</script>

<style scoped></style>
