<template>
  <div>
    <div class="search-panel-wrap">
      <div class="container">
        <div class="search-panel-page">
          <app-main-search-panel-commerce />
        </div>
      </div>
    </div>
    <div>
      <div class="container">
        <app-commerce-list-card />
      </div>
    </div>
  </div>
</template>

<script>
import AppMainSearchPanelCommerce from '@/components/front/content/search-panels-commerce/MainSearchPanelCommerce'
import AppCommerceListCard from '@/components/front/content/commerce-page/CommerceListCard'

export default {
  components: {
    AppMainSearchPanelCommerce,
    AppCommerceListCard
  },
  mounted() {
    // eslint-disable-next-line no-console
    // console.log(this.$route.query)
    // eslint-disable-next-line no-console
    // console.log(this.$route)
  }
}
</script>

<style lang="scss" scoped>
.search-panel-wrap {
  background: #fff;
  padding: 20px 0;
  height: 300px;
}
.search-panel-page {
  height: 254px;
  max-height: 254px;
  background: #fff;
  padding: 15px;
  /*margin: 20px auto 0;*/
  /*box-shadow: 0 6px 16px rgba(0, 0, 0, 0.07);*/
}
</style>
