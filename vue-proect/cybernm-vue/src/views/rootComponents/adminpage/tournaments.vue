<template>
<v-container>
  <v-card-title>
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
    sort-by="discipline_id"
    class="elevation-0"
    :search="search"
  >

    <template v-slot:item.tournament_image="{ item }">  
      <v-avatar size="48px" tile>
          <img :src= "item.tournament_image" alt="Avatar">
      </v-avatar>
    </template>  
    <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-spacer></v-spacer>
        <v-dialog
          v-model="dialog"
          max-width="500px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="primary"
              dark
              class="mb-2"
              v-bind="attrs"
              v-on="on"
            >
              New tournament
            </v-btn>
          </template>
         <v-card ref="form">
            <v-form @submit.prevent="submitForm"> 
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      type="number"
                      ref="tournament_id"
                      label="ID tournament"
                      v-model="tournament.tournament_id"
                    ></v-text-field>
                  </v-col>
                   <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      label="Name"
                      v-model="tournament.name"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                     <v-autocomplete
                        label="status"
                        v-model="tournament.status"
                        :items="statuses"
                      ></v-autocomplete>
                  </v-col>
                 
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      type="number"
                      label="Seats number"
                      v-model="tournament.seats_number"
                    ></v-text-field>
                  </v-col>
                  <v-col
                  >
                    <v-textarea
                      class="desc-area"
                      solo
                      rows="1"
                      name="input-7-4"
                      label="Prize"
                      v-model="tournament.prize"
                    ></v-textarea>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-autocomplete
                        label="Limitation"
                        v-model="tournament.limitation"
                        :items="limitations"
                      ></v-autocomplete>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      type="date"
                      label="Start date"
                      v-model="tournament.start_date"
                    ></v-text-field>
                  </v-col>
                  <v-col
                  >
                    <v-text-field
                      type="date"
                      label="End date"
                      v-model="tournament.end_date"
                    ></v-text-field>
                  </v-col>

                  

                  <v-col
                  cols="12"
                    sm="6"
                    md="4">
                    <v-text-field
                      type="number"
                      v-model="tournament.discipline_id"
                      label="Discipline"
                    ></v-text-field>
                    <!-- <v-autocomplete
                        v-model="tournament.discipline_id"
                        label="Discipline"
                        :items="tournament.discipline_id"
                      ></v-autocomplete> -->
                  </v-col>
                  <v-col>
                  <v-text-field
                      type="number"
                      v-model="tournament.employee_id"
                      label="Employee"
                    ></v-text-field>
                    <!-- <v-autocomplete
                      type="number"
                      v-model="tournament.employee_id"
                      label="Employee"
                    ></v-autocomplete> -->
                  </v-col>

                  <!-- <v-col class="image_upload"
                  cols="12"
                    sm="12"
                    md="8">
                    <v-text-field
                      type="file"
                      label="image"
                      v-model="tournament.tournament_image"
                    ></v-text-field>
                    <input type="file" name="file" id="file" class="inputfile">
                    <v-btn type="submit" class="ma-2" color="info"><label for="file">Download image</label></v-btn> 
                  </v-col>  -->

                  <v-col
                    cols="12"
                    sm="12"
                    md="12">
                    <v-autocomplete
                      label="players"
                      clearable
                      deletable-chips
                      multiple
                      small-chips
                      v-model="tournament.players"
                      :items="playersList"
                    ></v-autocomplete>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="blue darken-1"
                text
                @click="close"
              >
                Cancel
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                type="submit"
              >
                Save
              </v-btn>
            </v-card-actions>
            </v-form>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="headline">Are you sure you want to delete?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
              <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:item.actions="{ item }">
      <v-icon
        small
        class="mr-2"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
      <v-icon
        small
        @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
    </template>
  </v-data-table>

</v-container>
</template>

<style scoped>

</style>


