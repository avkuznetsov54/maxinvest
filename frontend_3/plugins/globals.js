import Vue from 'vue'
import iView from 'iview'
import locale from 'iview/dist/locale/ru-RU' // Change locale, check node_modules/iview/dist/locale

import VueAwesomeSwiper from 'vue-awesome-swiper'
import 'swiper/css/swiper.css'

Vue.use(iView, {
  locale
})

Vue.use(VueAwesomeSwiper /* { default options with global component } */)
