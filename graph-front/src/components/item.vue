<style>
  .block {
    display: block !important;
    display: flex !important;
  }

  .inputo,
  .selecto {
    width: 300px !important;
  }

  .form-itemo {
    width: 48%;
    float: left;
  }
</style>

<template>
  <el-form-item class="form-itemo" :rules="Rules" :label="item.label" :prop="item.key" v-if="!item.isHide" :class="{'block':item.block}">

    <el-input v-if="item.type==='input'" v-bind="$attrs" v-on="$listeners" :type="item.subtype" :min="item.min" :max="item.max"
      :minlength="item.minlength" :maxlength="item.maxlength" autocomplete="off" :placeholder="item.placeholder"
      :disabled="item.disabled" :readonly="item.readonly" :autosize="item.autosize" :clearable="item.clearable" class="inputo">
      <template v-if="item.append" slot="append">{{item.append}}</template>
    </el-input>

    <el-select v-else-if="item.type==='select'" v-bind="$attrs" v-on="$listeners" :multiple="item.multiple"
      :collapse-tags="item.collapseTags" :disabled="item.disabled" :props="item.props" :clearable="item.clearable"
      :multiple-limit="item.multipleLimit" class="selecto">
      <el-option v-for="o in item.options||ajaxOptions" :key="o[item.props.value]" :label="o[item.props.label]" :value="o[item.props.value]"
        :disabled="o.disabled"></el-option>
    </el-select>


    <el-cascader v-else-if="item.type==='cascader'" v-bind="$attrs" v-on="$listeners" :options="item.options||ajaxOptions"
      :filterable="item.filterable" :change-on-select="item.changeOnSelect" :props="item.props" :placeholder="item.placeholder"
      :disabled="item.disabled" :clearable="true" class="selecto"></el-cascader>

    <el-checkbox v-else-if="item.type==='switch' && item.appearance==='checkbox'" v-bind="$attrs" v-on="$listeners"
      :disabled="item.disabled"></el-checkbox>

    <el-switch v-else-if="item.type==='switch'" v-bind="$attrs" v-on="$listeners" :disabled="item.disabled"></el-switch>

    <el-rate v-else-if="item.type==='rate'" v-bind="$attrs" v-on="$listeners" :colors="['#99A9BF', '#F7BA2A', '#FF9900']"
      text-color="#ff9900"></el-rate>

    <el-color-picker v-else-if="item.type==='color'" v-bind="$attrs" v-on="$listeners" :show-alpha="item.showAlpha"
      :color-format="item.format"></el-color-picker>

    <el-slider v-else-if="item.type==='slider'" v-bind="$attrs" v-on="$listeners" :range="item.isRange" :show-stops="item.showStops"
      :step="item.step" :min="item.min" :max="item.max"></el-slider>

    <el-radio-group v-else-if="item.type==='radio'" :disabled="item.disabled" v-bind="$attrs" v-on="$listeners">
      <component :is="item.button?'el-radio-button':'el-radio'" v-for="o in item.options||ajaxOptions" :key="o.code"
        :label="o.code" :disabled="o.disabled" :border="item.border">{{o.name}}</component>
    </el-radio-group>

    <el-checkbox-group v-else-if="item.type==='checkbox'" :min="item.min" :max="item.max" v-bind="$attrs" v-on="$listeners"
      :props="item.props">
      <component :is="item.button?'el-checkbox-button':'el-checkbox'" v-for="o in item.options||ajaxOptions" :key="o.value"
        :disabled="o.disabled" :label="o.code" :border="item.border">{{o.name}}</component>
    </el-checkbox-group>

    <el-time-picker v-else-if="item.type==='time'" :is-range="item.isRange" range-separator="-" start-placeholder="开始时间"
      end-placeholder="结束时间" :value-format="item.valueFormat" :format="item.valueFormat" default-time="12:00:00"
      :placeholder="item.placeholder" :picker-options="item.pickerOptions" v-bind="$attrs" v-on="$listeners"></el-time-picker>

    <el-date-picker v-else-if="item.type==='date'" :type="item.subtype" range-separator="-" start-placeholder="开始时间"
      end-placeholder="结束时间" :value-format="item.valueFormat" :format="item.format" :placeholder="item.placeholder"
      :picker-options="item.pickerOptions" v-bind="$attrs" v-on="$listeners" :disabled="item.disabled"></el-date-picker>
    <span v-else-if="item.type==='txt'">{{item.txt}}</span>
    <!-- <richtext v-else-if="item.type==='richtext'" v-bind="$attrs" v-on="$listeners"></richtext> -->
    <span v-else>未知控件类型</span>
  </el-form-item>
</template>

<script>
  // import Richtext from "@/components/tinymce";
  export default {
    name: 'Item',
    components: {
      // Richtext
    },
    props: {
      item: {
        type: Object,
        required: true
      }
    },
    data() {
      return {
        ajaxOptions: [],
        provinceData: [],
        city: [],
        area: []
      };
    },
    methods: {
      updateView(e) {
          this.$forceUpdate()
      }
    },
    computed: {
      Rules() {
        var that = this;
        const rules = that.item.rules;
        if (rules === undefined) return undefined;
        const R = [];
        rules.forEach(rule => {
          // 请求验证
          if (rule.sql) {
            /* 请求验证 */
            const validator = (rule2, value, callback) => {
              that.$http
                .post(rule.sql, {
                  // key: rule2.field,
                  value
                  // sql: rule.sql.replace(/{key}/gi, rule2.field)
                })
                .then(res => {
                  // eslint-disable-next-line
                  callback(!res.data.returnMsg || undefined);
                })
                .catch(err => {
                  console.log(err);
                  that.$message.error(err.message);
                  // eslint-disable-next-line
                  callback(false);
                });
            };

            R.push({
              validator,
              message: rule.message,
              trigger: "blur"
            });
            // 正则验证
          } else if (rule.pattern) {
            var reg = rule.pattern;
            const validator = (rule2, value, callback) => {
              if (value === "") {
                callback(new Error("必填哦"));
              } else if (!reg.test(value)) {
                callback(new Error(rule.message));
              } else {
                callback();
              }
            };
            R.push({
              validator,
              message: rule.message,
              trigger: "blur"
            });
          } else {
            R.push(rule);
          }
        });
        return R;
      }
    },
    created() {
      const {
        optionsUrl,
        optionsParam,
        key,
        type
      } = this.item;
      if (optionsUrl) {
        var that = this;
        that.$http
          .post(optionsUrl, optionsParam)
          .then(res => {
            // console.log(res);
            // console.log(that.item);
            if (res.data.succeed == YESTAE_OMS.SUCCESS) {
              that.item.options = res.data.datas;
              if (res.data.datas.rows) {
                that.item.options = res.data.datas.rows
              }
            }
            // that.$set(this.item, 'options', res)
            // that.ajaxOptions = res.data.datas;
            // console.log(that.item)
          })
          .catch(err => {
            that.$message.error(err.message);
          });
      }
    }
  };
</script>
