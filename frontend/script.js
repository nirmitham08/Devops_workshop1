const form = document.getElementById("taskForm");
const input = document.getElementById("taskInput");
const list = document.getElementById("taskList");
const count = document.getElementById("taskCount");

let tasks = [];

form.addEventListener("submit", function(event) {
    event.preventDefault();

    const value = input.value.trim();

    if (value === "") {
        alert("Please enter a task!");
        return;
    }

    tasks.push(value);
    renderTasks();
    input.value = "";
});

function renderTasks() {
    list.innerHTML = "";

    tasks.forEach(function(task, index) {
        const item = document.createElement("li");
        item.textContent = task + " ";

        const button = document.createElement("button");
        button.textContent = "Delete";

        button.addEventListener("click", function() {
            tasks.splice(index, 1);
            renderTasks();
        });

        item.appendChild(button);
        list.appendChild(item);
    });

    count.textContent =
        tasks.length + (tasks.length === 1 ? " task" : " tasks");
}