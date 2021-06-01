<template>
    <v-container class="pa-0">
    <div class="main_info">
        <div class="main_img"><v-img 
        
          class="img-tour"
          src="https://picsum.photos/510/300?random"
          aspect-ratio="1.4"
        ></v-img></div>

        <div class="card">
            <v-card
            class="ml-15 v-cards"
            elevation="2"
            >
            <v-card-title>player:<span>{{ player.nickname }}</span></v-card-title>
            <v-card-subtitle>discipline: <span>{{ player.discipline_name }}</span></v-card-subtitle>
            <v-card-text>
                <ul class="tournament_description">
                    <li>first_name: <span>{{ player.first_name }}</span></li>
                    <li>second_name <span>{{ player.second_name }}</span></li>
                    <li>birth_date: <span>{{ player.birth_date }}</span></li>
                    <li>city: <span>{{ player.city }}</span></li>
                    <li>role: <span>{{ player.role }}</span></li>
                    <li>email: <span>{{ player.email }}</span></li>
                </ul>
            </v-card-text>
            <v-card-actions>
                <v-btn
                    class="mr-5 sign_in"
                    color="#FFA500"
                    dark
                    >
                    SIGN IN
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
            :items="tournamentsList"
            @click:row="goTo"
        >
        <template v-slot:item.tournament_image="{ item }">
          
          <v-avatar size="36px" tile>
            <img
              :src= "item.tournament_image"
              alt="Avatar"
            >
          </v-avatar>

        </template>

        <template v-slot:item.Actions="{ item }">
              <v-btn depressed color="primary"
              :to="`/tournament/${item.tournament_id}`"
              >go
            </v-btn>

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
    name: 'onetplayerpage',
    data () {
      return {
        id: this.$route.params['id'],
        player: {},
        search: '',
        headers: [
          {text: 'icon', value: 'tournament_image'},
          {text: 'name', value: 'name'},
          {text: 'prize', value: 'prize'},
          {text: 'limitation', value: 'limitation'},
          {text: 'seats_num', value: 'seats_number'},
          {text: 'start_date', value: 'start_date'},
          { text: 'Actions', value: 'Actions', sortable: false },
        ],
        tournamentsList: [],
      }
    },

  created(){
      this.LoadPlayer()
  },

  methods: {
    //   async LoadLisTournament(){
    //   this.tournamentsList = await fetch(
    //     `${this.$store.getters.getServerUrl}Alltournaments/`
    //   ).then(response => response.json())
    // },
    async LoadPlayer(){
        this.player = await fetch(
            `${this.$store.getters.getServerUrl}Oneplayer/${this.id}`
        ).then(response => response.json())
        this.tournamentsList = this.player.tournament_player
        console.log(this.player)
        console.log(this.id)
    },
  }
  }
</script>