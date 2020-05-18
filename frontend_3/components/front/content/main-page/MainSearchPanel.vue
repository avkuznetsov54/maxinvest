<template>
  <Tabs :animated="false" class="search-panel">
    <TabPane label="Продажа" name="name1">
      <!--      <div class="desktop-filter-row"></div>-->
      <app-search-panel-commerce-sale />
    </TabPane>
    <TabPane label="Аренда" name="name2">Аренда тут</TabPane>
  </Tabs>
</template>

<script>
import AppSearchPanelCommerceSale from './search-panels/SearchPanelCommerceSale'
export default {
  name: 'MainSearchPanel',
  components: {
    AppSearchPanelCommerceSale
  }
}
</script>

<style lang="scss" scoped>
.search-panel {
  min-height: 230px;
  background: #fff;
  padding: 15px;
  margin: 20px auto 0;
}
.ivu-tabs {
  overflow: visible;
}
</style>
