import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'
import ProfileView from '@/views/ProfileView.vue'
import MovieListView from '@/views/MovieListView.vue'
import MovieListDetailView from '@/views/MovieListDetailView.vue'
import EndingListView from '@/views/EndingListView.vue'
import EndingListDetailView from '@/views/EndingListDetailView.vue'
import EndingListCreateView from '@/views/EndingListCreateView.vue'
import CommunityView from '@/views/CommunityView.vue'
import CommunityDetailView from '@/views/CommunityDetailView.vue'
import CommunityCreateView from '@/views/CommunityCreateView.vue'
import MovieListSelectView from '@/views/MovieListSelectView.vue'
import { useMovieStore } from '@/stores/counter'
import CommunityUpdateView from '@/views/CommunityUpdateView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // 1. 메인 페이지
    {
      path: '/',
      name: 'Home',
      component: HomeView,
    },
    // 2. 로그인 페이지
    {
      path: '/login',
      name: 'Login',
      component: LoginView
    },
    // 3. 회원가입 페이지
    {
      path: '/signup',
      name: 'SignUp',
      component: SignUpView
    },
    // 4. 사용자 프로필 페이지
    {
      path: '/profile/:userid',
      name: 'Profile',
      component: ProfileView
    },
    // 5. 원본 영화 리스트 페이지
    {
      path: '/movielist',
      name: 'MovieList',
      component: MovieListView
    },
    // 6. 원본 영화 선택 페이지
    {
      path: '/movieselect',
      name: 'MovieSelect',
      component: MovieListSelectView
    },
    // 7. 원본 영화 상세 페이지
    {
      path: '/movielist/:movieid',
      name: 'MovieListDetail',
      component: MovieListDetailView
    },
    // 8. 대체 결말 리스트 페이지
    {
      path: '/ending',
      name: 'EndingList',
      component: EndingListView
    },
    // 9. 대체 결말 상세 페이지
    {
      path: '/ending/:endingid',
      name: 'EndingListDetail',
      component: EndingListDetailView
    },
    // 10. 대체 결말 생성 페이지
    {
      path: '/ending/create/:movieid',
      name: 'EndingListCreate',
      component: EndingListCreateView
    },
    // 11. 커뮤니티 게시판 페이지
    {
      path: '/community',
      name: 'Community',
      component: CommunityView
    },
    // 12. 커뮤니티 게시글 상세 페이지
    {
      path: '/community/:articleid',
      name: 'CommunityDetail',
      component: CommunityDetailView
    },
    // 13. 커뮤니티 게시글 작성 페이지
    {
      path: '/community/create',
      name: 'CommunityCreate',
      component: CommunityCreateView
    },
    // 14. 커뮤니티 게시글 수정 페이지
    {
      path: '/community/:articleid/update',
      name: 'CommunityUpdate',
      component: CommunityUpdateView
    }
  ],
})

router.beforeEach ((to, from) => {
  const store = useMovieStore()
  if ((to.name==='CommunityCreate'|to.name==='EndingListCreate'|to.name==='MovieSelect'|to.name==='Profile') && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name : 'LoginView'}
  }
  else if ((to.name === 'SignUp'|to.name==='Login') && store.isLogin){
    window.alert('이미 로그인 되어 있습니다.')
    return { name : 'HomeView'}
  }
})

export default router
