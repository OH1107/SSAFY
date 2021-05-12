import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todoList: [],
  },
  mutations: {
    ADD_TODO: function (state, todoItem) {
      state.todoList.push(todoItem)
    }
  },
  actions: {
    // 컴포넌트에서 dispatch로 호출할 함수
    addTodo: function (context, content){
      const todo = {
        content: content,
        createdAt: Date.now(),
        completed: false,
      }

      context.commit('ADD_TODO', todo)
    }
  },
  modules: {
  }
})
