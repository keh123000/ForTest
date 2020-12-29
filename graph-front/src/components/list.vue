<template>
  <div class="order-list">

    <dynamic-form ref="dynamicForm" :formConfig="formConfig" v-model="formInfo"></dynamic-form>


  </div>
</template>

<script>
  export default {
    name: "OrderList",
    data() {
      return {

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
          tabs:[{
            name:true,
            lable:'fdsf',
            formItemList: [{
                label: "原始订单号",
                prop: "platOrderNo",
                type: "input",
                value: "",
                key: "platOrderNo",
                clearable: true,
                placeholder: "请输入"
              },
              {
                type: "select",
                label: "订单类型",
                key: "orderType",
                prop: "orderType",
                value: "",
                placeholder: "全部",
                clearable: true,
                isHide: true,
                props: {
                  value: "code",
                  label: "name"
                },
                optionsUrl: "PO0132",
                optionsParam: {
                  pcode: "orderType"
                },
                options: []
              },
              {
                type: "select",
                label: "店铺名称",
                key: "shopId",
                prop: "shopId",
                value: "",
                clearable: true,
                props: {
                  value: "id",
                  label: "shopName"
                },
                optionsUrl: "PO1005",
                options: []
              },
              {
                type: "select",
                label: "仓库名称",
                key: "wareId",
                prop: "wareId",
                placeholder: "全部",
                value: "",
                clearable: true,
                props: {
                  value: "id",
                  label: "wareName"
                },
                optionsUrl: "PO0705",
                options: []
              },
              {
                label: "用户昵称",
                prop: "nick",
                type: "input",
                value: "",
                key: "nick",
                clearable: true,
                placeholder: "请输入"
              },
              {
                label: "商品SKU",
                prop: "goodsSku",
                type: "input",
                value: "",
                key: "goodsSku",
                clearable: true,
                placeholder: "请输入"
              },
              {
                label: "实付金额",
                key: "actualPaymin",
                prop: "actualPaymin",
                type: "input",
                isHide: false,
                subtype: "number",
                value: "",
                min: 0,
                clearable: true,
                placeholder: "",
                formItemStyle: {
                  width: "205px!important"
                },
                style: {
                  width: "80px!important"
                }
              },
              {
                label: "~",
                key: "actualPaymax",
                prop: "actualPaymax",
                type: "input",
                isHide: false,
                subtype: "number",
                value: "",
                clearable: true,
                min: 0,
                placeholder: "",
                labelWidth: "20px",
                formItemStyle: {
                  width: "120px!important"
                },
                style: {
                  width: "80px!important"
                }
              },
              {
                label: "交易时间",
                prop: "tradeTime",
                type: "date",
                subtype: "datetimerange",
                valueFormat: "yyyy-MM-dd HH:mm:ss",
                value: "",
                key: "tradeTime",
                clearable: true,
                style: {
                  width: "340px"
                },
                placeholder: "请选择"
              },
              {
                type: "select",
                label: "SKU数量",
                key: "goodsSkuRangeType",
                prop: "goodsSkuRangeType",
                value: "",
                isHide: false,
                clearable: true,
                props: {
                  value: "code",
                  label: "name"
                },
                optionsUrl: "PO0132",
                optionsParam: {
                  pcode: "mathNum"
                },
                options: [],
                formItemStyle: {
                  width: "200px!important"
                },
                style: {
                  width: "80px!important"
                }
              },
              {
                label: "",
                key: "goodsSkuRangeNum",
                prop: "goodsSkuRangeNum",
                type: "input",
                subtype: "number",
                value: "",
                isHide: false,
                clearable: true,
                min: 1,
                placeholder: "SKU数量",
                formItemStyle: {
                  width: "100px!important"
                },
                style: {
                  width: "105px!important"
                }
              },
              {
                label: "客服备注",
                key: "customRemark",
                prop: "customRemark",
                type: "input",
                maxlength: 50,
                value: "",
                clearable: true,
                placeholder: "请输入"
              },
              {
                type: "area",
                label: "省市区",
                key: "area",
                prop: "area",
                value: "",
                clearable: true,
                changeOnSelect: true,
                props: {
                  value: "cityCodeId",
                  label: "name",
                  children: "children"
                },
                options: [],
                style: {
                  width: "202px!important"
                }
              },
              {
                label: "收货地址",
                key: "receiverAddress",
                prop: "receiverAddress",
                type: "input",
                maxlength: 30,
                value: "",
                clearable: true,
                placeholder: "请输入"
              },
              {
                label: "收件人电话",
                key: "receiverPhone",
                prop: "receiverPhone",
                type: "input",
                maxlength: 30,
                isHide: false,
                value: "",
                clearable: true,
                placeholder: "请输入"
              }
            ]
          }]

        },

      };
    },
    computed: {

    },
    watch: {},
    methods: {}
  };
</script>

<style>

</style>
