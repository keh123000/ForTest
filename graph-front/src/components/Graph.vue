<template>
  <el-container>
    <el-header>Header</el-header>
    <el-container>
      <el-aside width="240px">Aside</el-aside>
      <el-container>
        <el-main>
          <el-row :gutter="10">
            <el-col :span="16">
              <el-row :gutter="10">
                <el-col :span="13">
                  <el-row :gutter="5">
                    <el-col :span="24">
                      <div class="grid-content">
                        <el-button type="primary"> 添加节点</el-button>
                      </div>
                    </el-col>
                    <el-col :span="24">
                      <div class="grid-content">
                        <template>
                          <el-table :data="tableData" style="width: 100%" max-height="540">
                            <el-table-column fixed prop="date" label="日期" width="150">
                            </el-table-column>
                            <el-table-column prop="name" label="姓名" width="100">
                            </el-table-column>
                            <el-table-column prop="province" label="省份" width="100">
                            </el-table-column>
                            <el-table-column fixed="right" label="操作" width="120">
                              <template slot-scope="scope">
                                <el-button @click.native.prevent="deleteRow(scope.$index, tableData)" type="text" size="small">
                                  详情
                                </el-button>
                              </template>
                            </el-table-column>
                          </el-table>
                        </template>
                      </div>
                    </el-col>
                  </el-row>
                </el-col>
                <el-col :span="11">
                  <el-row :gutter="5">
                    <el-col :span="24">
                      <div class="grid-content">
                        <el-button type="primary"> 添加连线</el-button>
                      </div>
                    </el-col>
                    <el-col :span="24">
                      <div class="grid-content bg-purple-light">
                        <template>
                          <el-table :data="tableData" style="width: 100%" max-height="540">
                            <el-table-column fixed prop="date" label="日期" width="150">
                            </el-table-column>
                            <el-table-column prop="name" label="姓名" width="120">
                            </el-table-column>
                            <el-table-column fixed="right" label="操作" width="120">
                              <template slot-scope="scope">
                                <el-button @click.native.prevent="deleteRow(scope.$index, tableData)" type="text" size="small">
                                  详情
                                </el-button>
                              </template>
                            </el-table-column>
                          </el-table>
                        </template>
                      </div>
                    </el-col>
                  </el-row>
                </el-col>
              </el-row>
            </el-col>
            <el-col :span="8">
              <el-row :gutter="5">
                <el-col :span="24">
                  <div class="grid-content">
                    <el-button type="primary"> 生成拓扑图</el-button>
                  </div>
                </el-col>
                <el-col :span="24">
                  <div class="grid-content">
                    <el-image style="width: 100%; height: 100%" :src="url" fit="cover" preview-src-list="srcList"></el-image>
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
        url: 'http://127.0.0.1:1680/static/img/result.png',
        srcList: ['http://127.0.0.1:1680/static/img/result.png'],
        tableData: [{
          date: '2016-05-03',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          zip: 200333
        }, {
          date: '2016-05-02',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          zip: 200333
        }, {
          date: '2016-05-04',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          zip: 200333
        }, {
          date: '2016-05-01',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          zip: 200333
        }, {
          date: '2016-05-02',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          zip: 200333
        }, {
          date: '2016-05-04',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          zip: 200333
        }, {
          date: '2016-05-01',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          zip: 200333
        }, {
          date: '2016-05-02',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          zip: 200333
        }, {
          date: '2016-05-04',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          zip: 200333
        }, {
          date: '2016-05-01',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          zip: 200333
        }]
      }
    }
  }
</script>

<style scoped>

  .el-header,
  .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 40px;
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
    line-height: 60px;
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
    min-height: 20px;
  }

  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
</style>
