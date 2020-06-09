<template>
  <div class="container">
    <app-commerce-detail :data="data" />
  </div>
</template>

<script>
import AppCommerceDetail from '@/components/front/content/commerce-obj-page/CommerceDetail'
export default {
  validate({ params }) {
    return Boolean(params.id)
  },
  components: {
    AppCommerceDetail
  },
  async asyncData({ store, params }) {
    const data = await store.dispatch(
      'commerce/FETCH_COMMERCE_DETAIL',
      params.id
    )
    return { data }
  }
}
</script>
