<template>
    <v-container>
        <div class="img_content">

            <ul id="discipline_ul" class="pa-0 discipline_img_ul">
          <li class="discipline_li" v-for="image in disciplineList" :key="image.id" >
           <img :src="image.discipline_image" alt="discipline" class="i">
            <!--router-link :to="" ссылка-->
          </li>
        </ul>

        </div>
    </v-container>
</template>

<style scoped>

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

</style>

<script>
export default {
  name: 'Home',

    data: () => ({
      reveal: false,
    }),

  data() {
    return{
        disciplineList: [],
      }
  },
  created(){
    this.LoadListTournaments()
  },

  methods: {
    async LoadListTournaments(){
      this.disciplineList = await fetch(
        `${this.$store.getters.getServerUrl}Alldisciplines/`
      ).then(response => response.json())
    },
  }

}
</script>
