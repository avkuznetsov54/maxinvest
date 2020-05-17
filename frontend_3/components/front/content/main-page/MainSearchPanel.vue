<template>
  <Tabs :animated="false" class="search-panel">
    <TabPane label="Коммерческая" name="name1">
      <!--      <div class="desktop-filter-row"></div>-->
      <app-search-panel-commerce />
    </TabPane>
    <TabPane label="Новостройки" name="name2">Новостройки тут</TabPane>
  </Tabs>
</template>

<script>
import AppSearchPanelCommerce from './search-panels/SearchPanelCommerce'
export default {
  name: 'MainSearchPanel',
  components: {
    AppSearchPanelCommerce
  }
}
</script>

<style lang="scss" scoped>
.search-panel {
  height: 200px;
  background: #fff;
  padding: 15px;
  margin: 20px auto 0;
}
.ivu-tabs {
  overflow: visible;
}
</style>
