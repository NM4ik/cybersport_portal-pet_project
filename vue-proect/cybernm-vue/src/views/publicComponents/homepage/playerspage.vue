<template>
    <v-container>
        <v-card flat>
        <v-card-title class="data_search_input">
            <v-spacer></v-spacer>
            <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Search"
            single-line
            hide-details
            ></v-text-field>
        </v-card-title>
        <v-data-table
            :headers="headers"
            :items="playersList"
            :search="search"    
        >
        <template v-slot:item.player_image="{ item }">
          
          <v-avatar size="36px" tile>
            <img
              :src= "item.player_image"
              alt="Avatar"
            >
          </v-avatar>

        </template>
         <template v-slot:item.Actions="{ item }">
              <v-btn depressed color="primary"
              :to="`/player/${item.nickname}`"
              >
                  go
                </v-btn>
            </template>
        </v-data-table>
        </v-card>
    </v-container>
</template>



<script>
  export default {
    name: 'Players-table',
    data () {
      return {
        search: '',
        headers: [
          {text: 'player_image', value: 'player_image'},
          {text: 'nickname', value: 'nickname'},
          {text: 'discipline', value: 'discipline_name'},
          {text: 'game role', value: 'role'},
          { text: 'Actions', value: 'Actions', sortable: false },
        ],
        playersList: [],
      }
    },

  created(){
    this.LoadListPlayers()
  },

  methods: {

    async LoadListPlayers(){
      this.playersList = await fetch(
        `${this.$store.getters.getServerUrl}Allplayers/`
      ).then(response => response.json())
    },
    goTo(item){
      console.log(item.nickname)
      this.$router.push({name: 'player', params: {id: item.nickname}})
    },
  }
  }
</script>