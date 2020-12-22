<template>
  <el-container>
    <el-header>Header</el-header>
    <el-container>
      <el-aside width="240px">Aside</el-aside>
      <el-container>
        <el-main>
          <el-row :gutter="5">
            <el-col :span="14">
              <el-row :gutter="5">
                <el-col :span="13">
                  <el-row :gutter="5">
                    <el-col :span="24">
                      <div class="grid-content bg-purple">添加节点</div>
                    </el-col>
                    <el-col :span="24">
                      <div class="grid-content bg-purple-light">节点数据</div>
                    </el-col>
                  </el-row>
                </el-col>
                <el-col :span="11">
                  <el-row :gutter="5">
                    <el-col :span="24">
                      <div class="grid-content bg-purple">添加连线</div>
                    </el-col>
                    <el-col :span="24">
                      <div class="grid-content bg-purple-light">连线数据</div>
                    </el-col>
                  </el-row>
                </el-col>
              </el-row>
            </el-col>
            <el-col :span="10">
              <el-row :gutter="5">
                <el-col :span="24">
                  <div class="grid-content bg-purple">生成拓扑图</div>
                </el-col>
                <el-col :span="24">
                  <div class="grid-content">
                    <el-image style="width: 100%; height: 100%" src="http://192.168.1.168:1680/static/img/result.png" fit="fill"></el-image>
                  </div>
                </el-col>
              </el-row>
            </el-col>
          </el-row>
        </el-main>
        <el-footer>Footer</el-footer>
      </el-container>
      <el-aside width="240px">Aside</el-aside>
    </el-container>
  </el-container>
</template>

<script>
  export default {
    name: 'Graph',
    data() {
      return {
        fits: ['fill'],
        url: '../assets/result.png'
      }
    }
  }
</script>

<style scoped>
  div {
    border: 1px red;
  }

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
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 160px;
  }

  body>.el-container {
    margin-bottom: 40px;
  }

  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }

  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }


  .el-row {
    margin-bottom: 20px;

    &:last-child {
      margin-bottom: 0;
    }
  }

  .el-col {
    border-radius: 4px;
  }

  .bg-purple-dark {
    background: #99a9bf;
  }

  .bg-purple {
    background: #d3dce6;
  }

  .bg-purple-light {
    background: #e5e9f2;
  }

  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }

  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
</style>
