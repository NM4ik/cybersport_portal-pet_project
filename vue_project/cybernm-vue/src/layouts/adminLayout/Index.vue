<template>
  <v-app>
    <pubes-bar> </pubes-bar>
    <PubesNav />
    <pubes-view />
  </v-app>
</template>

<script>
export default {
  name: "adminLayout",
  components: {
    PubesBar: () => import(/* webpackChunkName: 'public-appbar' */ "./AppBar"),
    PubesView: () => import(/* webpackChunkName: 'public-view' */ "./View"),
    PubesNav: () => import(/* webpackChunkName: 'public-appbar' */ "./navtabs"),
  },
};
</script>
