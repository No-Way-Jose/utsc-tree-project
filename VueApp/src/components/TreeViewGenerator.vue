<template>

  <!-- Container which will hold the tree structure -->
  <v-container>

    <v-row>
      <!-- Left column to display the tree -->
      <v-col cols="9">
        <h3>Tree View Area</h3>
        <!-- Center the diagram -->
        <v-layout justify-center>
          <TreeChart :json="data" />
        </v-layout>
      </v-col>

      <v-divider vertical></v-divider>

      <!-- Right column to display extra information for the courses like prof permission or ORs -->
      <v-col cols="2">
        <h3>Extra Information </h3>
        {{ extrainfo }}
      </v-col>
    </v-row>

  </v-container>

</template>

<script>
// Import axios since using API and TreeChart so we can generate the trees
import TreeChart from 'vue-tree-chart'
import axios from 'axios'

export default {
  name: 'TreeView',
  components: {
    TreeChart
  },
  // Prop so we can get the course from SearchDropBar
  props: {
    info: {
      type: String
    }
  },
  data () {
    return {
      data: {},
      extrainfo: ''
    }
  },
  // Watch when the info gets changed and set var to right course
  watch: {
    info: function () {
      this.extrainfo = this.info
    }
  },
  // Probably going to have to change this to a method once fully implemented
  created () {
    axios.get('http://127.0.0.1:5000/DataRetrieval/CSCA08H3')
      .then(response => {
        // Since Treechart accepts json just assign it straight
        this.data = (response.data)
      })
      // Catch any errors
      .catch(e => {
        this.errors.push(e)
      })
  }
}
</script>

<style scoped>

</style>
