export const state = () => ({
  DATA_VALUE_FILTERS: {}
})

export const getters = {
  GET_VALUE_FILTERS: (state) => state.DATA_VALUE_FILTERS
}

export const mutations = {
  SET_VALUE_FILTERS(state, data) {
    state.DATA_VALUE_FILTERS = data
  }
}

export const actions = {
  async FETCH_VALUE_FILTERS({ commit }) {
    try {
      const { data } = await this.$axios.get('api/v1/filters/')
      commit('SET_VALUE_FILTERS', data)
      // eslint-disable-next-line no-console
      // console.log(data)
    } catch (e) {
      // eslint-disable-next-line no-console
      console.log('catch FETCH_VALUE_FILTERS => ' + e)
    }
  }
}
