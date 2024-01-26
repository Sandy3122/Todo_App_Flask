function addTask() {
    var title = document.getElementById('title').value;

    // Check if the title is empty
    if (!title.trim()) {
        alert('Task title cannot be empty. Please provide a title.');
        return;
    }

    // Default status is set to "Pending"
    var status = 'Pending';

    fetch('/add_task', {
        method: 'POST',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        body: 'title=' + title + '&status=' + status
    })
    .then(response => response.json())
    .then(data => {
        alert(data.result);
        window.location.reload();
    });
}

function editUpdateTask(taskId, button) {
    var titleElement = document.getElementById('title-' + taskId);
    var statusElement = document.getElementById('status-' + taskId);
    var checkboxElement = document.getElementById('completed-checkbox-' + taskId);

    if (button.innerHTML.includes('bi-pencil-square')) {
        // Change the task title to a Bootstrap-styled input field for editing
        titleElement.innerHTML = '<input type="text" id="edit-title-' + taskId + '" class="form-control" value="' + titleElement.innerText + '">';

        // Change the task status to a Bootstrap-styled select menu for editing
        var statusOptions = ['Pending', 'In Progress', 'Completed'];
        var currentStatus = statusElement.innerText;
        statusElement.innerHTML = '<select id="edit-status-' + taskId + '" class="form-select">' +
            statusOptions.map(option => '<option value="' + option + '" ' + (option === currentStatus ? 'selected' : '') + '>' + option + '</option>').join('') +
            '</select>';

        // Change the button icon to "bi-floppy-fill" and apply Bootstrap styles
        button.innerHTML = '<i class="bi bi-save"></i>';
        button.classList.remove('btn-primary');
        button.classList.add('btn-success');
    } else {
        var newTitle = document.getElementById('edit-title-' + taskId).value;
        var newStatus = document.getElementById('edit-status-' + taskId).value;

        fetch('/update_task/' + taskId, {
            method: 'PUT',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ title: newTitle, status: newStatus })
        })
        .then(response => response.json())
        .then(data => {
            if (data.result === 'Task updated successfully') {
                // Update the task UI
                titleElement.innerText = newTitle;
                statusElement.innerText = newStatus;

                // Check the checkbox and add strikethrough if status is "Completed"
                checkboxElement.checked = newStatus === 'Completed';
                titleElement.style.textDecoration = newStatus === 'Completed' ? 'line-through' : 'none';

                alert(data.result);
            } else {
                alert('Failed to update task.');
            }
        })
        .finally(() => {
            // Change the button icon back to "bi-pencil-square" and revert Bootstrap styles
            button.innerHTML = '<i class="bi bi-pencil-square"></i>';
            button.classList.remove('btn-warning');
            button.classList.add('btn-primary');
        });
    }
}






function deleteTask(taskId) {
    fetch('/delete_task/' + taskId, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        alert(data.result);
        window.location.reload();
    });
}

function toggleCompleted(taskId) {
    var statusElement = document.getElementById('status-' + taskId);
    var titleElement = document.getElementById('title-' + taskId);
    var checkboxElement = document.getElementById('completed-checkbox-' + taskId);

    // Store the original status in a data attribute if not already stored
    if (!checkboxElement.hasAttribute('data-original-status')) {
        checkboxElement.setAttribute('data-original-status', statusElement.innerText);
    }

    if (checkboxElement.checked) {
        // Update status to "Completed" and add strikethrough to the title
        statusElement.innerText = 'Completed';
        titleElement.style.textDecoration = 'line-through';

        // Update the status in the database
        updateStatusInDatabase(taskId, titleElement.innerText, 'Completed');
    } else {
        // If unchecked, revert to the original status and remove strikethrough
        statusElement.innerText = checkboxElement.getAttribute('data-original-status');
        titleElement.style.textDecoration = 'none';

        // Update the status in the database
        updateStatusInDatabase(taskId, titleElement.innerText, statusElement.innerText);
    }
}

function updateStatusInDatabase(taskId, newTitle, newStatus) {
    // Update the status in the database
    fetch('/update_task/' + taskId, {
        method: 'PUT',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ title: newTitle, status: newStatus })
    })
    .then(response => response.json())
    .then(data => {
        if (data.result !== 'Task updated successfully') {
            alert('Failed to update task status.');
        }
    });
}