<template>
  <div id="MainApp">
    <!-- <img src="./assets/logo.png"> -->
    <router-view />
  </div>
</template>

<script>
  export default {
    name: 'App',
    data() {
      return {

      }
    }
  }
</script>

<style>
  html,
  body,
  #MainApp {
    height: 100%;
  }

  #MainApp {
    width: 100%;
    height: 100%;
    background-repeat: no-repeat;
    background-position: center;
    background-image: url(./assets/bg.jpg);
    background-size: cover;
  }

  /* #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  } */
</style>
