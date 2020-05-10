<template>
  <b-row>
    <b-col cols="12" sm="6" md="4" lg="3">
      <app-card-obj />
    </b-col>
    <b-col cols="12" sm="6" md="4" lg="3">
      <app-card-obj />
    </b-col>
    <b-col cols="12" sm="6" md="4" lg="3">
      <app-card-obj />
    </b-col>
    <b-col cols="12" sm="6" md="4" lg="3">
      <app-card-obj />
    </b-col>
  </b-row>
</template>

<script>
import AppCardObj from '@/components/front/main/CardObj'
export default {
  components: {
    AppCardObj
  },
  head() {
    return {
      title: 'Главная'
    }
  }
}
</script>

<style lang="sass"></style>
