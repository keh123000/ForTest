<template>
  <el-form @submit.native.prevent class="dynamic-form" :ref="formConfig.ref" :inline="formConfig.inline" :model="value"
    :label-position="formConfig.labelPosition" :label-width="formConfig.labelWidth" :size="formConfig.size"
    :status-icon="formConfig.statusIcon">
    <div class="formWrap" v-for="parentItem in formConfig.tabs" :key="parentItem.name" :label="parentItem.label" :name="parentItem.name"
      v-show="true">
      <dynamic-form-item v-for="item in parentItem.formItemList" :key="item.key" :item="item" :value="value[item.key]"
        v-if="value[item.key]!==undefined&&item.show!=false" @input="handleInput($event, item.key)" :style="{'min-width':columnMinWidth}"></dynamic-form-item>
    </div>
    <slot />
  </el-form>
</template>

<script>
  export default {
    name: 'Form',
    data() {
      // 密码验证
      return {
        activeName: "1"
      };
    },
    props: {
      formConfig: {
        type: Object,
        required: true
      },
      value: {
        type: Object,
        required: true
      },
      showOne: {
        type: String
      },
      columnMinWidth: {
        type: String
      }
    },
    created() {},
    mounted() {
      // this.setDefaultValue();
    },
    methods: {
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
