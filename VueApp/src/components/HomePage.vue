<template>

  <!-- Container to hold all the home page content -->
  <v-container class="home-container">
    <!-- Center the text and wrap it if needed -->
    <v-col class="col-container">
      <v-row>
        <h1 class="heading1">
          A new way <br> to view UTSC courses <br> without all the tabs!
        </h1>
      </v-row>
      <v-row class="spacer"></v-row>
      <v-row>
        <h1 class="heading2">
          Designed by students, for students.
        </h1>
      </v-row>
    </v-col>

  </v-container>
</template>

<script>

export default {
  components: {},
  data: () => ({
    whatsNext: [
      {
        text: 'Explore components',
        href: 'https://vuetifyjs.com/components/api-explorer'
      },
      {
        text: 'Select a layout',
        href: 'https://vuetifyjs.com/layout/pre-defined'
      },
      {
        text: 'Frequently Asked Questions',
        href: 'https://vuetifyjs.com/getting-started/frequently-asked-questions'
      }
    ]
  })
}
</script>

<style scoped>
  @import url('https://fonts.googleapis.com/css?family=Francois+One&display=swap');
  .home-container{
    background: url("../assets/background1.jpeg");
    background-size: cover;
    max-width: 100%;
    height: 93.5vh;
  }

  .heading1{
    font-family: 'Francois One', sans-serif;
    color: whitesmoke;
    padding-right: 3%;
    text-align: center;
    width: 100%;
    font-size: 50px;
  }
  .heading2{
    padding-right: 3%;
    text-align: center;
    font-size: 20px;
    color: whitesmoke;
    width: 100%;
  }
  .spacer{
    height: 30px;
  }
  .col-container{
    padding-left: 62%;
    padding-top: 10%;
  }

</style>
