<template>
  <div id="TaskList">
    <h1>Task List</h1>
    <ul>
      <li v-for="task in tasks" :key="task.id">
        <input type="checkbox" v-model="task.completed" @change="updateTask(task.id)">
        {{ task.title }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
    data() {
        return {
            tasks: []
        };
    },
    mounted() {
        this.fetchTasks();
    },
    methods: {
        fetchTasks() {
            // Здесь будет код для получения списка задач из API Django
            fetch('http://localhost:8000/api/tasks/')
                .then(response => response.json())
                .then(data => {
                    this.tasks = data.tasks;
                });
        },
        updateTask(taskId) {
            // Здесь будет код для отправки запроса на обновление статуса задачи в API Django
            fetch(`http://localhost:8000/api/tasks/${taskId}/update/`, {
                method: 'POST',
            })
                .then(response => response.json())
                .then(data => {
                    const updatedTask = this.tasks.find(task => task.id === data.id);
                    updatedTask.completed = data.completed;
                });
        }
    }
};
</script>

<style>
#app {
    text-align: center;
    margin-top: 60px;
}

ul {
    list-style-type: none;
    padding: 0;
}
</style>
