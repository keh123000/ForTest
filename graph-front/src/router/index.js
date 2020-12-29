import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/Home'
import Product from '@/components/Product'
import Graph from '@/components/Graph'

import Form from '@/components/form'
import Item from '@/components/item'
import OrderList from "@/components/list"

import Base from "@/components/Base"

import AddEquip from "@/components/entry/AddEquip"




Vue.component('dynamic-form', Form)
Vue.component('dynamic-form-item', Item)



Vue.use(Router)


export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/AddEquip',
      name: 'AddEquip',
      component: AddEquip
    },
    {
      path: '/base',
      name: 'Base',
      component: Base
    },
    {
      path: '/list',
      name: 'OrderList',
      component: OrderList
    },
    {
      path: '/',
      name: 'Graph',
      component: Graph,
      meta: { title: "拓扑图" }
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path: '/product',
      name: 'Product',
      component: Product
    }
  ]
})
