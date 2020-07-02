<template>
  <Row>
    <i-col span="24">
      <div v-if="isVisiblePage" class="text-center">
        <Page
          :total="lenPag"
          :current="currentPage"
          :page-size="3"
          @on-change="changePage"
        />
      </div>
    </i-col>
  </Row>
</template>

<script>
export default {
  name: 'Pagination',
  data() {
    return {
      isVisiblePage: false
    }
  },
  computed: {
    countObj() {
      return this.$store.getters['commerce/GET_COUNT_OBJ']
    },
    lenPag() {
      return Math.ceil(this.countObj)
    },
    currentPage() {
      if (
        typeof this.$store.getters['commerce/GET_PARAMS_FOR_FILTERS'].page !==
        'undefined'
      ) {
        const page = this.$store.getters['commerce/GET_PARAMS_FOR_FILTERS'].page
        return Number(page)
      } else {
        return 1
      }
    },

    paramsFilter() {
      return this.$store.getters['commerce/GET_PARAMS_FOR_FILTERS']
    }
  },
  mounted() {
    if (this.currentPage) {
      this.isVisiblePage = true
    } else {
      this.isVisiblePage = false
    }
  },
  methods: {
    changePage(e) {
      // eslint-disable-next-line no-console
      // console.log(e)

      if (this.$route.path === '/commerce') {
        const newParams = { ...this.paramsFilter, page: String(e) }
        // eslint-disable-next-line no-console
        // console.log(newArr)
        this.$store.dispatch('commerce/FETCH_PARAMS_FOR_FILTERS', newParams)
        this.$router.push({ query: this.paramsFilter })
        this.$store.dispatch('commerce/FETCH_COMMERCE_OBJ', this.paramsFilter)
      }
    }
  }
}
</script>

<style scoped></style>
