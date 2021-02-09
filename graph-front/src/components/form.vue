<template>
  <el-form @submit.native.prevent class="dynamic-form" :ref="formConfig.ref" :inline="formConfig.inline" :model="formInfo"
    :label-position="formConfig.labelPosition" :label-width="formConfig.labelWidth" :size="formConfig.size"
    :status-icon="formConfig.statusIcon">
    <div class="formWrap" v-for="parentItem in formItemData" :key="parentItem.name" :label="parentItem.label" :name="parentItem.name"
      v-show="true">
      <dynamic-form-item v-for="item in parentItem.formItemList" :key="item.key" :item="item" :value="formInfo[item.key]"
        v-model="formInfo[item.key]" v-if="item.value!==undefined&&item.show!=false" @input="handleInput($event, item.key)"
        :style="{'min-width':columnMinWidth}"></dynamic-form-item>
    </div>
    <slot />
    <el-form-item>
      <template v-if="isUpdate">
        <el-button type="primary" @click="updatePortInfo">更新</el-button>
      </template>
      <template v-else>
        <el-button type="primary" @click="addPortInfo">提交</el-button>
      </template>
      <el-button @click="resetForm(formConfig.ref)">重置</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
  import {
    // addNode,
    addEquip,
    getAllEquips,
    getTableProps,
    addPort,
    updatePort
  } from '../request/api'

  export default {
    name: 'Form',
    data() {
      // 密码验证
      return {
        formData: {},
        // formInfo: {},
        // 注册表单项们
        formConfig: {
          ref: "",
          inline: true,
          labelPosition: "right",
          labelWidth: "180px",
          size: "small",
          statusIcon: true
        },
        formItemData: []
      };
    },
    props: {
      // formConfig: {
      //   type: Object,
      //   required: true
      // },
      formInfo: {
        type: Object,
        required: true
      },
      equip_type: {
        type: String,
        required: true
      },
      isUpdate: {
        type: Boolean,
        required: true
      },
      columnMinWidth: {
        type: String
      }
    },
    watch: {
       equip_type(newV,oldV) {
         this.formData = {};
         this.formItemData = [];
         this.getInputForm(this.equip_type);
         console.log(newV,oldV)
       }
    },
    created() {
      this.getInputForm(this.equip_type);
    },
    mounted() {
      // this.setDefaultValue();

    },
    methods: {
      onSubmit(form) {

      },

      resetForm(form) {
        this.$refs[form].resetFields()
      },

      addPortInfo() {
        let data = this.formData
        data['table_name'] = this.equip_type
        addPort(data)
          .then(resp => {
            if (resp.code === 201) {
              this.$emit("refreshTable", {
                table_name: this.equip_type
              });
            }
          })
          .catch(error => {
            console.log(error)
          })
      },

      updatePortInfo() {
        let data = this.formInfo
        data['table_name'] = this.equip_type

        console.log('updatePortInfo')
        console.log(data)
        updatePort(data)
          .then(resp => {
            if (resp.code === 201) {
              this.$emit("refreshTable", {
                table_name: this.equip_type
              });
            }
          })
          .catch(error => {
            console.log(error)
          })
      },

      getInputForm(equip_type) {

        // if (this.formInfo != {}) {
        //   this.formData = this.formInfo
        // }

        getTableProps({
            table_name: equip_type
          })
          .then(resp => {
            if (resp.code === 200) {
              let form_props = resp.data;
              console.log('form_props')
              console.log(form_props)
              this.formConfig['ref'] = equip_type
              this.formItemData.push({
                name: true,
                lable: 'fdsf',
                formItemList: this.formatFormInfo(form_props)
              })
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
        let tempFormObj = {}
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
          tempFormObj[item.COLUMN_NAME] = ""
        })
        this.formData = tempFormObj
        if (this.formInfo == {}) {
          this.formInfo = tempFormObj
        }
        return formItemList
      },

      handleInput(val, key) {

        console.log(val)
        console.log(key)
        // 这里element-ui没有上报event，直接就是value了
        if (typeof(val) == 'string') {
          val = val.replace(/\s+/g, ""); //去除空格
        }
        this.$emit("input", { ...this.value,
          [key]: val
        });
        this.formData[key] = val
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

<style scoped>
  .formWrap {
    overflow: hidden;
  }
</style>
