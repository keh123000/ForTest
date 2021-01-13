<template>
  <div id="InputHome">
    <Base :title="title">
    <el-row :gutter="10">
      <el-col :span="24">
        <a href="/AddEquip">新增设备</a>
        <a href="/ManageEquip">设备管理</a>
      </el-col>
      <el-col :span="24">
        <template>
          <el-tabs v-model="activeName" type="card" @tab-click="handleClick">
            <el-tab-pane v-for="(item, index) in tabs" :label="item.TYPE" :name="item.TABLE_NAME" :key="index">
              <dynamic-form ref="dynamicForm" :equip_type="item.TABLE_NAME" :formInfo="formInfo" :isUpdate="false" v-model="formInfo"
                v-on:refreshTable="refreshLatestData"></dynamic-form>
            </el-tab-pane>
          </el-tabs>
        </template>
      </el-col>
      <el-col :span="24">
        <template>
          <el-table :data="tableData" border width="100%">
            <el-table-column :key="col.prop" :label="col.label" :prop="col.prop" v-for="col in cols">
            </el-table-column>
            <el-table-column label="操作" prop="option">
              <template slot-scope="scope">
                <el-button @click="editPort(scope.row)" size="mini" type="primary">
                  <i class="el-icon-edit"></i>
                  编辑
                </el-button>
              </template>
            </el-table-column>
          </el-table>
        </template>
      </el-col>
    </el-row>
    <el-dialog title="修改端口信息" :visible.sync="dialogFormVisible">
      <dynamic-form ref="dynamicForm" :equip_type="editEquipType" :formInfo="editFormInfo" :isUpdate="true" v-model="formInfo"
        v-on:refreshTable="refreshLatestData"></dynamic-form>
    </el-dialog>
    </Base>
  </div>
</template>

<script>
  import Base from '../Base.vue'

  import {
    // addNode,
    addEquip,
    getAllEquips,
    getTableProps,
    getLatestPortData
  } from '../../request/api'


  export default {
    name: 'InputHome',
    components: {
      Base
    },
    data() {
      return {
        title: '设备端口数据录入',
        tabs: [],
        activeName: 0,
        latestData: [],
        tableData: [],
        cols: [],
        editEquipType: '',
        dialogFormVisible: false,
        formInfo: {},
        editFormInfo: {},
        // 注册表单项们
        formConfig: {
          ref: "formInfo",
          inline: true, // 是否使用inline排版
          labelPosition: "right", // 标签对齐方式
          labelWidth: "100px", // 标签宽度
          size: "small", // 尺寸
          statusIcon: true, // 显示验证图标
          tabs: [{
            name: true,
            lable: 'fdsf',
            formItemList: []
          }]
        },
        formItemData: []
      }
    },
    props: {

    },
    created() {
      this.getEquips()

    },
    mounted() {
      // this.setDefaultValue();

    },
    methods: {
      handleClick(tab, event) {
        console.log(this.activeName);
        this.formInfo = {};
        this.tableData = [];
        this.refreshLatestData({
          table_name: this.activeName
        })
        // this.getInputForm(this.activeName)
      },

      editPort(e) {
        console.log(e)
        this.editEquipType = this.activeName
        this.editFormInfo = e
        this.dialogFormVisible = true
      },

      refreshLatestData(e) {
        this.dialogFormVisible = false

        let data = {
          table_name: e.table_name,
          start: 0,
          limit: 5
        }

        getLatestPortData(data)
          .then(resp => {
            if (resp.code === 201) {
              console.log(resp.data)
              this.latestData = resp.data

              this.cols = []
              if (resp.data != []) {
                let one_obj = resp.data[0]
                let prop_list = Object.keys(one_obj)
                for (var j = 0; j < prop_list.length; j++) {
                  var obj = {}
                  obj.label = prop_list[j]
                  obj.prop = prop_list[j]
                  this.cols.push(obj)
                }
              }
              // for (var j = 0; j < resp.data.length; j++) {
              //   var obj = {}
              //   obj.label = resp.data[j].label
              //   obj.prop = resp.data[j].prop
              //   this.cols.push(obj)
              // }
              console.log(this.cols)
              this.tableData = resp.data
              // for (var i = 0; i < resp.data.length; i++) {
              //   this.tableData.push(res.data.data.each_row[i])
              // }
              console.log(this.tableData)
            }
          })
          .catch(error => {
            console.log(error)
          })
      },

      getInputForm(equip_type) {
        let config = {}
        getTableProps({
            table_name: equip_type
          })
          .then(resp => {
            if (resp.code === 200) {
              let form_props = resp.data;
              config = {
                ref: "formInfo",
                inline: true,
                labelPosition: "right",
                labelWidth: "100px",
                size: "small",
                statusIcon: true,
                tabs: [{
                  name: true,
                  lable: 'fdsf',
                  formItemList: this.formatFormInfo(form_props)
                }]
              }
            }
            console.log(config)
          })
          .catch(error => {
            console.log(error)
          })
        console.log(config)
        return config
      },

      formatFormInfo(form_data) {
        let formItemList = [];
        form_data.forEach(function(item, idnex, array) {
          if (item.COLUMN_NAME.toUpperCase() != 'ID') {
            formItemList.push({
              label: item.COLUMN_COMMENT,
              prop: item.COLUMN_NAME,
              type: "input",
              value: "",
              key: item.COLUMN_NAME,
              clearable: true,
              show: true,
              placeholder: "请输入"
            });
          }
        })
        return formItemList
      },

      getEquips() {
        let req_data = {
          TABLE_STATUS: 1
        };
        getAllEquips(req_data)
          .then(resp => {
            if (resp.code === 200) {
              this.tabs = resp.data.current_data
              if (resp.data.length != 0) {
                this.activeName = resp.data.current_data[0].TABLE_NAME

                console.log('this.activeName', this.activeName)
                this.refreshLatestData({
                  table_name: this.activeName
                })
              }
            }
          })
          .catch(error => {
            console.log(error)
          })
      }
    }
  }
</script>

<style scoped>
  .inputo {
    width: 300px !important;
  }
</style>
