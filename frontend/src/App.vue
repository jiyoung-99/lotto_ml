<template>
  <div id="app">
    <header>
      <Navbar/>
    </header>
    
    <router-view/>
  </div>
</template>
<script>
import Navbar from './components/Navbar'


export default {
  name: 'App',
  components: {
    Navbar
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #3b3b3b;
  display: flex;
  flex-direction: column;
  background-image: linear-gradient(110deg, #ffffff, #ffffff);
  min-height: 100vh;
}
</style>
