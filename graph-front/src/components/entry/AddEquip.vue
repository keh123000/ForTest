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
                        <el-form-item label="设备类型" prop="type">
                          <el-input v-model="addForm.type" placeholder="请输入设备类型" class="inputo"></el-input>
                        </el-form-item>
                        <el-form-item label="设备端口信息表名" prop="table_name">
                          <el-input v-model="addForm.table_name" placeholder="请输入设备端口信息表名" class="inputo"></el-input>
                        </el-form-item>
                      </el-row>
                    </el-col>
                    <el-col :span="8">
                      <el-form-item label="设备描述" prop="describe">
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
                <el-form ref="propForm" :model="equip_prop" label-width="180px" size="small">
                  <el-row>
                    <el-col :span="14">
                      <el-form-item label="属性名称" prop="name">
                        <el-input v-model="equip_prop.name" placeholder="请输入属性名称" class="inputo"></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :span="8">
                      <el-form-item label="属性类型" prop="type">
                        <el-select v-model="equip_prop.type" placeholder="请选择属性类型" class="inputo">
                          <el-option label="整数" value="Int"></el-option>
                          <el-option label="字符串" value="String"></el-option>
                          <el-option label="日期时间" value="Datetime"></el-option>
                        </el-select>
                      </el-form-item>
                    </el-col>
                    <el-col :span="2"></el-col>
                    <el-col :span="14">
                      <el-form-item label="属性说明" prop="comment">
                        <el-input v-model="addForm.comment" placeholder="请输入属性说明" type="textarea" :autosize="{ minRows: 2, maxRows: 3}"
                          class="inputo"></el-input>
                        <!-- <el-input v-model="equip_prop.comment" placeholder="请输入属性说明" class="inputo"></el-input> -->
                      </el-form-item>
                    </el-col>
                    <el-col :span="6">
                      <el-form-item label="是否必填" prop="is_required">
                        <el-radio-group v-model="equip_prop.is_required">
                          <el-radio :label="true">是</el-radio>
                          <el-radio :label="false">否</el-radio>
                        </el-radio-group>
                      </el-form-item>
                    </el-col>
                    <el-col :span="4"></el-col>
                    <el-col :span="24">
                      <el-form-item>
                        <el-button type="primary" @click="submitForm('ruleForm')">添加</el-button>
                        <el-button @click="resetForm('ruleForm')">重置</el-button>
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
        <template>
          <el-table :data="tableData" height="275" border style="width: 100%;">
            <el-table-column prop="date" label="名称" width="180">
            </el-table-column>
            <el-table-column prop="name" label="类型" width="180">
            </el-table-column>
            <el-table-column prop="address" label="说明">
            </el-table-column>
          </el-table>
        </template>
      </el-col>
      <el-col :span="24">
        <el-row>
          <el-col :span="18">

          </el-col>
          <el-col :span="6">
            <el-button @click="resetForm('ruleForm')">重置</el-button>
            <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
          </el-col>
        </el-row>
      </el-col>
    </el-row>
    </Base>
  </div>
</template>

<script>
  import Base from '../Base.vue'
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
          table_name: ''
        },
        equip_prop: {
          'name': '',
          'type': '',
          'is_required': false,
          'comment': ''
        },
        tableData: [{
          date: '2016-05-03',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        }, {
          date: '2016-05-02',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        }, {
          date: '2016-05-04',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        }, {
          date: '2016-05-01',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        }, {
          date: '2016-05-08',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        }, {
          date: '2016-05-06',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        }, {
          date: '2016-05-07',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        }]
      }
    },
    props: {

    },
    created() {},
    mounted() {
      // this.setDefaultValue();
    },
    methods: {

    }
  };
</script>

<style scoped>
 /* #AddEquip {
    width: 100%;
    height: 100%;
    background-repeat: no-repeat;
    background-position: center;
    background-image: url(./assets/bg.jpg);
    background-size: cover;
  } */

  .inputo {
    width: 300px !important;
  }
  
  h3 {
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
