<template>
  <v-app>
    <pub-bar >
    </pub-bar>

    <pub-view />
  </v-app>
</template>

<script>
export default {
  name: 'Publiclayout',
  components: {
    PubBar: () => import(/* webpackChunkName: 'public-appbar' */ './AppBar'),
    PubView: () => import(/* webpackChunkName: 'public-view' */ './View'),
  },
};
</script>
