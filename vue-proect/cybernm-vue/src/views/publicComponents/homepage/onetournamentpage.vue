<template>
    <v-container class="pa-0">
    <div class="main_info">
        <div class="main_img"><v-img 
        
          class="img-tour"
          :src="tournament.tournament_image"
          aspect-ratio="1.4"
        ></v-img></div>

        <div class="card">
            <v-card
            class="ml-15 v-cards"
            elevation="2"
            >
            <v-card-title>tournament: <span>{{tournament.name}}</span></v-card-title>
            <v-card-subtitle>discipline: <span>{{tournament.discipline_id}}</span></v-card-subtitle>
            <v-card-text>
                <ul class="tournament_description">
                    <li>status: <span>{{tournament.status}}</span></li>
                    <li>seats <span>{{tournament.seats_number}}</span></li>
                    <li>limitation: <span>{{tournament.limitation}}</span></li>
                    <li>prize: <span>{{tournament.prize}}</span></li>
                    <li>start date: <span>{{tournament.start_date }}</span></li>
                    <li>end date: <span>{{tournament.end_date }}</span></li>
                </ul>
            </v-card-text>
            <v-card-actions>

                    <v-btn
                        @click="signTournament()"
                        class="mr-5 sign_in"
                        color="#FFA500"
                        dark
                        >
                        SIGN TO TOURNAMENT
                    </v-btn>
            </v-card-actions>
            </v-card>
            
        </div>
       
    </div>
    

    <v-card flat>
        <v-card-title class="data_input">
        </v-card-title>
        <v-data-table
            :headers="headers"
            :items="playersList"
        >
        <template v-slot:item.user_image="{ item }">
          
          <v-avatar size="36px" tile>
            <img
              :src= "item.user_image"
              alt="Avatar"
            >
          </v-avatar>
        </template>
        </v-data-table>
        </v-card>
      
    </v-container>
</template>

<style scoped>

.sign_in{
    margin-left: 24px;
    margin-top: 15px;
}

.data_input{
    margin-top: 60px;
}


.v-card__title{
    font-size: 26px;
}
.v-card__title span{
    margin-left: 10px;
    color: #FFA500;
}

.v-card__subtitle{
    font-size: 18px;
    margin-top: 10px;
}
.v-card__subtitle span{
    color: #FFA500;
}
.tournament_description{
    list-style-type: none;
    font-size: 20px;
}
.tournament_description > li{
    margin-top: 10px;
    color: black;
}
.tournament_description > li span{
    color: #FFA500;
}

.v-cards{
    width: 100vh;
    height: 100%;
}
    .main_info{
        display: flex;
    }
    .img-tour{
        height: 400px;
        width: 400px;
    }
    

</style>

<script>
  export default {
    name: 'onetournamentpage',
    data () {
      return {
        id: this.$route.params['id'],
        tournament: {},
        search: '',
        headers: [
          {text: 'player image', value: 'user_image'},
          {text: 'nickname', value: 'nickname'},
          {text: 'name', value: 'first_name'},
          {text: 'game role', value: 'role'},
        ],
        playersList: [],
      }
    },

  created(){
    //   this.LoadListPlayers()
      this.LoadTournament()

  },
//    watch: {
//       dialog (val) {
//         val || this.close()
//       },
//     },

  methods: {
    //   async LoadListPlayers(){
    //   this.playersList = await fetch(
    //     `${this.$store.getters.getServerUrl}Onetournament/${this.id}`
    //   ).then(response => response.json())
    // },
    async LoadTournament(){
        this.tournament = await fetch(
            `${this.$store.getters.getServerUrl}Onetournament/${this.id}`
        ).then(response => response.json())
        this.playersList = this.tournament.players
        console.log(this.tournament)
        console.log(this.id)
    }, 

    signTournament () {
            let token = localStorage.getItem("auth_token");
            if (token) {
                this.dialog = true
                alert("Your application has been sent")
            } else {
                window.location.replace("/LogIn");
            }
        },
  }
  }
</script>