<template>
  <div id="graph">
    <el-container>
      <el-header>
        <el-row :gutter="10">
          <el-col :span="24">
            <div>
              <h2>数据关系可视化</h2>
            </div>
          </el-col>
        </el-row>
      </el-header>
      <el-container>
        <el-aside width="240px">Aside</el-aside>
        <el-container>
          <el-main>
            <el-row :gutter="15">
              <el-col :span="16">
                <el-row :gutter="15">
                  <el-col :span="14">
                    <el-row :gutter="5">
                      <el-col :span="24">
                        <div class="grid-content">
                          <el-button type="primary" @click="onAddBtnClicked('node')"> 添加节点</el-button>
                        </div>
                      </el-col>
                      <el-col :span="24">
                        <div class="grid-content">
                          <template>
                            <el-table :data="nodeList" style="width: 100%" min-height="300" max-height="540">
                              <el-table-column fixed prop="name" label="名称" width="140">
                              </el-table-column>
                              <el-table-column prop="type" label="类型" width="100">
                              </el-table-column>
                              <el-table-column prop="describe" label="描述" width="160">
                              </el-table-column>
                              <el-table-column fixed="right" label="操作" width="120">
                                <template slot-scope="scope">
                                  <el-button @click="editRow(scope.row,'node')" size="small" type="primary" icon="el-icon-edit"
                                    circle></el-button>
                                  <el-button @click.native.prevent="deleteRow(scope.$index, nodeList)" size="small"
                                    type="danger" icon="el-icon-delete" circle></el-button>
                                </template>
                              </el-table-column>
                            </el-table>
                          </template>
                        </div>
                      </el-col>
                    </el-row>
                  </el-col>
                  <el-col :span="10">
                    <el-row :gutter="5">
                      <el-col :span="24">
                        <div class="grid-content">
                          <el-button type="primary" @click="onAddBtnClicked('link')"> 添加连线</el-button>
                        </div>
                      </el-col>
                      <el-col :span="24">
                        <div class="grid-content bg-purple-light">
                          <template>
                            <el-table :data="linkList" style="width: 100%" min-height="300" max-height="540">
                              <el-table-column fixed prop="Rome_port_id1" label="源节点" width="125">
                              </el-table-column>
                              <el-table-column prop="Rome_port_id2" label="目标节点" width="125">
                              </el-table-column>
                              <el-table-column fixed="right" label="操作" width="120">
                                <template slot-scope="scope">
                                  <el-button @click="editRow(scope.row,'link')" size="small" type="primary" icon="el-icon-edit"
                                    circle></el-button>
                                  <el-button @click.native.prevent="deleteRow(scope.$index, linkList)" size="small"
                                    type="danger" icon="el-icon-delete" circle></el-button>
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
                      <el-button type="primary">拓扑图预览</el-button>
                    </div>
                  </el-col>
                  <el-col :span="24">
                    <div class="grid-content" id="graphImg">
                      <template>
                        <el-popover placement="left" title="" trigger="click">
                          <el-image slot="reference" :src="graphImgUrl" :alt="graphImgUrl" style="width: 100%; height: 100%"></el-image>
                          <el-image :src="graphImgUrl" style="max-height: 600px;max-width: 900px"></el-image>
                        </el-popover>
                      </template>
                    </div>
                  </el-col>
                  <el-col :span="24">
                    <div class="grid-content" style="text-align: left;">
                      <el-form label-position="left" label-width="80px" :model="graphFormData">
                        <el-form-item label="名称">
                          <el-input v-model="graphFormData.name" readonly></el-input>
                        </el-form-item>
                        <el-form-item label="描述信息">
                          <el-input v-model="graphFormData.describe" placeholder="describe" type="textarea" :autosize="{ minRows: 2, maxRows: 3}"
                            readonly></el-input>
                        </el-form-item>
                      </el-form>
                    </div>
                  </el-col>
                  <el-col :span="24">
                    <div class="grid-content">
                      <el-button type="primary">保存</el-button>
                      <el-button type="primary">下载</el-button>
                    </div>
                  </el-col>
                </el-row>
              </el-col>
            </el-row>
          </el-main>
          <el-footer></el-footer>
        </el-container>
        <el-aside width="240px"></el-aside>
      </el-container>
    </el-container>
    <NodeForm v-on:propsChanged="updateBridgeProps" :formBridge="{
          formVisible: this.formVisible,
          formData: this.formData,
          selectedType: this.selectedType,
          isEdit: this.isEdit
        }"></NodeForm>
        
    <!-- <template>
      <div>
        <div id="nodes">
          <el-dialog title="添加节点信息" :visible.sync="nodeDialogFormVisible" center>
            <el-dropdown @command="selectType">
              <el-button type="primary" style="width: 90px;" plain>{{selectedType}}<i class="el-icon-arrow-down el-icon--right"></i>
              </el-button>
              <el-dropdown-menu slot="dropdown">
                <el-dropdown-item icon="el-icon-circle-plus" command="OLT">OLT</el-dropdown-item>
                <el-dropdown-item icon="el-icon-circle-plus" command="ONT">ONT</el-dropdown-item>
                <el-dropdown-item icon="el-icon-circle-plus" command="ODN">ODN</el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
            <el-form ref="nodeForm" :model="nodeFormData" label-width="180px" id="nodeForm">
              <el-form-item label="name" prop="name">
                <el-input v-model="nodeFormData.name" placeholder="name"></el-input>
              </el-form-item>
              <el-form-item label="slot_id" prop="slot_id" v-if="selectedType=='OLT'">
                <el-input v-model="nodeFormData.slot_id" placeholder="slot_id"></el-input>
              </el-form-item>
              <el-form-item label="port_id" prop="port_id" v-if="selectedType=='OLT'">
                <el-input v-model="nodeFormData.port_id" placeholder="port_id"></el-input>
              </el-form-item>
              <el-form-item label="Rome_port_id" prop="Rome_port_id" v-if="selectedType=='OLT'">
                <el-input v-model="nodeFormData.Rome_port_id" placeholder="Rome_port_id"></el-input>
              </el-form-item>
              <el-form-item label="Input2Rome_port_id" prop="Input2Rome_port_id" v-if="selectedType=='ODN'">
                <el-input v-model="nodeFormData.Input2Rome_port_id" placeholder="Input2Rome_port_id"></el-input>
              </el-form-item>
              <el-form-item label="Output2Rome_port_id" prop="Output2Rome_port_id" v-if="selectedType=='ODN'">
                <el-input v-model="nodeFormData.Output2Rome_port_id" placeholder="Output2Rome_port_id"></el-input>
              </el-form-item>
              <el-form-item label="Input2Rome_port_id" prop="Input2Rome_port_id" v-if="selectedType=='ONT'">
                <el-input v-model="nodeFormData.Input2Rome_port_id" placeholder="Input2Rome_port_id"></el-input>
              </el-form-item>
              <el-form-item label="describe" prop="describe">
                <el-input v-model="nodeFormData.describe" placeholder="describe" type="textarea" :autosize="{ minRows: 3, maxRows: 4}"></el-input>
              </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button @click="changeNodeVisible">取 消</el-button>
              <el-button @click="changeNodeVisible">重 置</el-button>
              <el-button type="primary" @click="addNodeData">提 交</el-button>
              <el-button type="primary" @click="addNodeData">更 新</el-button>
            </div>
          </el-dialog>
        </div>

        <div id="links">
          <el-dialog title="添加连线信息" :visible.sync="linkDialogFormVisible" center>
            <el-form ref="linkForm" :model="linkFormData" label-width="180px" id="linkForm">
              <el-form-item label="endport1">
                <el-input v-model="linkFormData.endport1" placeholder="endport1"></el-input>
              </el-form-item>
              <el-form-item label="endport2">
                <el-input v-model="linkFormData.endport2" placeholder="endport2"></el-input>
              </el-form-item>
              <el-form-item label="Rome_port_id1">
                <el-input v-model="linkFormData.Rome_port_id1" placeholder="Rome_port_id1"></el-input>
              </el-form-item>
              <el-form-item label="Rome_port_id2">
                <el-input v-model="linkFormData.Rome_port_id2" placeholder="Rome_port_id2"></el-input>
              </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button @click="changeLinkVisible">取 消</el-button>
              <el-button type="primary" @click="changeLinkVisible">确 定</el-button>
            </div>
          </el-dialog>
        </div>

      </div>
    </template> -->
  </div>

