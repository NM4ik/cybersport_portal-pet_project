<template>
    <v-container>
        <v-card>
            <v-card-title>
            Tournaments
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
            :items="tournamentsList"
            class="elevation-1"
            :search="search"
            @click:row="goTo"
            >

            <template v-slot:item.status="{ item }">
              <v-chip
                :color="getColor(item.status)"
                dark
              >
                {{item.status}}
              </v-chip>
            </template>
            
            
            <template v-slot:item.tournament_image="{ item }">  
                <v-avatar size="48px" >
                    <img :src= "item.tournament_image" alt="Avatar">
                </v-avatar>
            </template>
            <template v-slot:item.tournament_id="{ item }">
              <v-btn depressed color="primary"
              :to="`/tournament/${item.tournament_id}`"
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
    name: 'Tournaments-table',
    data () {
      return {
        search: '',
        headers: [
          {text: 'icon', value: 'tournament_image'},
          {text: 'status', value: 'status'},
          {text: 'discipline', value: 'discipline_id'},
          {text: 'name', value: 'name'},
          {text: 'limitation', value: 'limitation'},
          {text: 'start_date', value: 'start_date'},
          { text: 'Actions', value: 'tournament_id', sortable: false },
        ],
        tournamentsList: [],
        DisciplineList: [],
      }
    },

  created(){
    this.LoadListtournament()
    this.LoadDisciplines()
  },

  methods: {

     getColor (status) {
        if (status == 'announced') return 'orange'
        else if (status == 'run') return 'green'
        else return 'red'
      },
  
    async LoadListtournament(){
      this.tournamentsList = await fetch(
        `${this.$store.getters.getServerUrl}Alltournaments/`
      ).then(response => response.json())
    },
    goTo(item){
      console.log(item.tournament_id)
      this.$router.push({name: 'tournament', params: {id: item.tournament_id}})
    },
},
  }
</script>