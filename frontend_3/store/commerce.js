export const state = () => ({
  DATA_VALUE_FILTERS: {},
  DATA_COUNT_OBJ: null,
  DATA_COMMERCE_OBJ: []
})

export const getters = {
  GET_VALUE_FILTERS: (state) => state.DATA_VALUE_FILTERS,
  GET_COUNT_OBJ: (state) => state.DATA_COUNT_OBJ,
  GET_COMMERCE_OBJ: (state) => state.DATA_COMMERCE_OBJ
}

export const mutations = {
  SET_VALUE_FILTERS(state, data) {
    state.DATA_VALUE_FILTERS = data
  },
  SET_COUNT_OBJ(state, data) {
    state.DATA_COUNT_OBJ = data
  },
  SET_COMMERCE_OBJ(state, data) {
    state.DATA_COMMERCE_OBJ = data
  }
}

export const actions = {
  async FETCH_VALUE_FILTERS({ commit }) {
    try {
      const res = await this.$apiCommerce.getFilters()
      commit('SET_VALUE_FILTERS', res)
    } catch (e) {
      // eslint-disable-next-line no-console
      console.log('catch FETCH_VALUE_FILTERS => ' + e)
    }
  },
  async FETCH_COUNT_OBJ({ commit }, payload) {
    try {
      const res = await this.$apiCommerce.getCommerceCount()
      commit('SET_COUNT_OBJ', res.count)
    } catch (e) {
      // eslint-disable-next-line no-console
      console.log('catch FETCH_COUNT_OBJ => ' + e)
    }
  },
  async FETCH_COMMERCE_OBJ({ commit }) {
    try {
      // const data = await this.$http.$get('api/v1/residential/complex/all/')
      const data = await this.$apiCommerce.getAllCommerce()
      // eslint-disable-next-line no-console
      // console.log(data)
      commit('SET_COMMERCE_OBJ', data)
    } catch (e) {
      // eslint-disable-next-line no-console
      console.log('catch FETCH_COMMERCE_OBJ => ' + e)
    }
  },
  async FETCH_COMMERCE_DETAIL({ commit }, id) {
    try {
      return await this.$apiCommerce.getCommerceDetail(id)
    } catch (e) {
      // eslint-disable-next-line no-console
      console.log('catch FETCH_COMMERCE_DETAIL => ' + e)
    }
  }
}
