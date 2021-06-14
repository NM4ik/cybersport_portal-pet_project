<template>
    <v-container>


    <v-card
    class="mx-auto"
    style="max-width: 500px;
    background-color: #585858;
    "
    dark
    >
    <h1 class="h1Login"
    >Sign Up</h1>
    <v-form
      ref="form"
      class="pa-4 pt-6"
    >

      <v-text-field
        style="border-radius: 10px;
        border-style:none!important;
        "
        color="deep-orange"
        v-model="username"
        filled
        label="Username"
        required
      ></v-text-field>
        <v-text-field
        v-model="nickname"
        filled
        color="deep-orange"
        label="game nickname"
        required
      ></v-text-field>
      <v-text-field
        v-model="password"
        filled
        color="deep-orange"
        label="password"
        style="border-radius: 10px;"
        type="password"
        required
      ></v-text-field>

    </v-form>
    <v-card-actions
         style="
        display:flex;
        justfy-content: center;
        align-items: center;
        flex-direction: column;
        "
    >
      <v-btn
        @click="setSignup()"
        class="white--text"
        color="#FFA500"
        depressed
        style="width: 470px;
        height: 45px;
        margin-bottom: 15px;
        display:flex;
        justfy-content: center;
        align-items: center;
        border-radius: 10px;
        "
      >
        signup
      </v-btn>
    </v-card-actions>
    <a href="/LogIn">Are you already registered? LogIn</a>
    </v-card> 
    </v-container>
</template>

<style>
  .v-text-field > .v-input__control > .v-input__slot:before, .v-text-field > .v-input__control > .v-input__slot:after{
    content: none!important;
  }
</style>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Lexend+Deca&display=swap');
 *{
    font-family: 'Lexend Deca', sans-serif!important;
  }

.h1Login{
    margin-top: 30px;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding-top: 10px;
}
a {
    color: "deep-orange";
    text-decoration: none;
    font-size: 14px;
  }

</style>


<script>
  import $ from 'jquery'
  export default {
    name: 'Signup',

    data: () => ({
      username: undefined,
      nickname: undefined,
      password: undefined,
    }),


    methods: {
      async setSignup() {
        let users = await fetch(
            `${this.$store.getters.getServerUrl}Allplayers/`
        ).then(response => response.json())
        this.user_id = users['length'] + 1;
        $.ajax({
          url: `${this.$store.getters.getServerUrl}auth/users/`,
          type: "POST",
          data: {
            username: this.username,
            nickname: this.nickname,
            password: this.password,
          },
          success: (response) => {
            window.location.replace("/login");
          },
          error: (response) => {
              alert("Ошибка");
          }
        })
      }
    }
  }
</script>