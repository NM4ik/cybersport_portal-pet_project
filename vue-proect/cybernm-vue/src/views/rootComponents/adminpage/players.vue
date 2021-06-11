<template>
    <v-card flat tile>
       <v-container
       
      class="grey lighten-4"
      fluid
    >
    <div class="new-item">
        <v-dialog
        v-model="dialog"
        width="500"
        >
         <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="#FFA500"
              dark
              v-bind="attrs"
              v-on="on"
              style="margin-bottom: 15px"
            >
              Add new
            </v-btn>
          </template>
          <v-card>
            <v-form @submit.prevent="submitForm"> 
            <v-card-title>
              <span class="text-h5">{{formTitle}}</span>
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
                      label="nickname"
                      v-model="player.nickname"
                    ></v-text-field>
                  </v-col>                
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      label="first name"
                      v-model="player.first_name"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      label="second name"
                      v-model="player.second_name"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="12"
                    md="12"
                  >
                    <v-text-field
                    type="date"
                      label="birth date"
                      v-model="player.birth_date"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      label="city"
                      v-model="player.city"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      label="role"
                      v-model="player.role"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      label="email"
                      v-model="player.email"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      label="social link"
                      v-model="player.social_link"
                    ></v-text-field>
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
            <v-card-title class="text-h5">Are you sure you want to delete this item?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
              <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
        </div>

      <v-row dense>
        <v-spacer></v-spacer>
        <v-col
          cols="12"
          sm="6"
          md="4"
          v-for="card in playersList"
          :key="card.id"
        >
          <v-card>
            <v-img
              :src="card.player_image" alt="player_image"
              height="300px"
            >
               <span
                class="text-h5 orange--text pl-4 pt-4 d-inline-block"
                v-text="card.nickname"
              ></span>
            </v-img>

            <v-card-actions class="white justify-end">
              <v-icon
                class="mr-3"
                @click="editItem(card)"
              >
                mdi-pencil
              </v-icon>
              <v-icon
                @click="deleteItem(card)"
              >
                mdi-delete
              </v-icon>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    </v-card>
</template>

<style scoped>
.new-item{
  display: flex;
  justify-content: flex-end;
}
</style>

<style>
  .image_upload{
    margin: auto;
  }
  .inputfile{
    width: 0.1px;
    height: 0.1px;
    opacity: 0;
    overflow: hidden;
    position: absolute;
    z-index: -1;
  } 
</style>


<script>
  export default {  
    
    data () {
      return{
        dialog: false,
        dialogDelete: false,
        playersList: [],
        player: {
          nickname: '',
          first_name: '',
          //player_image: '',
          second_name: '',
          birth_date: '',
          city: '',
          role: '',
          email: '',
          social_link: '',
        },
        defaultItem: {
          nickname: '',
          first_name: '',
          //player_image: '',
          second_name: '',
          birth_date: '',
          city: '',
          role: '',
          email: '',
          social_link: '',
        },
      }
    },

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'New player' : 'Edit player'
      },
    },

    created(){
      this.LoadListPlayers()
    },

    watch: {
      dialog (val) {
        val || this.close()
      },
      dialogDelete (val) {
        val || this.closeDelete()
      },
    },

    methods: {

      async LoadListPlayers(){
        this.playersList = await fetch(
          `${this.$store.getters.getServerUrl}Allplayers/`
        ).then(response => response.json())
      },
      editItem (card) {
            this.editedIndex = this.playersList.indexOf(card)
            this.player = Object.assign({}, card)
            this.dialog = true
        },

      deleteItem (card) {
            this.editedIndex = this.playersList.indexOf(card)
            this.player = Object.assign({}, card)
            this.dialogDelete = true
        },

      async deleteItemConfirm () {
            await this.LoadListPlayers();
            await fetch(
                `${this.$store.getters.getServerUrl}Deleteplayer/${this.player.nickname}/`,
                {
                  method: 'delete',
                  headers: {
                      'Content-Type': 'application/json'
                  },
                  body: JSON.stringify(this.player)
                }
            );
            await this.LoadListPlayers();
            this.closeDelete()
        },

      close () {
            this.dialog = false
            this.$nextTick(() => {
            this.player = Object.assign({}, this.defaultItem)
            this.editedIndex = -1
            })
        },

        closeDelete () {
            this.dialogDelete = false
            this.$nextTick(() => {
            this.player = Object.assign({}, this.defaultItem)
            this.editedIndex = -1
            })
        },

      async submitForm() {
            await this.LoadListPlayers();
            if (this.editedIndex > -1) {
              this.editPlayer();              
            } else {
              this.addPLayer();
            }
            this.close()
        },

      async addPLayer ()  { 
          await fetch(
              `${this.$store.getters.getServerUrl}Addplayer/`,
              {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.player)
              }
          );
          await this.LoadListPlayers();
        },
  
        async editPlayer () {
          await fetch(
              `${this.$store.getters.getServerUrl}Updateplayer/${this.player.nickname}/`,
              {
                method: 'put',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.player)
              }
          );
          await this.LoadListPlayers();
        },
    }
  }
</script>