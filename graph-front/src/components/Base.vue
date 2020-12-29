<template>
  <el-container>
    <el-header>
      <Header>
       <template v-slot:header>
          {{title}}
        </template>
      </Header>
    </el-header>
    <el-container>
      <el-aside width="240px">
        <LeftSide></LeftSide>
      </el-aside>
      <el-container>
        <el-main>
          <!-- <Main></Main> -->
          <slot></slot>
        </el-main>
        <el-footer>
          <Footer></Footer>
        </el-footer>
      </el-container>
      <el-aside width="240px">
        <RightSide></RightSide>
      </el-aside>
    </el-container>
  </el-container>
</template>

<script>
  import Header from './Header.vue'
  import Footer from './Footer.vue'
  import Main from './Main.vue'
  import LeftSide from './LeftSide.vue'
  import RightSide from './RightSide.vue'

  export default {
    name: 'Base',
    components: {
      Header,
      Footer,
      Main,
      LeftSide,
      RightSide
    },
    data() {

    },
    props: {
      title:{
        type: String,
        default: () => ''
      }
    },
    created() {},
    mounted() {
      // this.setDefaultValue();
    },
    methods: {

    }
  };
</script>

<style scoped>
  .el-header,
  .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }

  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }

  .el-main {
    /* background-color: #E9EEF3; */
    color: #333;
    /* text-align: center; */
    line-height: 60px;
  }
</style>
