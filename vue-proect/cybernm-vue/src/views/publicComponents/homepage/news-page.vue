<template>
    <v-container>
        <div class="list">
            <v-card
            class="mx-auto"
            tile
            >
            <v-list dense class="v-lists">
                <v-subheader>NEWS</v-subheader>
                <v-list-item-group
                v-model="selectedItem"
                color="primary" 
                @click:row="goTo"
                >
                <v-list-item class="v-list-items"
                    v-for="news in tournamentsList" :key="news.name"
                >
                    <v-list-item-icon>
                    <v-avatar size="32px">
                        <img :src= "news.image" alt="Avatar">
                    </v-avatar>
                    </v-list-item-icon>
                    <v-list-item-content>
                    <v-list-item-title v-text="news.name"></v-list-item-title>
                    </v-list-item-content>
                    </v-list-item>
                </v-list-item-group>
            </v-list>
            </v-card>
        </div>
    </v-container>
</template>


<style>

  .v-lists{
    margin-bottom: 100px;
  }

  .v-list-items{
    margin-bottom:10px;
  }

  .disciplines_title{
    margin-top: 60px;
  }

  .disciplines_title h3{
    font-weight: 600;
    font-size: 20px;
  }
  .show_all a{
    font-weight: 400;
    font-size: 20px;
    text-decoration: none;
    color: #FFB937;
    margin-right: 5px;
  }
  .arrow_d{
    color: #FFB937;
  }
  .discipline_img_ul{
    justify-content: center;
  }
 #discipline_ul{
    margin-top: 30px;
    display: flex;
    flex-wrap: wrap;
  }
  .discipline_li{
    list-style-type: none;
    margin-bottom: 30px;
  }
  .discipline_li:nth-of-type(1n){
    margin-right: 30px;
  }
  .v-card--reveal {
    bottom: 0;
    opacity: 1 !important;
    position: absolute;
    width: 100%;
  }
</style>


<script>
export default {
  name: 'Home',

    data: () => ({
      reveal: false,

    }),

  data() {
    return{
        tournamentsList: [],
        disciplineList: [],
      }
    
  },
  created(){
    this.LoadListTournaments()
  },

  methods: {
    async LoadListTournaments(){
      this.tournamentsList = await fetch(
        `${this.$store.getters.getServerUrl}Allnews/`
      ).then(response => response.json()),
      this.disciplineList = await fetch(
        `${this.$store.getters.getServerUrl}Alldisciplines/`
      ).then(response => response.json())
    },

  goTo(news){
      console.log(news.name)
      this.$router.push({name: 'name', params: {id: news.name}})
    },

  }

}
</script>
