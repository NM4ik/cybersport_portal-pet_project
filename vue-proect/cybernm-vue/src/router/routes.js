export default [
  //Fallback route
  {
    path: '/',
    redirect: {
      path: '/homepage',
    },
  },

  {
    path: '/homepage',
    name: 'homepage',
    meta: { layout: 'public_layout' },
    component: () => import('@/views/publicComponents/homepage/home.vue'),
  },
  
  {
    path: '/player',
    name: 'players',
    meta: { layout: 'public_layout' },
    component: () => import('@/views/publicComponents/homepage/playerspage.vue'),  
  },

  {
    path: '/tournament',
    name: 'tournaments',
    meta: { layout: 'public_layout' },
    component: () => import('@/views/publicComponents/homepage/tournamentspage.vue'),
  },

  {
    path: '/discipline',
    name: 'discipline',
    meta: { layout: 'public_layout' },
    component: () => import('@/views/publicComponents/homepage/discipline-page.vue'),
  },

  {
    path: '/tournament/:id',
    name: 'tournament',
    meta: { layout: 'public_layout' },
    component: () => import('@/views/publicComponents/homepage/onetournamentpage.vue'),
  },

  {
    path: '/news',
    name: 'news',
    meta: { layout: 'public_layout' },
    component: () => import('@/views/publicComponents/homepage/news-page.vue'),
  },

  {
    path: '/news/:id',
    name: 'news',
    meta: { layout: 'public_layout' },
    component: () => import('@/views/publicComponents/homepage/onenews-page.vue'),
  },

  {
    path: '/player/:id',
    name: 'player',
    meta: { layout: 'public_layout' },
    component: () => import('@/views/publicComponents/homepage/oneplayer-page.vue'),
  },

  {
    path: '*',
    name: 'error',
    meta: { layout: 'public_layout', requiresAuth: false },
    component: () => import('@/views/publicComponents/notfound/index.vue'),
  },

  {
    path: '/administration',
    name: 'admin',
    meta: { layout: 'admin_layout' },
    component: () => import('@/views/publicComponents/adminpage/admin.vue'),
  },
  
  
];
