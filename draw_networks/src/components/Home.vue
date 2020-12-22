<template>
  <div id="app">
    <div class="container">
      <div class="row">
        <div class="col-md-7" style="">
          <div class="row">
            <div class="col-md-7" style="">
              <div class="row">
                <div class="col-md-12" style="text-align: center; padding-top: 20px;">
                  <button type="button" class="btn btn-outline-primary" data-target="#addNodeModal" data-toggle="modal"
                    id="addNodeBtn">添加节点
                  </button>
                </div>
                <div class="col-md-12">
                  <div style="margin: 1px;">
                    <table class="table">
                      <thead class="thead-light">
                        <tr>
                          <th scope="col">id</th>
                          <th scope="col">Name</th>
                          <th scope="col">Desc</th>
                          <th scope="col">Port</th>
                          <th scope="col">View</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="item in getUserNodes(userId)" :key="item._id">
                          <th scope="row">{{item._id}}</th>
                          <td>{{item.name}}</td>
                          <td>{{item.describe }}</td>
                          <td>{{item.port_id}}</td>
                          <td>
                            <button type="button" class="btn btn-info" @click.prevent="viewNode(item._id)">查看</button>
                          </td>
                        </tr>
                        <tr>
                          <th scope="row">1</th>
                          <td>Mark</td>
                          <td>Otto</td>
                          <td>1024</td>
                          <td>
                            <button type="button" class="btn btn-info">查看</button>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-5" style="height: 500px;">
            </div>
          </div>
        </div>
        <div class="col-md-5" style="height: 500px;">
          <div class="row">
            <div class="col-12" style="height: 100px; text-align: center; vertical-align: middle;">
              <button type="button" class="btn btn-outline-success">生成拓扑图</button>
            </div>
            <div class="col-12">
              <img src="../assets/result.png" class="img-thumbnail imgitem" style="width: 100%; height: 100%;" onclick="BigBig(this.src, this.width, this.height);"
                data-target="#imgModal" data-toggle="modal" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import {
    // addNode,
    viewNodeById,
    getNodesByUserId
  } from '../request/api'

  export default {
    name: 'Home',
    components: {

    },
    data() {
      return {
        userId: '5fd0a07d3f1a9abb4c741b2f',
        nodeList: []
      }
    },
    // created() {

    //   getNodesByUserId(data)
    //     .then(resp => {
    //       if (resp.status === 1) {
    //         this.nodeList = resp.data
    //         console.log(nodeList)
    //         // return nodeList
    //       }
    //     })
    //     .catch(error => {
    //       console.log(error)
    //     })
    //   }
    // },
    created:function(){
      var a= []
    },
    methods: {
      //
      // 获取用户节点信息
      getUserNodes(userId) {
        var nodeList = []
        var data = {
          user_id: userId
        }
        getNodesByUserId(data)
          .then(resp => {
            if (resp.status === 1) {
              nodeList = resp.data;
              console.log(nodeList);
              return nodeList
            }
          })
          .catch(error => {
            console.log(error)
          })
        return nodeList
      },
      viewNode(nodeId) {
        var result = viewNodeById(nodeId)
        console.log(result)
        return {}
      }
    }
  }
</script>

<style>
</style>
