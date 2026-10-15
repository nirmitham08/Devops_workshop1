
const API_URL = "http://127.0.0.1:8000/todos";

const taskForm = document.getElementById("taskForm");
const taskInput = document.getElementById("taskInput");
const taskList = document.getElementById("taskList");
const taskCount = document.getElementById("taskCount");

// Load tasks from the backend
async function loadTasks() {
    try {
        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error("Could not load tasks");
        }

        const tasks = await response.json();
        displayTasks(tasks);
    } catch (error) {
        console.error(error);
        taskCount.textContent = "Could not connect to the backend.";
    }
}

// Display tasks on the page
function displayTasks(tasks) {
    taskList.innerHTML = "";

    tasks.forEach(function (task) {
        const li = document.createElement("li");
        li.appendChild(document.createTextNode(task.title + " "));

        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Delete";

        deleteButton.addEventListener("click", function () {
            deleteTask(task.id);
        });

        li.appendChild(deleteButton);
        taskList.appendChild(li);
    });

    taskCount.textContent =
        tasks.length + (tasks.length === 1 ? " task" : " tasks");
}

// Add a task through the API
taskForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const title = taskInput.value.trim();

    if (!title) {
        taskInput.reportValidity();
        return;
    }

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ title: title })
        });

        if (!response.ok) {
            throw new Error("Could not add task");
        }

        taskInput.value = "";
        await loadTasks();
    } catch (error) {
        console.error(error);
        alert("Could not add task. Check whether the backend is running.");
    }
});

// Delete a task through the API
async function deleteTask(id) {
    try {
        const response = await fetch(`${API_URL}/${id}`, {
            method: "DELETE"
        });

        if (!response.ok) {
            throw new Error("Could not delete task");
        }

        await loadTasks();
    } catch (error) {
        console.error(error);
        alert("Could not delete task.");
    }
}

// Load tasks when the page opens
loadTasks();
