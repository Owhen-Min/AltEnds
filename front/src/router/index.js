import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'
import ProfileView from '@/views/ProfileView.vue'
import AiBoard from '@/views/AiBoard.vue'
import CommunityView from '@/views/CommunityView.vue'
import MovieListView from '@/views/MovieListView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/aiboard',
      name: 'aiboard',
      component: AiBoard
    },
    {
      path: '/community',
      name: 'community',
      component: CommunityView
    },
    {
      path:'/movielist',
      name:'movielist',
      component: MovieListView
    },
    {
      path:'/movielist/detail',
      name:'MovieDetail',
      component: MovieDetailView
    }
  ],
})

export default router
