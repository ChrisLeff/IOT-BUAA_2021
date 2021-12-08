import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

let store = new Vuex.Store({
    state: {
      origin:"http://127.0.0.1:5000/"
    }
})
export default store