import Vue from 'vue';
import Router from 'vue-router';
import Ping from '../components/Ping.vue';
import Support from '../components/Support.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/support',
      name: 'Support',
      component: Support,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
});
