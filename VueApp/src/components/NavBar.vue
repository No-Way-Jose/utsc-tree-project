<template>
  <!-- Nav bar that contains a list of the router links -->
  <nav>
    <ul>
      <li><router-link exact to="/">Home</router-link></li>
      <li><router-link exact to="/courses">Courses</router-link></li>
      <li><router-link exact to="/treeview">TreeView</router-link></li>
      <li><router-link exact to="/information">Information</router-link></li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'NavBar'
}
</script>

<style scoped>
  ul{
    list-style-type: none;
    text-align: center;
    margin: 0;
  }
  li{
    display: inline-block;
    margin: 0 10px;
    color: black;
  }
  a{
    color: black;
    text-decoration: none;
    padding: 6px 8px;
    font-size: 20px;
    border-radius: 10px;
  }
  nav{
    background: transparent;
    padding: 17px 0;
    border-radius: 50px;
  }

  .router-link-active{
    border-bottom: 3px solid skyblue;
    border-radius: 2px;
    color: skyblue;
  }

</style>
