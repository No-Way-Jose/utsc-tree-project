<template>

  <!-- Container to hold the tree view structure -->
  <v-container class="container">
    <!-- Header -->
    <h1 class="heading">Course TreeView</h1>
    <!-- Search bar so they can select or search a course to view -->
    <SearchBar class="searchContainer" @inputData="updateExInfo"></SearchBar>
    <!-- Bottom row which will house the tree diagram and extra info panel -->
    <v-row>
      <TreeStructure :info="extraCourseInfo"></TreeStructure>
    </v-row>
  </v-container>

</template>

<script>
// Import the components that we are using in the view
import TreeStructure from '@/components/TreeViewGenerator.vue'
import SearchBar from '@/components/SearchDropBar.vue'

export default {
  name: 'TreeView',
  components: {
    TreeStructure,
    SearchBar
  },
  data: function () {
    return {
      extraCourseInfo: ''
    }
  },
  // Update info method so TreeViewGenerator knows when SearchDropBar changes course
  methods: {
    updateExInfo (variable) {
      this.extraCourseInfo = variable
    }
  }
}

</script>

<style scoped>
  .heading{
    padding-left: 50%;
    padding-top: 5px;
    margin-left: -125px;
  }
  .container{
    max-width: 95%;
  }
  .searchContainer{
    max-width: 50%;
  }

</style>
