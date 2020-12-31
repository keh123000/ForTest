<template>
  <div id="AddEquip">
    <Base :title="title">
    <el-row :gutter="10">
      <el-col :span="24">
        <el-row :gutter="30">
          <el-col :span="24">
            <el-row :gutter="10">
              <el-col :span="24">
                <h4>设备基础信息</h4>
              </el-col>
              <el-col :span="24">
                <el-form ref="addForm" :model="addForm" label-width="180px" size="small">
                  <el-row>
                    <el-col :span="14">
                      <el-row>
                        <el-form-item label="设备类型" prop="type" required>
                          <el-input v-model="addForm.type" placeholder="请输入设备类型" class="inputo"></el-input>
                        </el-form-item>
                        <el-form-item label="设备端口信息表名" prop="table_name" required>
                          <el-input v-model="addForm.table_name" placeholder="请输入设备端口信息表名" class="inputo"></el-input>
                        </el-form-item>
                      </el-row>
                    </el-col>
                    <el-col :span="8">
                      <el-form-item label="设备描述" prop="describe" required>
                        <el-input v-model="addForm.describe" placeholder="请输入设备描述" type="textarea" :autosize="{ minRows: 3, maxRows: 4}"
                          class="inputo"></el-input>
                      </el-form-item>
                    </el-col>
                  </el-row>
                </el-form>
              </el-col>
            </el-row>
          </el-col>
          <el-col :span="24">
            <el-row :gutter="10">
              <el-col :span="24">
                <h4>设备属性信息</h4>
              </el-col>
              <el-col :span="24">
                <el-form ref="propForm" :model="equip_prop" :rules="propRules" label-width="180px" size="small">
                  <el-row>
                    <el-col :span="14">
                      <el-form-item label="属性名称" prop="name" required>
                        <el-input v-model="equip_prop.name" placeholder="请输入属性名称" class="inputo"></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :span="8">
                      <el-form-item label="属性类型" prop="type" required>
                        <el-select v-model="equip_prop.type" placeholder="请选择属性类型" class="inputo">
                          <el-option label="整数" value="Int"></el-option>
                          <el-option label="字符串" value="String"></el-option>
                          <el-option label="日期时间" value="Datetime"></el-option>
                        </el-select>
                      </el-form-item>
                    </el-col>
                    <el-col :span="2"></el-col>
                    <el-col :span="14">
                      <el-form-item label="属性说明" prop="comment" required>
                        <el-input v-model="equip_prop.comment" placeholder="请输入属性说明" type="textarea" :autosize="{ minRows: 2, maxRows: 3}"
                          class="inputo"></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :span="6">
                      <el-form-item label="是否必填" prop="is_required" required>
                        <el-radio-group v-model="equip_prop.is_required">
                          <el-radio :label="true">是</el-radio>
                          <el-radio :label="false">否</el-radio>
                        </el-radio-group>
                      </el-form-item>
                    </el-col>
                    <el-col :span="4"></el-col>
                    <el-col :span="24">
                      <el-form-item>
                        <el-button type="primary" @click="submitForm('propForm')">添加</el-button>
                        <el-button @click="resetForm('propForm')">重置</el-button>
                      </el-form-item>
                    </el-col>
                  </el-row>
                </el-form>
              </el-col>
            </el-row>
          </el-col>
        </el-row>
      </el-col>
      <el-col :span="24">
        <h4>已添加属性信息</h4>
        <div class="prop_table">
          <template>
            <el-table :data="addForm.prop_list" height="310" border style="width: 80%;">
              <el-table-column prop="name" label="名称" width="200" align="center">
              </el-table-column>
              <el-table-column prop="type" label="类型" width="160" align="center" :formatter="formatType">
              </el-table-column>
              <el-table-column prop="is_required" label="是否必填" width="140" align="center" :formatter="formatIsRequired">
              </el-table-column>
              <el-table-column prop="comment" label="说明" align="center">
              </el-table-column>
              <el-table-column fixed="right" label="操作" width="120" align="center">
                <template slot-scope="scope">
                  <!-- <el-button @click="editRow(scope.row,'node')" size="small" type="primary" icon="el-icon-edit"
                    circle></el-button> -->
                  <el-button @click.native.prevent="deleteRow(scope.$index, addForm.prop_list)" size="small" type="danger"
                    icon="el-icon-delete" circle></el-button>
                </template>
              </el-table-column>
            </el-table>
          </template>
        </div>
      </el-col>
      <el-col :span="24">
        <el-row>
          <el-col :span="18">
            <div>s</div>
          </el-col>
          <el-col :span="6">
            <el-button @click="resetForm('addForm')">重置</el-button>
            <el-button type="primary" @click="submitForm('addForm')">提交</el-button>
          </el-col>
        </el-row>
      </el-col>
    </el-row>
    </Base>
  </div>
</template>

<script>
  import Base from '../Base.vue'

  import {
    // addNode,
    addEquip
  } from '../../request/api'


  export default {
    name: 'AddEquip',
    components: {
      Base
    },
    data() {
      return {
        title: '新增设备类型',
        addForm: {
          type: '',
          describe: '',
          table_name: '',
          prop_list: []
        },
        equip_prop: {
          'name': '',
          'type': '',
          'is_required': false,
          'comment': ''
        },
        propRules: {
          name: [{
            required: true,
            message: '请输入属性名称'
          }, {
            min: 3,
            max: 30,
            message: '长度在 3 到 30 个字符'
          }]
        }
      }
    },
    props: {

    },
    created() {},
    mounted() {
      // this.setDefaultValue();
    },
    methods: {
      submitForm(form) {
        if (form === 'propForm') {
          this.addForm.prop_list.push({
            name: this.equip_prop.name,
            type: this.equip_prop.type,
            is_required: this.equip_prop.is_required,
            comment: this.equip_prop.comment
          })

        }
        else if (form === 'addForm') {
          this.addEquipment()
        }
        // this.resetForm(form)
      },
      resetForm(form) {
        if (form === 'propForm') {
          this.$refs.propForm.resetFields()
        }
        else if (form === 'addForm') {
          this.$refs.addForm.resetFields()
        }
      },
      deleteRow(index, rows) {
        rows.splice(index, 1)
      },
      // 添加设备信息
      addEquipment() {
        var nodeList = []
        var data = this.addForm
        addEquip(this.addForm)
          .then(resp => {
            console.log(resp)
            if (resp.code === 200) {
              // nodeList = resp.data
              // this.nodeList = resp.data
              // console.log(nodeList)
              // return nodeList
            }
          })
          .catch(error => {
            console.log(error)
          })
        return nodeList
      },
      formatIsRequired(row, column) {
        switch (row.is_required) {
          case true:
            return '是'

          case false:
            return '否'

          default:
            return ''
        }
      },
      formatType(row, column) {
        switch (row.type) {
          case 'Int':
            return '整数'

          case 'String':
            return '字符串'

          case 'Datetime':
            return '日期时间'

          default:
            return ''
        }
      }
    }
  }
</script>

<style scoped>
  /* https://www.cnblogs.com/steamed-twisted-roll/p/10167501.html */
  .inputo {
    width: 300px !important;
  }

  h3 {}

  .prop_table {

  }

  /* .el-row {
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
    min-height: 36px;
  }

  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  } */
</style>
