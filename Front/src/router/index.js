import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/HomeView.vue')
    },
    {
      path: '/running',
      name: 'running',
      component: () => import('@/views/RunningView.vue')
    },
    {
      path: '/setting',
      name: 'setting',
      component: () => import('@/views/SettingView.vue')
    }
  ]
})

export default router