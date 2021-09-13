<template>
  <v-toolbar flat dark class="mb-5 header_back">
    <v-container
      class="pa-0 header_container d-flex justify-space-between align-sm-center"
    >
      <v-toolbar-title class="cybernm_header">
        <router-link to="/" class="cybernm_link">CYBERNM</router-link>
      </v-toolbar-title>
      <v-toolbar-items>
        <v-btn class="nav-menu" text to="/tournament">
          <span>Tournaments</span>
        </v-btn>

        <v-btn class="nav-menu" text to="/player">
          <span>Players</span>
        </v-btn>

        <v-menu offset-y>
          <template v-slot:activator="{ on, attrs }">
            <v-btn class="nav-menu" v-bind="attrs" v-on="on" text>
              <span>MORE</span>
              <fa icon="chevron-down" />
            </v-btn>
          </template>
          <v-list class="b_list">
            <v-list-item>
              <v-list-item-title class="v-list-link"
                ><router-link to="/discipline"
                  >disciplines</router-link
                ></v-list-item-title
              >
            </v-list-item>
            <v-list-item>
              <v-list-item-title class="v-list-link"
                ><router-link to="/news">news</router-link></v-list-item-title
              >
            </v-list-item>
          </v-list>
        </v-menu>
      </v-toolbar-items>

      <div class="profile">
        <div v-if="auth" class="profile d-flex">
          <div class="profile_info">
            <p class="name">{{ username }}</p>
            <p class="post">{{ role }}</p>
          </div>
          <div v-if="username == 'admin'">
            <router-link to="administration" class="linkadmin">
              <v-btn depressed color="orange ml-4 text white--text">
                Admin panel
              </v-btn>
            </router-link>
          </div>
          <v-btn
            depressed
            color="orange ml-4 text white--text"
            @click="logout()"
          >
            Log out
          </v-btn>
        </div>

        <div v-else>
          <v-toolbar-items>
            <div class="my-2">
              <router-link to="/LogIn" class="linksignin"
                ><v-btn class="mr-5" color="#FFA500" dark>
                  SIGN IN
                </v-btn></router-link
              >

              <v-btn color="#F1E1C2" dark>
                <router-link to="/SignUp"
                  ><span class="button_signup">SIGN UP</span></router-link
                >
              </v-btn>
            </div>
          </v-toolbar-items>
        </div>
      </div>
    </v-container>
  </v-toolbar>
</template>

<script>
import $ from "jquery";
export default {
  data() {
    return {
      block: 1,
      username: "",
      role: "",
      auth: true,
    };
  },

  created() {
    this.isLogin();
  },
  methods: {
    async isLogin() {
      let token = localStorage.getItem("auth_token");
      if (token) {
        this.auth;
        $.ajax({
          url: `${this.$store.getters.getServerUrl}auth/users/me`,
          type: "GET",
          headers: {
            Authorization: "Token " + token,
          },
          success: (response) => {
            this.username = response.username;
            if (response.post) this.role = response.post;
            else if (this.username == "admin") this.role = "Admin account";
            else this.role = "Guest";
          },
          error: (response) => {},
        });
      } else {
        this.auth = false;
      }
    },
    logout() {
      localStorage.removeItem("auth_token");
      window.location.replace("/");
    },
  },
};
</script>

<style>
.linkadmin {
  text-decoration: none;
  margin-right: 5px;
}

.name {
  color: #ffa500;
}

.post {
  font-size: 12px;
}

.profile {
  align-items: center !important;
}
.profile_info p {
  margin-bottom: 0px !important;
}
.linksignin {
  text-decoration: none;
}

.b_list {
  text-align: center;
}

.v-list-link a {
  text-decoration: none;
  color: #ffa500;
}

.nav-menu {
  border-bottom: 3px solid transparent;
  display: flex;
  transition: 0.4s;

  background: none !important;
  background-color: none !important;
}

.nav-menu:hover {
  background-color: none;
  border-bottom-color: #ffa500;
}
.nav-menu span {
  margin-right: 5px;
}

.cybernm_link {
  text-decoration: none;
  color: white !important;
}

.button_signup {
  color: #ffa500;
}

.header_back {
  background: #3a3a3a !important;
}
.cybernm_header {
  font-size: 28px !important;
  font-weight: 900;
  color: white;
}
</style>
