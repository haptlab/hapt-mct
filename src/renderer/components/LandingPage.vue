<template>
  <div id="wrapper">
    <button class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent">
      Button
    </button>
    <!--img id="logo" style="width: 100px" src="~@/assets/logo.png" alt="electron-vue"-->
  </div>
</template>

<script>
  export default {
    components: {},
    methods: {
      open (link) {
        this.$electron.shell.openExternal(link)
      }
    }
  }
</script>

<style lang="scss">
  @import url('https://fonts.googleapis.com/css?family=Source+Sans+Pro');
</style>
