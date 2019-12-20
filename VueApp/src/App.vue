<template>
  <v-app>

    <v-app-bar app>
      <v-img
        src="https://upload.wikimedia.org/wikipedia/en/thumb/0/04/Utoronto_coa.svg/1200px-Utoronto_coa.svg.png"
        aspect-ratio="1"
        max-width="50"
        max-height="50"
      ></v-img>
      <v-toolbar-title class="headline">
        <span>UTSC</span>
        <span class="font-weight-light"> Course Tree</span>
      </v-toolbar-title>

      <v-toolbar-items>
         <navbar></navbar>
      </v-toolbar-items>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn text>Login</v-btn>
      </v-toolbar-items>
    </v-app-bar>

    <v-content>
      <router-view></router-view>
    </v-content>

  </v-app>

</template>

<script>

import NavBar from '@/components/NavBar.vue'

export default {
  name: 'App',
  components: {
    'navbar': NavBar
  },
  data: () => ({
    //
  })
}
</script>

<style>

</style>
