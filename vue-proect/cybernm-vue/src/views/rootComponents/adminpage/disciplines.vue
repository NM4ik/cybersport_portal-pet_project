<template>
    <v-container fluid>
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
                  <!-- <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      type="number"
                      label="ID discipline"
                      v-model="discipline.discipline_id"
                    ></v-text-field>
                  </v-col> -->
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >   
                     <v-text-field
                      label="Discipline name"
                      v-model="discipline.discipline_name"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      type="number"
                      label="match seatsnumber  "
                      v-model="discipline.match_seatsnumber"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-autocomplete
                      label="Type"
                      v-model="discipline.type"
                      :items="types"
                    ></v-autocomplete>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-textarea
                      class="desc-area"
                      solo
                      rows="1"
                      name="input-7-4"
                      label="Description"
                      v-model="discipline.description"
                    ></v-textarea>
                  </v-col>
                  <!-- <v-col class="image_upload"
                    cols="12"
                    sm="12"
                    md="8">
                    <v-text-field
                      type="file"
                      label="image"
                      v-model="discipline.discipline_image"
                    ></v-text-field>
                   <input type="file" name="file" id="file" class="inputfile">
                    <v-btn type="submit" class="ma-2" color="info"><label for="file">Download image</label></v-btn> 
                  </v-col>  -->
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
        <v-col
          v-for="card in disciplineList"
          :key="card.id"
          :cols="card.flex"
        >
          <v-card>
            <v-img
              :src="card.discipline_image" alt="discipline" class="i white--text align-end"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
              height="200px"
            >
              <v-card-title v-text="card.discipline_name"></v-card-title>
            </v-img>
            <v-card-actions>
              <v-spacer></v-spacer>

              <v-icon
                class="mr-2"
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
</template>

<style scoped>
  .new-item{
    display: flex;
    justify-content: flex-end;
  }

  .desc-area{
    width: 500px!important;
  }
</style>
<style>
  .desc-area .v-input__slot{
    width: 270px!important;
  }
</style>

<script>
  export default {
    data ()  {
     return {
        uploadFile: [],
        dialog: false,
        dialogDelete: false,
        disciplineList: [],
        editedIndex: -1,
        types: ['strategy', 'shooter', 'simulator'],

        discipline: {
            discipline_id: 0,
            discipline_name: '',
            //discipline_image: '',
            match_seatsnumber: '',
            seats_number: 0,
            type: '',
            description: '',
        },
        defaultItem: {
          discipline_id: 0,
          discipline_name: '',
          //discipline_image: '',
          match_seatsnumber: '',
          seats_number: 0,
          type: '',
          description: '',
        },
      }},

   
    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'New discipline' : 'Edit discipline'
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
      this.LoadListDiscipline();
    },

    methods: {
      async LoadListDiscipline(){
        this.disciplineList = await fetch(
          `${this.$store.getters.getServerUrl}Alldisciplines/`
        ).then(response => response.json())
      },

      editItem (card) {
            this.editedIndex = this.disciplineList.indexOf(card)
            this.discipline = Object.assign({}, card)
            this.dialog = true
        },

      deleteItem (card) {
            this.editedIndex = this.disciplineList.indexOf(card)
            this.discipline = Object.assign({}, card)
            this.dialogDelete = true
        },

      async deleteItemConfirm () {
            await this.LoadListDiscipline();
            await fetch(
                `${this.$store.getters.getServerUrl}Deletediscipline/${this.discipline.discipline_id}/`,
                {
                  method: 'delete',
                  headers: {
                      'Content-Type': 'application/json'
                  },
                  body: JSON.stringify(this.discipline)
                }
            );
            await this.LoadListPlayers();
            this.closeDelete()
        },

      close () {
            this.dialog = false
            this.$nextTick(() => {
            this.discipline = Object.assign({}, this.defaultItem)
            this.editedIndex = -1
            })
        },

        closeDelete () {
            this.dialogDelete = false
            this.$nextTick(() => {
            this.discipline = Object.assign({}, this.defaultItem)
            this.editedIndex = -1
            })
        },

      async submitForm() {
        switch(this.discipline.type) {
          case 'strategy':
            this.discipline.type = 'st'
            break;
          case 'shooter':
            this.discipline.type = 'sh'
            break;
          case 'simulator':
            this.discipline.type = 'sm'
            break;
        }
            await this.LoadListDiscipline();
            if (this.editedIndex > -1) {
              this.editDiscipline();              
            } else {
              this.addDiscipline();
            }
            this.close()
        },

      async addDiscipline ()  { 
          await fetch(
              `${this.$store.getters.getServerUrl}Adddiscipline/`,
              {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.discipline)
              }
          );
          await this.LoadListDiscipline();
        },
  
        async editDiscipline () {
          
          await fetch(
              `${this.$store.getters.getServerUrl}Updatediscipline/${this.discipline.discipline_id}/`,
              {
                method: 'put',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.discipline)
              }
          );
          await this.LoadListDiscipline();
        }
    },
  }
</script>