<template>
  <!-- Container to hold the directory and course information -->
  <v-container class="container">
    <v-row >
      <v-col class="dirSide">
        <v-text-field
          v-model="search"
          label="Search for a course ..."
          hint="Ex. 'CSCA08H3' or 'Elementary Musicianship I'"
          flat
          clearable
          class="courseSearch"
        ></v-text-field>
        <!-- Tree view section with its attributes/qualities  -->
        <v-treeview
          open-all
          :items=items
          return-object
          hoverable
          dense
          activatable
          open-on-click
          transition
          color="warning"
          rounded
          :search="search"
          :filter="filter"
          :open.sync="open"
        >
          <!-- This template allows for events on every course so can bring up course info when clicked -->
          <template slot="label" slot-scope="{ item }">
            <a @click="getCourseInfo(item)">{{ item.name }}</a>
          </template>
          <template v-slot:prepend="{ item }">
            <v-icon
              v-if="item.children"
              v-text="`mdi-${item.id === 1}`"
            ></v-icon>
          </template>
        </v-treeview>
      </v-col>

      <v-divider vertical></v-divider>

      <!-- Right column to hld the course information -->
      <v-col class="pa-6" cols="6">
        <template>
          <!-- If they've clicked a course display the information -->
          <div v-if="courseInfo.name !== 'Select a course to view more information ...'">
            <h1>{{ courseInfo.name }}</h1>
            <br><br>
            <h2>Course Information:</h2>
            {{ courseInfo.desc }}
            <br><br>
            <h2>Prerequisites:</h2>
            {{ courseInfo.pre }}
            <br><br>
            <h3>Exclusions:</h3>
            {{ courseInfo.excl }}
            <br><br>
            <h3>Student Limit:</h3>
            {{ courseInfo.limit }}
            <br><br>
            <h3>Breadth Requirement:</h3>
            {{ courseInfo.breadth }}
          </div>
          <!-- If they haven't selected a course output a default message-->
          <div v-else class="emptyInfo">
            <v-layout>
              <v-col>
                <h2>Ooops Nothing to see here <br> {{ courseInfo.name }}</h2>
                <v-img src="../assets/Oops.png" height="300" width="300"></v-img>
              </v-col>
            </v-layout>
          </div>
        </template>
      </v-col>

    </v-row>

  </v-container>

</template>

<script>
// Import axios since using APIs to fetch data
import axios from 'axios'
export default {
  data: () => ({
    // Course info object
    courseInfo: { name: 'Select a course to view more information ...',
      desc: '',
      pre: '',
      excl: '',
      limit: '',
      breadth: '' },
    // Treeview course data
    items: [],
    open: [1, 2],
    search: null,
    caseSensitive: false
  }),
  // API call upon creation to populate the course directory
  created () {
    axios.get('http://127.0.0.1:5000/DataRetrieval/directory')
      .then(response => {
        // Run a loop to append the data
        for (let section in response.data) {
          this.items.push(response.data[section])
        }
      })
      // Catch any errors
      .catch(e => {
        this.errors.push(e)
      })
  },
  // Filter for search functionality
  filter () {
    return this.caseSensitive
      ? (item, search, textKey) => item[textKey].indexOf(search) > -1
      : undefined
  },
  methods: {
    // This method will create an API call to get the info related to the course and update the variable
    getCourseInfo: function (courses) {
      // Array to store course letters to check if they clicked on a course or no
      let alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'W']
      // If they clicked on a letter or category and not a course output a default message
      if ((alphabet.includes(courses.name)) || !(courses.name.match(/[A-Z]{4}[0-9]{2}[A-Z][0-9]/))) {
        this.courseInfo.name = 'Select a course to view more information ...'
      } else {
        // If they actually clicked a course use API call passing in course to get its info
        let url = 'http://127.0.0.1:5000/DataRetrieval/courseInfo/' + courses.name
        axios.get(url)
          .then(response => {
            let info = (response.data)
            // Fill the object with the course information to output
            this.courseInfo.name = courses.name
            this.courseInfo.desc = info.desc
            this.courseInfo.pre = info.pre
            this.courseInfo.excl = info.ex
            this.courseInfo.limit = info.limit
            this.courseInfo.breadth = info.breadth
          })
          // Catch any errors
          .catch(e => {
            this.errors.push(e)
          })
      }
    }
  }
}

</script>

<style scoped>
  .dirSide{
    height: 83vh;
    overflow-y: auto;
  }
  .container{
    max-width: 95%;
  }
  .courseSearch{
    max-width: 90%;
  }

  .emptyInfo{
    text-align: center;
    height: 50%;
  }
</style>
