<template>
  <Tabs :animated="false" class="search-panel">
    <TabPane label="Покупка" name="name1">
      <!--      <div class="desktop-filter-row"></div>-->
      ewqeqw
    </TabPane>
    <TabPane label="Аренда" name="name2">
      ewqeqwe
    </TabPane>
  </Tabs>
</template>

<script>
export default {
  name: 'SearchPanelNewBuilding',

  data() {
    return {}
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
