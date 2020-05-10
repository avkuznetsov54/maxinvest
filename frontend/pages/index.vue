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
  components: {
    AppCardResidentialComplex
  },
  async fetch({ store, error }) {
    try {
      if (store.getters['real-estate/GET_RESIDENTIAL_COMPLEXES'].length === 0) {
        await store.dispatch('real-estate/FETCH_RESIDENTIAL_COMPLEXES')
      }
    } catch (e) {
      // eslint-disable-next-line no-console
      console.log('error => ' + e)
      error(e)
    }
  },
  data() {
    return {
      data: null
    }
  },
  // mounted() {
  //   this.data = this.$store.getters('real-estate/GET_RESIDENTIAL_COMPLEXES')
  //   // eslint-disable-next-line no-console
  //   console.log(this.data.length)
  // },
  computed: {
    resComplexes() {
      return this.$store.getters['real-estate/GET_RESIDENTIAL_COMPLEXES']
    }
  },
  head() {
    return {
      title: 'Главная'
    }
  }
}
</script>

<style lang="sass"></style>
