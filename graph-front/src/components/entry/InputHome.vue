<template>
  <div id="InputHome">
    <Base :title="title">
    <el-row :gutter="10">
      <el-col :span="22">
        <template>
          <el-tabs v-model="activeName" type="card" @tab-click="handleClick">
            <el-tab-pane v-for="(item, index) in tabs" :label="item.TYPE" :name="item.TABLE_NAME">
              <dynamic-form ref="dynamicForm" :formConfig="getInputForm(item.TABLE_NAME)" v-model="formInfo"></dynamic-form>
            </el-tab-pane>
          </el-tabs>
        </template>
      </el-col>
      <el-col :span="2">
        <a href="/AddEquip">新增设备</a>
      </el-col>
    </el-row>
    </Base>
  </div>
</template>

<script>
  import Base from '../Base.vue'

  import {
    // addNode,
    addEquip,
    getAllEquips,
    getTableProps
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
        formInfo: {
          platOrderNo: "",
          orderType: "",
          wareId: "",
          area: [],
          receiverAddress: "",
          receiverPhone: "",
          customRemark: "",
          actualPaymax: "",
          actualPaymin: "",
          goodsSkuRangeType: "2",
          goodsSkuRangeNum: "",
          tradeTime: [],
          nick: "",
          shopId: "",
          goodsSku: ""
        },
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
        // this.getInputForm(this.activeName)
      },
      getInputForm(equip_type) {
        var config = {};
        getTableProps({
            table_name: equip_type
          })
          .then(resp => {
            if (resp.code === 200) {
              var form_props = resp.data;
              config={
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
          })
          .catch(error => {
            console.log(error)
          })
        return config
      },
      formatFormInfo(form_data) {
        var formItemList = [];
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
        getAllEquips()
          .then(resp => {
            if (resp.code === 200) {
              this.tabs = resp.data
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
