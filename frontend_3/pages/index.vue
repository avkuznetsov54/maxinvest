<template>
  <div>
    <app-main-view />
    <app-main-page-content />
  </div>
</template>

<script>
import AppMainView from '@/components/front/content/main-page/MainView'
import AppMainPageContent from '@/components/front/content/main-page/MainPageContent'
export default {
  components: {
    AppMainView,
    AppMainPageContent
  },
  async fetch({ store, error }) {
    try {
      if (
        Object.keys(
          store.getters['value-for-filters/GET_VALUE_FILTERS'].length === 0
        )
      ) {
        await store.dispatch('value-for-filters/FETCH_VALUE_FILTERS')
      }
    } catch (e) {
      // eslint-disable-next-line no-console
      console.log('error => ' + e)
      error(e)
    }
  }
}
</script>

<style lang="sass" scoped>
.iit
  margin: 0 8px
  height: 50px
  background-color: #47494e
</style>
