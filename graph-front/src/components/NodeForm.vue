<template>
  <div>
    <div id="nodes">
      <el-dialog title="添加节点信息" :visible.sync="formBridge.formVisible" :destroy-on-close='true' center>
        <el-dialog width="30%" title="查询结果" :visible.sync="innerVisible" append-to-body center="">
          <el-row>
            <el-col :span="0">
              <span>抱歉，未查到Rome信息！请手动输入Rome信息或放弃此节点的添加。</span>
            </el-col>
            <el-col :span="24">
              <template>
                <el-table :data="tableData" style="width: 100%" max-height="250">
                  <el-table-column fixed prop="date" label="日期" width="150">
                  </el-table-column>
                  <el-table-column prop="name" label="姓名" width="120">
                  </el-table-column>
                  <el-table-column prop="province" label="省份" width="120">
                  </el-table-column>
                  <el-table-column prop="city" label="市区" width="120">
                  </el-table-column>
                  <el-table-column prop="address" label="地址" width="300">
                  </el-table-column>
                  <el-table-column prop="zip" label="邮编" width="120">
                  </el-table-column>
                  <el-table-column fixed="right" label="操作" width="120">
                    <template slot-scope="scope">
                      <el-button @click.native.prevent="deleteRow(scope.$index, tableData)" type="text" size="small">
                        选取
                      </el-button>
                    </template>
                  </el-table-column>
                </el-table>
              </template>
            </el-col>
          </el-row>
          <span slot="footer" class="dialog-footer">
            <el-button @click="innerVisible = false">取 消</el-button>
            <el-button type="primary" @click="innerVisible = false">确 定</el-button>
          </span>
        </el-dialog>
        <el-form ref="nodeForm" :model="formObj" label-width="180px" id="nodeForm">
          <el-row>
            <el-col :span="24">
            </el-col>
            <el-col :span="24">
              <el-form ref="searchForm" :model="searchForm" label-width="120px">
                <el-row :gutter="30">
                  <el-col :span="24">
                    <el-form-item label="节点名称" prop="name">
                      <el-input v-model="formObj.name" placeholder="请输入节点名称"></el-input>
                    </el-form-item>
                    <el-form-item label="节点描述" prop="describe">
                      <el-input v-model="formObj.describe" placeholder="请输入节点描述" type="textarea" :autosize="{ minRows: 2, maxRows: 3}"></el-input>
                    </el-form-item>
                  </el-col>
                  <el-col :span="24">
                    <el-row>
                      <el-col :span="24">
                        <el-row>
                          <el-col :span="12">
                            <el-form-item label="设备类型">
                              <el-select v-model="searchForm.type" placeholder="请输入设备类型">
                                <el-option label="OLT" value="OLT"></el-option>
                                <el-option label="STC" value="STC"></el-option>
                                <el-option label="ODN" value="ODN"></el-option>
                                <el-option label="ONT_Array" value="ONT_Array"></el-option>
                              </el-select>
                            </el-form-item>
                          </el-col>
                          <el-col :span="12">
                            <el-form-item label="设备编号">
                              <el-input v-model="searchForm.number" placeholder="请输入设备编号"></el-input>
                            </el-form-item>
                          </el-col>
                        </el-row>
                      </el-col>
                      <el-col :span="24">
                        <el-form-item label="槽位号">
                          <el-input v-model="searchForm.slot" placeholder="请输入槽位号"></el-input>
                        </el-form-item>
                      </el-col>
                      <el-col :span="24">
                        <el-form-item label="Rome信息" prop="rome">
                          <el-row type="flex" class="row-bg">
                            <el-col :span="16">
                              <el-input v-model="formObj.rome" placeholder="请查询Rome信息"></el-input>
                            </el-col>
                            <el-col :span="2">
                            </el-col>
                            <el-col :span="6">
                              <el-button type="primary" @click="innerVisible=true">获取Rome信息</el-button>
                            </el-col>
                          </el-row>
                        </el-form-item>
                      </el-col>
                    </el-row>
                  </el-col>
                </el-row>
              </el-form>
            </el-col>
          </el-row>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="formBridge.formVisible=false">取 消</el-button>
          <el-button type="primary" @click="onFormSubmit">确 定</el-button>
        </div>
      </el-dialog>
    </div>
    <!--
    <div id="links">
      <el-dialog title="添加连线信息" :visible.sync="formBridge.formVisible" center>
        <el-form ref="linkForm" :model="formBridge" label-width="180px" id="linkForm">
          <el-form-item label="endport1">
            <el-input v-model="formBridge.formData.endport1" placeholder="endport1"></el-input>
          </el-form-item>
          <el-form-item label="endport2">
            <el-input v-model="formBridge.formData.endport2" placeholder="endport2"></el-input>
          </el-form-item>
          <el-form-item label="Rome_port_id1">
            <el-input v-model="formBridge.formData.Rome_port_id1" placeholder="Rome_port_id1"></el-input>
          </el-form-item>
          <el-form-item label="Rome_port_id2">
            <el-input v-model="formBridge.formData.Rome_port_id2" placeholder="Rome_port_id2"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="formBridge.formVisible = false">取 消</el-button>
          <el-button type="primary" @click="formBridge.formVisible = false">确 定</el-button>
        </div>
      </el-dialog>
    </div> -->

  </div>
</template>

<script>
  var commonNodeProp = ['name', 'describe', 'rome']
  var oltProps = []
  export default {
    name: 'NodeForm',
    props: {
      formBridge: {
        type: Object,
        required: true,
        default: () => {}
      }
    },
    data() {
      return {
        formLabelWidth: '180px',
        innerVisible: false,
        searchForm: {
          type: 'OLT',
          name: '',
          describe: '',
          slot: ''
        },
        formObj: {},
        formData: {},
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
          date: '2016-05-08',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          zip: 200333
        }, {
          date: '2016-05-06',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          zip: 200333
        }, {
          date: '2016-05-07',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          zip: 200333
        }]
      }
    },
    created() {
      this.getNullFormObj()
    },
    mounted() {

    },
    methods: {
      getNullFormObj() {
        console.log(this.formBridge)
        if (this.formBridge.isEdit) {
          return
        }
        var equipType = this.formBridge.selectedType
        var objProps = []
        if (equipType === 'OLT') {
          objProps = commonNodeProp.concat(oltProps)
        }
        for (var i = 0; i < objProps.length; i++) {
          this.formData[objProps[i]] = ''
        }
        this.formData = this.formObj
      },
      onSubmit() {
        console.log('submit!')
      },
      handleClick() {
        alert('button click')
      },
      changePropsValue(prop, value) {
        this.$emit('propsChanged', {
          name: prop,
          value: value
        }) // 自定义事件  传递值“子向父组件传值”
      },
      selectType(data) {
        this.changePropsValue('selectedType', data)
      },
      changeNodeVisible() {
        this.changePropsValue('nodeDialogFormVisible', false)
      },
      changeLinkVisible() {
        this.changePropsValue('linkDialogFormVisible', false)
      },
      onFormSubmit() {
        this.changePropsValue('formVisible', false)
      },
      onDialogClosed() {
        this.changePropsValue('formVisible', false)
        console.log(this.formBridge)
      }
    },
    watch: {

    }
  }
</script>

<style scoped>
  .el-dialog {}

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
</style>
