<template>
  <div id="BaseHeader">
    <h1>
      <slot name="header">赫尔墨斯工具</slot>
    </h1>
  </div>
</template>

<script>
  export default {
    name: 'Header',
    data() {
      return {

      }
    },
    props: {

    },
    created() {},
    mounted() {
      // this.setDefaultValue();
    },
    methods: {

    }
  };
</script>

<style>

</style>
