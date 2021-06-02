<template>
  
    <v-toolbar 
    flat
    dark
    class="mb-5 header_back"
   
    >
     <v-container class="pa-0 header_container d-flex justify-space-between align-sm-center">

    

      <v-toolbar-title class="cybernm_header">
        <router-link to="/" class="cybernm_link">CYBERNM</router-link>
      </v-toolbar-title>
      <v-toolbar-items>
        <v-btn class="nav-menu" text to = "/tournament">
          <span>Tournaments</span>
        </v-btn>

        <v-btn class="nav-menu" text to = "/player">
          <span>Players</span>
        </v-btn>

      <v-menu offset-y>
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          class="nav-menu"
          v-bind="attrs"
          v-on="on"
          text
        >
        <span>MORE</span>
        <fa icon="chevron-down" />
        </v-btn>
        

      </template>
      <v-list class="b_list">
        <v-list-item>
          <v-list-item-title class="v-list-link"><router-link to="/discipline">disciplines</router-link></v-list-item-title>
        </v-list-item>
        <v-list-item>
          <v-list-item-title class="v-list-link"><router-link to="/news">news</router-link></v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
          </v-toolbar-items>


      <v-toolbar-items>
        <div class="my-2">
            <v-btn
              class="mr-5"
              color="#FFA500"
              dark
            >
              SIGN IN
            </v-btn>

            <v-btn
              color="#F1E1C2"
              dark
            >
              <span class="button_signup">SIGN UP</span>
            </v-btn>
          </div>
      </v-toolbar-items>
        </v-container>
    </v-toolbar>

</template>





<script>
export default {
  data() {
    return {};
  },
};
</script>

<style>

  .b_list{
    text-align: center;
  }

  .v-list-link a{
    text-decoration: none;
    color:#FFA500;
  }

  .nav-menu{
    border-bottom: 3px solid transparent;
    display: flex;
    transition: 0.4s;
    
    background: none!important;
    background-color: none!important;
  }

  .nav-menu:hover{
    background-color:none;
    border-bottom-color: #FFA500;
  }
  .nav-menu span{
    margin-right: 5px;
  }

  .cybernm_link{
    text-decoration: none;
    color:white!important;
  }

  .button_signup{
    color: #FFA500;
  }

  .header_back{
    background: #3A3A3A!important;
  }
  .cybernm_header{
    font-size: 28px!important;
    font-weight: 900;
    color: white;
  }
</style>
