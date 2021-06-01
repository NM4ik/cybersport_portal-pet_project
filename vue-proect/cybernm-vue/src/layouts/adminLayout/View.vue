<template>
  <v-main>
    <v-app>
      <router-view />
    </v-app>
  </v-main>
</template>

<script>
export default {
  name: 'Adminview',

  data() {
    return {
      visible: true,
    };
  },
  computed: {},
};
</script>
