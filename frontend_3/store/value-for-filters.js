export const state = () => ({
  DATA_VALUE_FILTERS: {},
  DATA_COUNT_OBJ: null
})

export const getters = {
  GET_VALUE_FILTERS: (state) => state.DATA_VALUE_FILTERS,
  GET_COUNT_OBJ: (state) => state.DATA_COUNT_OBJ
}

export const mutations = {
  SET_VALUE_FILTERS(state, data) {
    state.DATA_VALUE_FILTERS = data
  },
  SET_COUNT_OBJ(state, data) {
    state.DATA_COUNT_OBJ = data
  }
}

export const actions = {
  async FETCH_VALUE_FILTERS({ commit }) {
    try {
      // const { data } = await this.$axios.get('api/v1/filters/')
      // const res = await this.$http.$get('api/v1/filters/')
      const res = await this.$apiMain.getFilters()
      // const data = await res.json()
      commit('SET_VALUE_FILTERS', res)
      // eslint-disable-next-line no-console
      // console.log(data)
    } catch (e) {
      // eslint-disable-next-line no-console
      console.log('catch FETCH_VALUE_FILTERS => ' + e)
    }
  },
  async FETCH_COUNT_OBJ({ commit }, payload) {
    try {
      // const { data } = await this.$axios.get('api/v1/count/', {
      //   params: payload
      // })
      // const res = await this.$http.$get('api/v1/count/')
      const res = await this.$apiMain.getComplexCount()
      // const data = await res.json()
      commit('SET_COUNT_OBJ', res.count)
      // eslint-disable-next-line no-console
      // console.log(res)
    } catch (e) {
      // eslint-disable-next-line no-console
      console.log('catch FETCH_COUNT_OBJ => ' + e)
    }
  }
}
