import axios from 'axios'
// 环境的切换
if (process.env.NODE_ENV === 'development') {
  axios.defaults.baseURL = 'http://127.0.0.1:1688/' // 开发环境
} else if (process.env.NODE_ENV === 'debug') {
  axios.defaults.baseURL = '' // 调试环境
} else if (process.env.NODE_ENV === 'production') {
  axios.defaults.baseURL = '' // 生产环境
}

axios.defaults.withCredentials = true;
axios.defaults.timeout = 1000000;

/*
设置请求传递数据的格式(看服务器要求的格式)
x-www-form-urlencoded
默认提交表单
把数据对象序列化成表单数据
*/
// axios.defaults.headers['Content-Type']='application/x-www-form-urlencoded';
// axios.defaults.transformRequest =data=>qs.stringify(data);
/*

设置默认提交json
把数据对象序列化成json字符串
*/
axios.defaults.headers['Content-Type'] = 'application/json;charset=UTF-8'; //设置默认提交json
// axios.defaults.transformRequest = data => JSON.stringify(data) //把数据对象序列化成json字符串

// axios.defaults.headers.post['Content-Type'] =' application/json;charset=UTF-8';
// axios.defaults.headers.put['Content-Type'] = 'application/json;charset=UTF-8';

// axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8';


/*
请求拦截器：发送请求前需要调用这个函数
1.当没有登录时，直接跳转到登录页
2.请求发送前把token获取 设置到header中
*/

axios.interceptors.request.use(
  config => {
    // 每次发送请求之前判断是否存在token，如果存在，则统一在http请求的header都加上token，不用每次请求都手动添加了
    const token = sessionStorage.getItem("jwt_token");
    console.log(token);
    if (token) {
      config.headers.Authorization = 'JWT ' + token
    }
    return config;
  },
  error => {
    return Promise.error(error);
  });



// 响应拦截
axios.interceptors.response.use(
  // 请求成功
  res => res.status === 200 ? Promise.resolve(res) : Promise.reject(res),

  // 请求失败
  error => {
    if (error.response) {
      // 判断一下返回结果的status == 401？  ==401跳转登录页面。  ！=401passs
      console.log(error.response);
      if (error.response.status === 401) {
        // 跳转不可以使用this.$router.push方法、
        // this.$router.push({path:'/login'})
        window.location.href = "http://127.0.0.1:8080/#/login"
      } else {
        // errorHandle(response.status, response.data.message);
        return Promise.reject(error.response);
      }
      // 请求已发出，但是不在2xx的范围
    } else {
      // 处理断网的情况
      // eg:请求超时或断网时，更新state的network状态
      // network状态在app.vue中控制着一个全局的断网提示组件的显示隐藏
      // 关于断网组件中的刷新重新获取数据，会在断网组件中说明
      // store.commit('changeNetwork', false);
      return Promise.reject(error.response);
    }
  });



// 封装get post put delete方法

// 封装xiaos请求  封装axios里的get
export function axios_get(url, params) {
  return new Promise(
    (resolve, reject) => {
      axios.get(url, {
          params: params
        })
        .then(res => {
          console.log("封装信息的的res", res);
          resolve(res.data)
        }).catch(err => {
          reject(err.data)
        })
    }
  )
}

// 封装xiaos请求  封装axios里的post
export function axios_post(url, data) {
  return new Promise(
    (resolve, reject) => {
      console.log(data);
      axios.post(url, JSON.stringify(data))
        .then(res => {
          console.log("封装信息的的res", res);
          resolve(res.data)
        }).catch(err => {
          reject(err.data)
        })
    }
  )
}

// 封装xiaos请求  封装axios里的put
export function axios_put(url, data) {
  return new Promise(
    (resolve, reject) => {
      console.log(data);
      axios.put(url, JSON.stringify(data))
        .then(res => {
          console.log("封装信息的的res", res);
          resolve(res.data)
        }).catch(err => {
          reject(err.data)
        })
    }
  )
}

// 封装xiaos请求  封装axios里的delete
export function axios_delete(url, data) {
  return new Promise(
    (resolve, reject) => {
      console.log(data);
      axios.delete(url, {
          params: data
        })
        .then(res => {
          console.log("封装信息的的res", res);
          resolve(res.data)
        }).catch(err => {
          reject(err.data)
        })
    }
  )
}



function requestFN(method, url, data) {
  // 基础请求方法
  let obj = {
    method, // 请求的类型
    url, // 请求地址
  }
  if (method === 'get') {
    obj.params = data; // url后面带参数 如 https://echarts.baidu.com/examples/a?test="1"
  } else if (method === 'post') {
    obj.data = data; // data 带参数
  }
  // 返回axios的基础方法
  return axios(obj).then(r => {
    return r; // 方法请求的数据
  })
}
