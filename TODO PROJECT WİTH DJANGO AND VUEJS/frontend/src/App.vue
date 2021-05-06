<template>
  <div class="container">
    <div id="newtask">
      <input type="text" @keypress.enter="postData" v-model="newTodo" placeholder="Task to be done"/>
      <button id="push" @click="postData">Add</button>
    </div>
    <div id="tasks" v-for="item in todos" :key="item.id">
      <span
          style="cursor: pointer;"
          @click="updateTodo(item.id,item.todo,item.isActive)"
          id="taskname"
          :class = "(item.isActive === true)?'done':''"
      >
          {{ item.todo }}
      </span>
      <i style="cursor:pointer; float: right;" class="fas fa-trash" @click="deleteData(item.id)"></i>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      newTodo: '',
      todos: [],
    }
  },
  methods: {
    getData() {
      axios.get('http://127.0.0.1:8000/api/task-list/')
          .then((res) => res.data)
          .then((res) => {
            this.todos = res
          })
    },
    updateTodo(pk, todo, active) {
      if (active === true) {
        axios.post(`http://127.0.0.1:8000/api/task-update/${pk}`, {
          isActive: false,
          todo: todo,
          id: pk
        })
            .then(() => {
              this.getData()
            })
      } else {
        axios.post(`http://127.0.0.1:8000/api/task-update/${pk}`, {
          isActive: true,
          todo: todo,
          id: pk
        })
            .then(() => {
              this.getData()
            })
      }
    },
    deleteData(pk) {
      axios.delete(`http://127.0.0.1:8000/api/task-delete/${pk}`)
          .then(() => {
            this.getData()
          })
    },
    postData() {
      if (this.newTodo === '') {
        return alert('Lütfen boş içerik bırakmayın!');
      } else {
        axios.post(`http://127.0.0.1:8000/api/task-create/`, {
          todo: this.newTodo,
        })
            .then((res) => {
              const data = res.data
              this.todos.push(data)
              this.newTodo = "";
            })
      }
    },
  },
  mounted() {
    this.getData()
  }
}
</script>

<style>
*,
*:before,
*:after {
  padding: 0;
  margin: 0;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  -webkit-tap-highlight-color: transparent;
}

body {
  height: 100vh;
  background-image: -o-linear-gradient(
      315deg,
      #8052EC,
      #D161FF
  );
  background-image: linear-gradient(
      135deg,
      #8052EC,
      #D161FF
  );
  background-size: cover;
  background-position: center center;
  background-attachment: fixed;
}

.container {
  width: 50%;
  min-width: 340px;
  position: absolute;
  margin: auto;
  top: 0;
  left: 0;
  right: 0;
  padding: 30px 0;
  border-radius: 8px;
}

#newtask {
  position: relative;
  padding: 30px 15px;
  background-color: #ffffff;
  border-radius: 5px;
  -webkit-box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
}

#newtask input {
  border-radius: 5px;
  width: 70%;
  height: 45px;
  font-size: 15px;
  border: 2px solid #d1d3d4;
  padding: 12px;
  color: #111111;
  font-family: 'Poppins', sans-serif;
  font-weight: 500;
  position: relative;
}

#newtask input:focus {
  outline: none;
  border-color: #8052EC;
}

#newtask button {
  position: relative;
  float: right;
  width: 23%;
  height: 45px;
  border-radius: 5px;
  font-family: "Poppins", sans-serif;
  font-weight: 500;
  font-size: 16px;
  background-color: #8052EC;
  color: #fff;
  border: none;
  outline: none;
  cursor: pointer;
}

#tasks {
  width: 100%;
  position: relative;
  margin-top: 40px;
  background-color: #ffffff;
  -webkit-box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
  padding: 30px 20px;
  border-radius: 5px;
}

.task {
  background: #ffffff;
  height: 50px;
  padding: 5px 10px;
  border-radius: 0px;
  margin-top: 10px;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
  cursor: pointer;
  border-bottom: 2px solid #d1d3d4;
}

.task span {
  font-family: 'Poppins', sans-serif;
  font-size: 15px;
  font-weight: 400;
  cursor: pointer;
}

.task button {
  border: none;
  background: #8052EC;
  height: 100%;
  width: 40px;
  color: #ffffff;
  border-radius: 5px;
  cursor: pointer;
}

.completed {
  text-decoration: line-through;
}

a {
  display: block;
  color: #282828;
  font-family: "Poppins", sans-serif;
  font-weight: 500;
  position: relative;
  margin-top: 40px;
  background-color: #ffffff;
  border-radius: 5px;
  text-decoration: none;
  text-align: center;
  -webkit-box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
}

a > .fab {
  color: #FF0000;
}

@media screen and (min-width: 451px) {
  a {
    font-size: 18px;
    padding: 10px 12px 10px 12px;
  }
}

@media screen and (max-width: 450px) {
  a {
    font-size: 16px;
    padding: 10px 8px;
  }
}
.done{
  text-decoration: line-through;
}
</style>
