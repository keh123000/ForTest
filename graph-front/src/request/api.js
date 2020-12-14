//将我们http.js中封装好的  get,post.put,delete  导过来

import {
  axios_get,
  axios_post,
  axios_delete,
  axios_put
} from './http.js'


// 节点（nodes）操作相关api

// 获取所有节点信息
export const getAllNodes = p => axios_get("/nodes", p);
// 添加节点
export const addNode = p => axios_post("/node", p);
// 根据用户id获取用户所有节点信息
export const getNodesByUserId = p => axios_get("/nodes/" + p.user_id, p);
// 查看单一节点信息
export const viewNodeById = p => axios_get("/node/" + p.node_id, p);


// 连线（links）操作相关api

// 获取所有节点信息
export const getAllLinks = p => axios_get("/links", p);
// 添加节点
export const addLink = p => axios_post("/link", p);
// 根据用户id获取用户所有节点信息
export const getLinksByUserId = p => axios_get("/links/" + p.user_id, p);
// 查看单一节点信息
export const viewLinkById = p => axios_get("/link/" + p.node_id, p);
