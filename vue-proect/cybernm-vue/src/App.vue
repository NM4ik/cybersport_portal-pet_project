
<template>
    <v-fade-transition mode="out-in">
      <component :is="currentLayout" />
    </v-fade-transition>
</template>

<script>
export default {
  name: 'AppVue',
  computed: {
    currentLayout() {
      return this.$route.meta.layout;
    },
  },
};
</script>

<style>

  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap');
  *{
    font-family: 'Inter', sans-serif;
  }

</style>
