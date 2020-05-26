<template>
  <Tabs :animated="false" class="search-panel">
    <TabPane label="Продажа" name="name1">
      <!--      <div class="desktop-filter-row"></div>-->
      <app-search-panel-commerce-sale />
    </TabPane>
    <TabPane label="Аренда" name="name2">
      <app-search-panel-commerce-rent />
    </TabPane>
  </Tabs>
</template>

<script>
// import { hydrateWhenVisible } from 'vue-lazy-hydration'
import AppSearchPanelCommerceSale from './SearchPanelCommerceSale'
import AppSearchPanelCommerceRent from './SearchPanelCommerceRent'
export default {
  name: 'MainSearchPanel',
  components: {
    AppSearchPanelCommerceSale,
    AppSearchPanelCommerceRent
  }
}
</script>

<style lang="scss" scoped>
.search-panel {
  max-height: 254px;
  background: #fff;
  padding: 15px;
  margin: 20px auto 0;
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.07);
}
.ivu-tabs {
  overflow: visible;
}
</style>
