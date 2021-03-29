import Vue from 'vue';
import Router from 'vue-router';
import Main from '../components/Main.vue';
import Support from '../components/Support.vue';
import Lotto from '../components/Lotto.vue';


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
      path: '/lotto',
      name: 'Lotto',
      component: Lotto,
    },
    {
      path: '/',
      name: 'Main',
      component: Main,
    },
  ],
});
