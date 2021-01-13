<template>
  <el-form @submit.native.prevent class="dynamic-form" :ref="formConfig.ref" :inline="formConfig.inline" :model="formInfo"
    :label-position="formConfig.labelPosition" :label-width="formConfig.labelWidth" :size="formConfig.size"
    :status-icon="formConfig.statusIcon">
    <div class="formWrap" v-for="parentItem in formConfig.tabs" :key="parentItem.name" :label="parentItem.label" :name="parentItem.name"
      v-show="true">
      <dynamic-form-item v-for="item in parentItem.formItemList" :key="item.key" :item="item" :value="item.value"
        v-if="item.value!==undefined&&item.show!=false" @input="handleInput($event, item.key)" :style="{'min-width':columnMinWidth}"></dynamic-form-item>
    </div>
    <slot />
    <el-form-item>
      <el-button type="primary" @click="onSubmit(formConfig.ref)">立即创建</el-button>
      <el-button>取消</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
  import {
    // addNode,
    addEquip,
    getAllEquips,
    getTableProps
  } from '../request/api'

  export default {
    name: 'Form',
    data() {
      // 密码验证
      return {
        activeName: "1",
        tabs: [],
        activeName: 0,
        formInfo: {},
        // 注册表单项们
        formConfig: {
          ref: "formInfo",
          inline: true,
          labelPosition: "right",
          labelWidth: "100px",
          size: "small",
          statusIcon: true,
          tabs: [{
            name: true,
            lable: 'fdsf',
            formItemList: []
          }]
        },
      };
    },
    props: {
      // formConfig: {
      //   type: Object,
      //   required: true
      // },
      value: {
        type: Object,
        required: true
      },
      equip_type: {
        type: String,
        required: true
      },
      showOne: {
        type: String
      },
      columnMinWidth: {
        type: String
      }
    },
    created() {
      this.getInputForm(this.equip_type)
    },
    mounted() {
      // this.setDefaultValue();
    },
    methods: {
      onSubmit(form) {
        console.log(form)
        console.log(this.$refs[form])
        console.log('submit!')
        this.$refs[form].resetFields()
      },

      getInputForm(equip_type) {
        getTableProps({
            table_name: equip_type
          })
          .then(resp => {
            if (resp.code === 200) {
              let form_props = resp.data;
              console.log('form_props')
              console.log(form_props)
              this.formConfig = {
                ref: equip_type,
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
      },

      getFormPropValue(form_data) {
        let propValueObj = {};
        form_data.forEach(function(item, idnex, array) {
          if (item.COLUMN_NAME.toUpperCase() != 'ID') {
            propValueObj[item.COLUMN_NAME] = ""
          }
        })
        console.log(propValueObj)
        return propValueObj
      },

      formatFormInfo(form_data) {
        console.log('form_data')
        console.log(form_data)

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

      handleInput(val, key) {
        // 这里element-ui没有上报event，直接就是value了
        if (typeof(val) == 'string') {
          val = val.replace(/\s+/g, ""); //去除空格
        }
        this.$emit("input", { ...this.value,
          [key]: val
        });
      },

      setDefaultValue() {
        const formData = { ...this.value
        };
        var that = this;
        // 设置默认值
        that.formConfig.tabs.forEach(item => {
          let formItemList = item.formItemList;
          formItemList.forEach(item1 => {
            const {
              key,
              value
            } = item1;
            if (formData[key] === undefined || formData[key] === null) {
              formData[key] = value;
            }
          });
        });
        that.$emit("input", { ...formData
        });
      }
    }
  };
</script>

<style>
  .formWrap {
    overflow: hidden;
  }
</style>
