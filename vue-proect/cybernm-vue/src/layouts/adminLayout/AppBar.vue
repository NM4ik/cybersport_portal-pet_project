<template>
  
    <v-toolbar 
    flat
    dark
    class="header_back"
   
    >
     <v-container class="pa-0 header_container d-flex justify-space-between align-sm-center">

    

      <router-link to="/homepage" class="linkhome"><v-toolbar-title class="cybernm_header">CYBERNM</v-toolbar-title></router-link>
      <v-toolbar-items>
        <h2>ADMINPAGE</h2>
      </v-toolbar-items>

      <v-toolbar-items>
        <div class="my-2">
            <v-btn
              class="mr-5"
              color="#FFA500"
              dark
              @click="logout()"
            >
              LOG OUT
            </v-btn>
          </div>
      </v-toolbar-items>
        </v-container>
    </v-toolbar>

</template>
<script>
import $ from 'jquery'
export default {
  data() {
    return {
      
    };
  },
  methods: {
        logout () {
            localStorage.removeItem("auth_token");
            window.location.replace("/");
        }
      },
};
</script>

<style>
.linkhome{
  text-decoration: nones;
}

  .button_signup{
    color: #FFA500;
  }

  .header_back{
    background: #3A3A3A!important;
  }
  .cybernm_header{
    font-size: 28px;
    font-weight: 900;
    color: white;
  }
</style>
