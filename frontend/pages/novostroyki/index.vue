<template>
  <app-list-card-residential-complex />
</template>

<script>
import AppListCardResidentialComplex from '@/components/front/main/ListCardResidentialComplex'
export default {
  components: {
    AppListCardResidentialComplex
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

  head() {
    return {
      title: 'Новостройки'
    }
  }
}
</script>

<style scoped></style>
