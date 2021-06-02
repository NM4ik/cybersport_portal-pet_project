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
            <v-card-title>
              <span class="text-h5">{{ formTitle }}</span>
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
                      label="Dessert name"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      label="Calories"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      label="Fat (g)"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      label="Carbs (g)"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      label="Protein (g)"
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
                @click="save"
              >
                Save
              </v-btn>
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
                @click="editItem(item)"
              >
                mdi-pencil
              </v-icon>
              <v-icon
                @click="deleteItem(item)"
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
</style>


<script>
  export default {
    data: () => ({
      dialogDelete: false,
    }),
  
    name: 'admin_discipline',
    data () {
      return {
        dialog: false,
        id: this.$route.params['id'],
        discipline: {},
        search: '',
        cards: [
          {title: 'discipline_name', flex: 6},
        ],
        disciplineList: [],
      }
    },

   computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
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

  created(){
    //   this.LoadListPlayers()
      this.LoadDisciplines()
  },

  methods: {
    //   async LoadListPlayers(){
    //   this.playersList = await fetch(
    //     `${this.$store.getters.getServerUrl}Onetournament/${this.id}`
    //   ).then(response => response.json())
    // },
    async LoadDisciplines(){
        this.disciplineList = await fetch(
            `${this.$store.getters.getServerUrl}Alldisciplines/`
        ).then(response => response.json())
        console.log(this.discipline)
        console.log(this.id)
    },

      close () {
        this.dialog = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      save () {
        if (this.editedIndex > -1) {
          Object.assign(this.desserts[this.editedIndex], this.editedItem)
        } else {
          this.desserts.push(this.editedItem)
        }
        this.close()
      },
  }
  }
</script>