<template>
  <v-container class="pa-0">
    <v-card
      class="d-flex justify-space-between mb-3 disciplines_title"
      flat
      tile
    >
      <h3>TOURNAMENTS</h3>
      <div class="show_all">
        <router-link to="/tournament">
          <a href="">show all</a>
          <fa class="arrow_d" icon="arrow-right" />
        </router-link>
      </div>
    </v-card>

    <ul id="discipline_ul" class="pa-0 discipline_img_ul">
      <li class="discipline_li" v-for="image in disciplineList" :key="image.id">
        <img :src="image.discipline_image" alt="discipline" class="i" />
        <!--router-link :to="" ссылка-->
      </li>
    </ul>

    <div class="">
      <v-card class="mx-auto" tile>
        <v-list dense class="v-lists">
          <div class="subhead">
            <div class="subhead-text">
              <v-subheader>NEWS</v-subheader>
            </div>
            <router-link to="/news" class="news-link">
              <div class="subhead-link">
                <a href="">show all</a>
                <fa class="arrow_n" icon="arrow-right" />
              </div>
            </router-link>
          </div>

          <v-list-item-group color="primary" @click:row="goTo">
            <v-list-item
              class="v-list-items"
              v-for="news in tournamentsList.slice(-5)"
              :key="news.name"
            >
              <v-list-item-icon>
                <v-avatar size="32px">
                  <img :src="news.image" alt="Avatar" />
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
.news-link {
  text-decoration: none !important;
}
.v-lists {
  margin-bottom: 100px;
}

.v-list-items {
  margin-bottom: 10px;
}

.disciplines_title {
  margin-top: 60px;
}

.subhead {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.disciplines_title h3 {
  font-weight: 600;
  font-size: 20px;
}
.show_all a {
  font-weight: 400;
  font-size: 20px;
  text-decoration: none;
  color: #ffb937;
  margin-right: 5px;
}

.subhead-text {
  margin-left: 10px;
}

.subhead-link {
  margin-right: 10px;
}

.subhead-link a {
  font-weight: 400;
  font-size: 16px;
  text-decoration: none;
  color: #ffb937;
  margin-right: 5px;
}

.arrow_n {
  color: #ffb937;
  height: 15px;
}

.arrow_d {
  color: #ffb937;
}
.discipline_img_ul {
  justify-content: center;
}
#discipline_ul {
  margin-top: 30px;
  display: flex;
  flex-wrap: wrap;
}
.discipline_li {
  list-style-type: none;
  margin-bottom: 30px;
}
.discipline_li:nth-of-type(1n) {
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
  name: "Home",

  data: () => ({
    reveal: false,
  }),

  data() {
    return {
      tournamentsList: [],
      disciplineList: [],
    };
  },
  created() {
    this.LoadListTournaments();
  },

  methods: {
    async LoadListTournaments() {
      (this.tournamentsList = await fetch(
        `${this.$store.getters.getServerUrl}Allnews/`
      ).then((response) => response.json())),
        (this.disciplineList = await fetch(
          `${this.$store.getters.getServerUrl}Alldisciplines/`
        ).then((response) => response.json()));
    },

    goTo(item) {
      console.log(news.name);
      this.$router.push({ name: "name", params: { id: news.name } });
    },
  },
};
</script>
