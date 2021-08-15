<template>
  <v-container>
    <v-card>
      <v-toolbar class="toolbar-back" dark>
        <template v-slot:extension>
          <v-tabs v-model="tabs" centered>
            <v-tab>tournaments</v-tab>
            <v-tab>players</v-tab>
            <v-tab>disciplines</v-tab>
          </v-tabs>
        </template>
      </v-toolbar>

      <v-tabs-items v-model="tabs">
        <v-tab-item>
          <v-card flat>
            <tournaments />
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card flat>
            <players />
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card flat>
            <disciplines />
          </v-card>
        </v-tab-item>
      </v-tabs-items>
    </v-card>
  </v-container>
</template>

<style scoped>
.v-toolbar {
  border-radius: 0 !important;
}
.toolbar-back {
  background: #3a3a3a !important;
}
</style>

<script>
import tournaments from "@/views/rootComponents/adminpage/tournaments";
import disciplines from "@/views/rootComponents/adminpage/disciplines";
import players from "@/views/rootComponents/adminpage/players";

export default {
  components: {
    tournaments,
    disciplines,
    players,
  },
  data() {
    return {
      tabs: null,
      text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    };
  },
};
</script>
