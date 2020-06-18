<template>
  <div class="container my-40">
    <Row>
      <i-col
        v-for="resObj in comObjs"
        :key="resObj.id"
        :xs="24"
        :sm="8"
        :md="6"
        :lg="6"
      >
        <app-commerce-card
          :com-obj="resObj"
          :switch-sale-rent="switchSaleRent"
        />
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
    comObjs() {
      return this.$store.getters['commerce/GET_COMMERCE_OBJ']
    },
    switchSaleRent() {
      return this.$store.getters['commerce/GET_SWITCH_SALE_RENT']
    }
  },
  watch: {
    switchSaleRent(newValue) {
      // eslint-disable-next-line no-console
      // console.log(newValue)
      this.fetchFilterObjs(newValue)
    }
  },
  async mounted() {
    if (this.$store.getters['commerce/GET_COMMERCE_OBJ'].length === 0) {
      await this.$store.dispatch('commerce/FETCH_COMMERCE_OBJ')
    }
  },
  methods: {
    async fetchFilterObjs(newValue) {
      const params = new URLSearchParams()
      if (newValue === 'Продажа') {
        // const params = { is_sale: true }
        // await this.$store.dispatch('commerce/FETCH_COMMERCE_OBJ', params)
        params.append('is_sale', true)
      } else if (newValue === 'Аренда') {
        // const params = { is_rent: true }
        // await this.$store.dispatch('commerce/FETCH_COMMERCE_OBJ', params)
        params.append('is_rent', true)
      }
      await this.$store.dispatch('commerce/FETCH_COMMERCE_OBJ', params)
    }
  }
}
</script>

<style scoped></style>
