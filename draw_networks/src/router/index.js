import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Nodes from '@/components/Nodes'
import Links from '@/components/Links'
import Graphs from '@/components/Graphs'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/',
      name: 'Nodes',
      component: Nodes
    },
    {
      path: '/',
      name: 'Links',
      component: Links
    },{
      path: '/',
      name: 'Graphs',
      component: Graphs
    }
  ]
})
