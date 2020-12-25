<template>
  <div>
    <div id="nodes">
      <el-dialog title="添加节点信息" :visible.sync="formBridge.formVisible" :destroy-on-close='true' center>
        <el-dialog width="30%" title="获取Rome信息" :visible.sync="innerVisible" append-to-body>
          <el-form :inline="true" :model="searchForm" class="form-inline">
            <!-- <el-form-item label="设备类型">
              <el-select v-model="searchForm.type" placeholder="设备类型">
                <el-option label="OLT" value="OLT"></el-option>
                <el-option label="STC" value="STC"></el-option>
                <el-option label="ODN" value="ODN"></el-option>
                <el-option label="ONT_Array" value="ONT_Array"></el-option>
              </el-select>
            </el-form-item> -->
            <el-form-item label="设备编号">
              <el-input v-model="searchForm.number" placeholder="number"></el-input>
            </el-form-item>
            <el-form-item label="Slot">
              <el-input v-model="searchForm.slot" placeholder="slot"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="onSubmit">查询</el-button>
            </el-form-item>
          </el-form>
        </el-dialog>
        <el-dropdown @command="selectType" v-if="formBridge.isEdit==false">
          <el-button type="primary" style="width: 90px;" plain>{{formBridge.selectedType}}<i class="el-icon-arrow-down el-icon--right"></i>
          </el-button>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item icon="el-icon-circle-plus" command="OLT">OLT</el-dropdown-item>
            <el-dropdown-item icon="el-icon-circle-plus" command="ONT">ONT</el-dropdown-item>
            <el-dropdown-item icon="el-icon-circle-plus" command="ODN">ODN</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
        <el-form ref="nodeForm" :model="formObj" label-width="180px" id="nodeForm">
          <el-form-item label="节点名称" prop="name">
            <el-input v-model="formObj.name" placeholder="name"></el-input>
          </el-form-item>
          <el-form-item label="节点描述" prop="describe">
            <el-input v-model="formObj.describe" placeholder="describe" type="textarea" :autosize="{ minRows: 3, maxRows: 4}"></el-input>
          </el-form-item>
          <el-form-item label="Rome信息" prop="rome">
            <el-input v-model="formObj.rome" placeholder="rome"></el-input>
            <el-button type="primary" @click="innerVisible=true">查询</el-button>
          </el-form-item>
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
        formObj: {}
      }
    },
    created(){
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
          this.formObj[objProps[i]] = ''
        }
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
      onFormSubmit(){
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