</template>

<script>
  import NodeForm from './NodeForm.vue'
  export default {
    name: 'Graph',
    data() {
      return {
        selectedType: 'OLT',
        formVisible: false,
        isEdit: false,
        formData: {},
        nodeDialogFormVisible: false,
        linkDialogFormVisible: false,
        nodeFormData: {
          name: '',
          slot_id: '',
          port_id: '',
          Rome_port_id: '',
          describe: '',
          Input2Rome_port_id: '',
          Output2Rome_port_id: ''
        },
        linkFormData: {
          endport1: '',
          endport2: '',
          Rome_port_id1: '',
          Rome_port_id2: ''
        },
        graphFormData: {
          name: '拓扑图demo',
          describe: '拓扑图demo的描述信息'
        },
        graphImgUrl: 'http://192.168.1.168:1680/static/img/result.png',
        // srcList: ['http://127.0.0.1:1680/static/img/result.png'],
        nodeList: [{
            _id: "5fd18d5a06fbdba7c5d40aed",
            name: 'OLT',
            slot_id: '11',
            port_id: '1234',
            Rome_port_id: '2356',
            describe: '防水粉色突然',
            type: 'OLT',
            Input2Rome_port_id: '569',
            Output2Rome_port_id: '756'
          },
          {
            _id: "5fd18d5a06fbdba7c5d40aed",
            name: 'OLT',
            slot_id: '11',
            port_id: '1234',
            Rome_port_id: '2356',
            describe: '防水粉色突然',
            type: 'OLT',
            Input2Rome_port_id: '569',
            Output2Rome_port_id: '756'
          },
          {
            _id: "5fd18d5a06fbdba7c5d40aed",
            name: 'OLT',
            slot_id: '11',
            port_id: '1234',
            Rome_port_id: '2356',
            describe: '防水粉色突然',
            type: 'OLT',
            Input2Rome_port_id: '569',
            Output2Rome_port_id: '756'
          },
          {
            _id: "5fd18d5a06fbdba7c5d40aed",
            name: 'OLT',
            slot_id: '11',
            port_id: '1234',
            Rome_port_id: '2356',
            describe: '防水粉色突然',
            type: 'OLT',
            Input2Rome_port_id: '569',
            Output2Rome_port_id: '756'
          },
          {
            _id: "5fd18d5a06fbdba7c5d40aed",
            name: 'OLT',
            slot_id: '11',
            port_id: '1234',
            Rome_port_id: '2356',
            describe: '防水粉色突然',
            type: 'OLT',
            Input2Rome_port_id: '569',
            Output2Rome_port_id: '756'
          }
        ],
        linkList: [{
            _id: "5fd2cc3cf2729bd71a93d467",
            endport1: '搭嘎段',
            endport2: '高度和规范的',
            Rome_port_id1: '52147',
            Rome_port_id2: '89523'
          },
          {
            _id: "5fd2cc3cf2729bd71a93d467",
            endport1: '搭嘎段',
            endport2: '高度和规范的',
            Rome_port_id1: '52147',
            Rome_port_id2: '89523'
          },
          {
            _id: "5fd2cc3cf2729bd71a93d467",
            endport1: '搭嘎段',
            endport2: '高度和规范的',
            Rome_port_id1: '52147',
            Rome_port_id2: '89523'
          }
        ],
        formBridge: {
          formVisible: this.formVisible,
          formData: this.formData,
          selectedType: this.selectedType,
          isEdit: this.isEdit
        }
      }
    },
    methods: {
      handleClick(e) {
        alert(e.name)
      },
      updateBridgeProps(e) {
        if (e.name === 'formVisible') {
          this.formVisible = e.value
        }
      },
      editRow(row, dataFlag) {
        if (dataFlag === 'node') {
          this.selectedType = row.type
          this.nodeFormData = row
          this.nodeDialogFormVisible = true
        } else if (dataFlag === 'link') {
          this.linkFormData = row
          this.linkDialogFormVisible = true
        }
      },
      onAddBtnClicked(dataFlag) {
        this.formVisible = true
        if (dataFlag === 'node') {

        } else if (dataFlag === 'link') {

        }
      },
      deleteRow(index, rows) {
        rows.splice(index, 1)
      },
      resetForm(formName) {
        //    this[formName] = {}
        this.$refs[formName].resetFields()
        //    this.$nextTick(() => {
        //     this.$refs[formName].resetFields()
        //    });
      },
      selectType(data) {
        this.selectedType = data
        this.resetForm('nodeForm')
      },
      addNodeData() {
        console.log(this.selectedType)
        console.log(this.nodeFormData)
        this.nodeDialogFormVisible = false
      },
      changeNodeVisible() {
        this.nodeDialogFormVisible = false
      },
      changeLinkVisible() {
        this.linkDialogFormVisible = false
      }

    },
    components: {
      'NodeForm': NodeForm
    }
  }
</script>

<style scoped>
  .el-header {
    padding-top: 20px;
    height: 80px !important;
    color: white;
  }

  .el-header,
  .el-footer {
    /* background-color: #B3C0D1; */
    text-align: center;
    /* line-height: 60px; */
  }

  .el-aside {
    /* background-color: #D3DCE6; */
    color: #333;
    text-align: center;
    line-height: 200px;
  }

  .el-main {
    /* background-color: #E9EEF3; */
    color: #333;
    text-align: center;
    line-height: 60px;
  }

  /* 设置表格边框样式 */
  .el-table {
    border-radius: 6px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
  }

  .el-dropdown {
    padding-bottom: 20px;
    vertical-align: top;
  }

  .el-dropdown+.el-dropdown {
    margin-left: 15px;
  }

  .el-icon-arrow-down {
    font-size: 12px;
  }

  /*  body>.el-container {
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
  } */
</style>
