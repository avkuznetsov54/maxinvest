<template>
  <div>
    <client-only>
      <!--      <Tabs :animated="false" class="search-panel-tabs">-->
      <!--        <TabPane label="Продажа" name="name1">-->
      <!--          &lt;!&ndash;      <div class="desktop-filter-row"></div>&ndash;&gt;-->
      <!--          <app-search-panel-commerce-sale />-->
      <!--        </TabPane>-->
      <!--        <TabPane label="Аренда" name="name2">-->
      <!--          <app-search-panel-commerce-rent />-->
      <!--        </TabPane>-->
      <!--      </Tabs>-->
      <div>
        <RadioGroup v-model="select" type="button" class="select-mode">
          <Radio label="Продажа" class="select-mode-radio"></Radio>
          <Radio label="Аренда" class="select-mode-radio"></Radio>
        </RadioGroup>
      </div>
      <div class="select-tab">
        <div v-if="select === 'Продажа'">
          <app-search-panel-commerce-sale />
        </div>
        <div v-else-if="select === 'Аренда'">
          <div class="search-panel">
            <app-search-panel-commerce-rent />
          </div>
        </div>
      </div>
    </client-only>
  </div>
</template>

<script>
// import LazyHydrate from 'vue-lazy-hydration'
// import AppSearchPanelCommerceSale from './SearchPanelCommerceSale'
import AppSearchPanelCommerceRent from './SearchPanelCommerceRent'
export default {
  name: 'MainSearchPanel',
  components: {
    // LazyHydrate,
    // eslint-disable-next-line vue/no-unused-components
    AppSearchPanelCommerceSale: () => import('./SearchPanelCommerceSale'),
    // eslint-disable-next-line vue/no-unused-components
    AppSearchPanelCommerceRent
  },
  data() {
    return {
      select: 'Продажа'
    }
  },
  watch: {
    select(newValue) {
      this.$store.dispatch('commerce/FETCH_SWITCH_SALE_RENT', newValue)
    }
  }
}
</script>

<style lang="scss" scoped>
/*.search-panel {*/
/*  height: 254px;*/
/*  max-height: 254px;*/
/*  background: #fff;*/
/*  padding: 15px;*/
/*  margin: 20px auto 0;*/
/*  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.07);*/
/*}*/
.search-panel-tabs {
  background: #fff;
}
.ivu-tabs {
  overflow: visible;
}
.select-mode {
  color: #515a6e;
}
.select-tab {
  color: #515a6e;
  margin-top: 16px;
}
</style>
