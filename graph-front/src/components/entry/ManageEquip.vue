<template>
  <div id="ManageEquip">
    <Base :title="title">
    <el-row :gutter="10">
      <el-col :span="24">
        <h4>已添加设备信息</h4>
      </el-col>
      <el-col :span="24">
        <el-row :gutter="5">
          <template>
            <el-table :data="equipData" style="width: 100%" :max-height="410" align="center">
              <el-table-column type="expand">
                <template slot-scope="props">
                  <el-form label-position="left" inline class="demo-table-expand">
                    <el-form-item label="ID">
                      <span>{{ props.row.ID }}</span>
                    </el-form-item>
                    <el-form-item label="设备类型">
                      <span>{{ props.row.TYPE }}</span>
                    </el-form-item>
                    <el-form-item label="设备描述">
                      <span>{{ props.row.DESCRIBE }}</span>
                    </el-form-item>
                    <el-form-item label="端口信息表名">
                      <span>{{ props.row.TABLE_NAME }}</span>
                    </el-form-item>
                    <el-form-item label="表状态">
                      <span>{{ props.row.TABLE_STATUS }}</span>
                    </el-form-item>
                    <el-form-item label="创建人">
                      <span>{{ props.row.CREATOR }}</span>
                    </el-form-item>
                    <el-form-item label="创建时间">
                      <span>{{ props.row.CREATE_TIME }}</span>
                    </el-form-item>
                    <el-form-item label="更新时间">
                      <span>{{ props.row.UPDATE_TIME }}</span>
                    </el-form-item>
                  </el-form>
                </template>
              </el-table-column>
              <el-table-column label="ID" prop="ID" width="120">
              </el-table-column>
              <el-table-column label="设备类型" prop="TYPE">
              </el-table-column>
              <el-table-column label="设备描述" prop="DESCRIBE">
              </el-table-column>
              <el-table-column label="端口信息表名" prop="TABLE_NAME">
                <template slot-scope="scope">
                  <el-popover placement="right" width="500" trigger="hover" title="表属性信息" @show="getPortTablePorps(scope.row.TABLE_NAME)">
                    <el-table :data="portTablePropData">
                      <el-table-column width="120" property="COLUMN_NAME" label="属性名"></el-table-column>
                      <el-table-column width="120" property="DATA_TYPE" label="属性类型"></el-table-column>
                      <el-table-column width="200" property="COLUMN_COMMENT" label="属性说明"></el-table-column>
                    </el-table>
                    <el-button slot="reference">{{scope.row.TABLE_NAME}}</el-button>
                  </el-popover>
                </template>
              </el-table-column>
              <el-table-column label="表状态" prop="TABLE_STATUS">
              </el-table-column>
              <el-table-column fixed="right" label="操作" width="200">
                <template slot-scope="scope">
                  <template v-if="scope.row.TABLE_STATUS === 1">
                    <el-button @click="tableOperation(scope.row,0)" type="primary" size="small" class="operationBtn">去激活</el-button>
                  </template>
                  <template v-else>
                    <el-button @click="tableOperation(scope.row,0)" type="info" size="small" class="operationBtn">激 活</el-button>
                  </template>
                  <el-button @click="tableOperation(scope.row,2)" type="danger" size="small" class="operationBtn">删 除</el-button>
                </template>
              </el-table-column>
            </el-table>
          </template>
          <template>
            <div class="block" style="padding-top: 10px;">
              <el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="currentPage"
                :page-sizes="[5, 10, 20, 30, 40,50]" :page-size="pageSize" layout="total, sizes, prev, pager, next, jumper"
                :total="total" :hide-on-single-page="false">
              </el-pagination>
            </div>
          </template>
        </el-row>
      </el-col>
      <el-col :span="24">
        <el-row :gutter="5"></el-row>
      </el-col>
    </el-row>
    </Base>
  </div>
</template>

<script>
  import Base from '../Base.vue'

  import {
    // addNode,
    getTableProps,
    getAllEquips,
    addEquip,
    deleteEquip,
    updateEquip
  } from '../../request/api'


  export default {
    name: 'ManageEquip',
    components: {
      Base
    },
    data() {
      return {
        pageSize: 5,
        currentPage: 1,
        total: 0,
        title: '设备信息管理',
        equipData: [],
        portTablePropData: []
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
      handleSizeChange(val) {
        console.log(`每页 ${val} 条`);
        this.pageSize = val
        this.getEquips()
      },

      handleCurrentChange(val) {
        console.log(`当前页: ${val}`);
        this.currentPage = val
        this.getEquips()
      },

      handleClick(row) {
        console.log(row);
      },

      tableOperation(row, operate_type) {
        if (operate_type == 0) {
          let TABLE_STATUS = 1;
          if (row.TABLE_STATUS == 1) {
            TABLE_STATUS = 0
          }

          // 去激活设备信息表
          let req_data = {
            ID: row.ID,
            TABLE_STATUS: TABLE_STATUS
          };
          updateEquip(req_data)
            .then(resp => {
              if (resp.code == 200) {
                this.getEquips()
              }
            })
            .catch(error => {
              console.log(error)
            })
        } else if (operate_type == 2) {
          // 删除设备信息
          let req_data = {
            ID: row.ID,
            TABLE_NAME: row.TABLE_NAME
          };
          deleteEquip(req_data)
            .then(resp => {
              if (resp.code == 204) {
                this.getEquips()
              }
            })
            .catch(error => {
              console.log(error)
            })
        }
      },

      getEquips() {
        let req_data = {
          start: (this.currentPage - 1) * this.pageSize,
          limit: this.pageSize
        }
        getAllEquips(req_data)
          .then(resp => {
            if (resp.code === 200) {
              this.total = resp.data.total
              this.equipData = resp.data.current_data
            }
          })
          .catch(error => {
            console.log(error)
          })
      },

      getPortTablePorps(table_name) {
        getTableProps({
            table_name: table_name
          })
          .then(resp => {
            if (resp.code === 200) {
              this.portTablePropData = resp.data;
            }
          })
          .catch(error => {
            console.log(error)
          })
      },

      submitForm(form) {
        if (form === 'propForm') {
          this.addForm.prop_list.push({
            name: this.equip_prop.name,
            type: this.equip_prop.type,
            is_required: this.equip_prop.is_required,
            comment: this.equip_prop.comment
          })
        } else if (form === 'addForm') {
          this.addEquipment()
        }
        // this.resetForm(form)
      },
      resetForm(form) {
        if (form === 'propForm') {
          this.$refs.propForm.resetFields()
        } else if (form === 'addForm') {
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
  .demo-table-expand {
    font-size: 0;
  }

  .demo-table-expand label {
    width: 90px;
    color: #99a9bf;
  }

  .demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
  }

  .operationBtn {
    width: 65px;
  }
</style>