<script>
  export default {
    name: 'Tournaments-table',

    data ()  {
     return {
        dialog: false,
        dialogDelete: false,
        search: '',
        headers: [
          {text: 'icon', value: 'tournament_image'},
          {text: 'status', value: 'status'},
          {text: 'discipline', value: 'discipline_id'},
          {text: 'name', value: 'name'},
          {text: 'limitation', value: 'limitation'},
          {text: 'start_date', value: 'start_date'},
          {text: 'Actions', value: 'actions', sortable: false },
        ],
        tournamentsList: [],
        playersList: [],
        due: null,
        editedIndex: -1,
        statuses: ['анонсирован', 'проводится', 'закончен'],
        limitations: ['1-5lvl', '5-8lvl', '8-10lvl'],

        tournament: {
            tournament_id: 0,
            status: '',
            //tournament_image: '',
            name: '',
            seats_number: 0,
            prize: '',
            limitation: '',
            start_date: '',
            end_date: '',
            discipline_id: 0,
            employee_id: 0,
            players: [],
        },

        defaultItem: {
            tournament_id: 0,
            status: '',
            //tournament_image: '',
            name: '',
            seats_number: 0,
            prize: '',
            limitation: '',
            start_date: '',
            end_date: '',
            discipline_id: 0,
            employee_id: 0,
            players: [],
        },
      }},

   
    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'New tournament' : 'Edit tournament'
      },
    },

    watch: {
      dialog (val) {
        val || this.close()
      },
      dialogDelete (val) {
        val || this.closeDelete()
      },
    },

    created () {
      this.LoadListPlayers();
      this.LoadPlayers();
    },

    methods: {
      async LoadListPlayers(){
        this.tournamentsList = await fetch(
          `${this.$store.getters.getServerUrl}Alltournaments/`
        ).then(response => response.json())
      },
      async LoadPlayers(){
        let players = await fetch(
          `${this.$store.getters.getServerUrl}nicknames`
        ).then(response => response.json());
        let i = 0
        players.forEach(element => {
          this.playersList[i] = element.nickname
          i++
        });
      },



      editItem (item) {
            this.editedIndex = this.tournamentsList.indexOf(item)
            this.tournament = Object.assign({}, item)
            this.dialog = true
        },

      deleteItem (item) {
            this.editedIndex = this.tournamentsList.indexOf(item)
            this.tournament = Object.assign({}, item)
            this.dialogDelete = true
        },

      async deleteItemConfirm () {
            await this.LoadListPlayers();
            await fetch(
                `${this.$store.getters.getServerUrl}Deletetournament/${this.tournament.tournament_id}/`,
                {
                  method: 'delete',
                  headers: {
                      'Content-Type': 'application/json'
                  },
                  body: JSON.stringify(this.tournament)
                }
            );
            await this.LoadListPlayers();
            this.closeDelete()
        },

      close () {
            this.dialog = false
            this.$nextTick(() => {
            this.tournament = Object.assign({}, this.defaultItem)
            this.editedIndex = -1
            })
        },

        closeDelete () {
            this.dialogDelete = false
            this.$nextTick(() => {
            this.tournament = Object.assign({}, this.defaultItem)
            this.editedIndex = -1
            })
        },

      async submitForm() {
        switch(this.tournament.limitation) {
          case '1-5lvl':
            this.tournament.limitation = 'f15'
            break;
          case '5-8lvl':
            this.tournament.limitation = 'f58'
            break;
          case '8-10lvl':
            this.tournament.limitation = 'f810'
            break;
        }
        
        switch(this.tournament.status) {
          case 'анонсирован':
            this.tournament.status = 'a'
            break;
          case 'проводится':
            this.tournament.status = 'r'
            break;
          case 'закончен':
            this.tournament.status = 'e'
            break;
        }


            await this.LoadListPlayers();
            if (this.editedIndex > -1) {
                      
          
          console.log(this.tournament.players)
          console.log(this.playersList)
              this.editTournament();              
            } else {
              this.addTournament();
            }
            this.close()
        },

      async addTournament () {
        
          await fetch(
              `${this.$store.getters.getServerUrl}Addtournament/`,
              {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.tournament)
              }
          );
          await this.LoadListPlayers();
        },
        
  
        async editTournament () {
          // console.log(this.tournament)
          await fetch(
              `${this.$store.getters.getServerUrl}Updatetournament/${this.tournament.tournament_id}/`,
              {
                method: 'put',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.tournament)
              }
          );
          await this.LoadListPlayers();
          this.stusent = {};
        }
    },
  }
</script>