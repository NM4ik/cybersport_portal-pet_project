import Vue from 'vue';
import App from '@/App.vue';
import router from '@/router';
import store from '@/store';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.css';
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import Vuelidate from 'vuelidate'
Vue.use(Vuelidate)

library.add(fas)
Vue.component('fa', FontAwesomeIcon)


Vue.use(Vuetify)

Vue.component('public_layout', () => import('@/layouts/publicLayout/Index'))
Vue.component('admin_layout', () => import('@/layouts/adminLayout/Index'))
Vue.component('autorize_layout', () => import('@/layouts/authorizationLayout/Index'))

new Vue({
  router,
  vuetify: new Vuetify({ iconfont: 'mdi' }),
  render: (h) => h(App),
  store,
}).$mount('#app');
