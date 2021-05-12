<template>
  <div id="app">
    <input type="text" @keyup.enter="onEnter" v-model="content">
  </div>
</template>

<script>

export default {
  name: 'App',
  data: function () {
    return {
      content: '',
    }
  },
  methods: {
    onEnter: function () {
      this.$store.dispatch('addTodo', this.content)
    }
  },
  components: {
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
