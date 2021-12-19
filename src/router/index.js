import Vue from 'vue'
import Router from 'vue-router'
import webApp from '@/components/webApp'
import canvas from '@/components/canvas'
Vue.use(Router)

let router = new Router({
  routes: [
    {
      path: '/',
      name: 'webApp',
      component: webApp
    },
    {
      path: '/canvas',
      name: 'canvas',
      component: canvas
    }
  ]
})
export default router