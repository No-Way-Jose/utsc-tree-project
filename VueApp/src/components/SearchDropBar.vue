<template>
  <!-- Container to hold the search bar component -->
  <v-container class="search-bar">
    <model-select
      ref="select"
      :options="options"
      v-model="item"
      placeholder="Enter or select a course ..."
    >
    </model-select>
  </v-container>

</template>

<script>
// Import the search bar module and axios
import { ModelSelect } from 'vue-search-select'
import axios from 'axios'

export default {
  name: 'SearchDropBar',
  data () {
    return {
      options: [],
      item: ''
    }
  },
  components: {
    ModelSelect
  },
  // Watch the item variable so we can call the method to send the selected course
  watch: {
    // Emit the data when it has been changed so TreeViewGenerator knows what to show
    item: function () {
      this.$emit('inputData', this.item)
    }
  },
  // Use axios for API call when page loads to load upt he data into the search bar
  created () {
    axios.get('http://127.0.0.1:5000/DataRetrieval/courses')
      .then(response => {
        // Run a loop to append the data
        for (let course in response.data) {
          this.options.push(response.data[course])
        }
      })
      // Catch any errors
      .catch(e => {
        this.errors.push(e)
      })
  }

}
</script>

<style scoped>
  .search-bar{
    min-width: 150px;
  }

</style>
