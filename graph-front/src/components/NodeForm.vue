<template>
  <div>
    <div id="nodes">
      <el-dialog title="添加节点信息" :visible.sync="nodeDialogFormVisible" :destroy-on-close='true' center @close="onDialogClosed">
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
          <el-form-item label="name">
            <el-input v-model="nodeFormData.name" placeholder="name"></el-input>
          </el-form-item>
          <el-form-item label="solt_id" v-if="selectedType=='OLT'">
            <el-input v-model="nodeFormData.solt_id" placeholder="solt_id"></el-input>
          </el-form-item>
          <el-form-item label="port_id" v-if="selectedType=='OLT'">
            <el-input v-model="nodeFormData.port_id" placeholder="port_id"></el-input>
          </el-form-item>
          <el-form-item label="Rome_port_id" v-if="selectedType=='OLT'">
            <el-input v-model="nodeFormData.Rome_port_id" placeholder="Rome_port_id"></el-input>
          </el-form-item>
          <el-form-item label="Input2Rome_port_id" v-if="selectedType=='ODN'">
            <el-input v-model="nodeFormData.Input2Rome_port_id" placeholder="Input2Rome_port_id"></el-input>
          </el-form-item>
          <el-form-item label="Output2Rome_port_id" v-if="selectedType=='ODN'">
            <el-input v-model="nodeFormData.Output2Rome_port_id" placeholder="Output2Rome_port_id"></el-input>
          </el-form-item>
          <el-form-item label="Input2Rome_port_id" v-if="selectedType=='ONT'">
            <el-input v-model="nodeFormData.Input2Rome_port_id" placeholder="Input2Rome_port_id"></el-input>
          </el-form-item>
          <el-form-item label="describe">
            <el-input v-model="nodeFormData.describe" placeholder="describe" type="textarea" :autosize="{ minRows: 3, maxRows: 4}"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="changeNodeVisible">取 消</el-button>
          <el-button type="primary" @click="changeNodeVisible">确 定</el-button>
        </div>
      </el-dialog>
    </div>

    <div id="links">
      <el-dialog title="添加连线信息" :visible.sync="linkDialogFormVisible" center @close="onDialogClosed">
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
</template>

<script>
  export default {
    name: 'NodeForm',
    props: {
      selectedType: {
        type: String,
        required: true,
        default: 'OLT'
      },
      nodeDialogFormVisible: {
        type: Boolean,
        required: true,
        default: false
      },
      linkDialogFormVisible: {
        type: Boolean,
        required: true,
        default: false
      },
      nodeFormData: {
        type: Object,
        required: true
      },
      linkFormData: {
        type: Object,
        required: true
      }
    },
    data() {
      return {
        formLabelWidth: '120px',
      };
    },
    methods: {
      handleClick() {
        alert('button click');
      },
      changePropsValue(prop, value) {
        this.$emit("nodePropsChanged", {
          name: prop,
          value: value
        }); //自定义事件  传递值“子向父组件传值”
      },
      selectType(data) {
        this.changePropsValue('selectedType', data)
      },
      changeNodeVisible() {
        this.changePropsValue('nodeDialogFormVisible', false);
      },
      changeLinkVisible() {
        this.changePropsValue('linkDialogFormVisible', false);
      },
      onDialogClosed() {
        this.changeNodeVisible();
        this.changeLinkVisible();
      }
    },
    watch: {

    }
  };
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
