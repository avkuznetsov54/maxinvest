export default {
  mode: 'universal',
  /*
   ** Headers of the page
   */
  head: {
    title: process.env.npm_package_name || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: process.env.npm_package_description || ''
      }
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }]
  },
  /*
   ** Customize the progress-bar color
   */
  loading: { color: 'red' },
  /*
   ** Global CSS
   */
  css: ['element-ui/lib/theme-chalk/index.css', '@/theme/index.sass'],
  /*
   ** Plugins to load before mounting the App
   */
  plugins: ['@/plugins/globals'],
  /*
   ** Nuxt.js dev-modules
   */
  buildModules: [
    // Doc: https://github.com/nuxt-community/eslint-module
    '@nuxtjs/eslint-module'
  ],
  /*
   ** Nuxt.js modules
   */
  modules: [
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios',
    '@nuxtjs/proxy',
    'bootstrap-vue/nuxt'
  ],
  /*
   ** Axios module configuration
   ** See https://axios.nuxtjs.org/options
   */
  axios: {
    // baseURL: process.env.BASE_URL || 'http://localhost:8000'
    baseURL: 'http://localhost:8000'
  },
  proxy: {
    '/media': {
      target: 'http://localhost:8000',
      pathRewrite: {
        '^/media': '/media'
      }
    }
  },
  bootstrapVue: {
    icons: true,
    // https://bootstrap-vue.org/docs#tree-shaking-with-nuxtjs
    components: ['BContainer', 'BRow', 'BCol', 'BIconArrowUp'],
    componentPlugins: ['IconsPlugin']
  },
  /*
   ** Build configuration
   */
  build: {
    transpile: [/^element-ui/],
    /*
     ** You can extend webpack config here
     */
    extend(config, ctx) {}
  }
}
