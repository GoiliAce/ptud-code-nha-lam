$(document).ready(function () {
    // load tasks from local storage
    function loadTasks() {
        var day = $('#day').val();
        var task_by_day = JSON.parse(localStorage.getItem('tasks_by_week'))[day];
        if (task_by_day) {
            $.each(task_by_day, function (index, task) {
                var taskItem =
                    `
                        <div class="form-group task-item-box">
                            <input type="checkbox" name="${task.id}" id="${task.id}" ${(task.completed ? 'checked' : '')} class="from-control custom-checkbox">
                            <label for="${task.id}" class="task-label  ${(task.completed ? 'completed' : '')}">${task.task}</label>
                            <i class="fas fa-trash task-delete"></i>
                            <i class="fas fa-pencil-alt task-edit"></i>
                            <i class="fas fa-check task-save d-none"></i>
                        </div>
                `;
                $('#task-list').append(taskItem);
            });
        }
    }
    // save tasks to local storage
    function saveTasksByWeek(tasks_by_day, day) {
        var tasks_by_week = JSON.parse(localStorage.getItem('tasks_by_week'));
        if (tasks_by_week) {
            tasks_by_week[day] = tasks_by_day;
        } else {
            tasks_by_week = {
                [day]: tasks_by_day
            }
        }
        localStorage.setItem('tasks_by_week', JSON.stringify(tasks_by_week));
    }
    function saveTasks() {
        var tasks = [];
        var day = $('#day').val();
        var tasks_by_day = [];
        $('#task-list').children().each(function () {
            var task = {
                "id": $(this).children('input[type="checkbox"]').attr('id'),
                "task": $(this).children('.task-label').text(),
                "completed": $(this).children('input[type="checkbox"]').is(':checked')
            }
            tasks.push(task);
            tasks_by_day.push(task);
        });
        localStorage.setItem('tasks', JSON.stringify(tasks));
        saveTasksByWeek(tasks_by_day, day);
    }
    function editTask() {
        var task = $(this).parents().children('.task-label').text();
        $(this).parents().children('.task-label').html('<input type="text" class="task-edit-input">');
        $(this).parents().children('.task-label').children('.task-edit-input').val(task);
        $(this).parents().children('.task-label').children('.task-edit-input').focus();
        $(this).addClass('d-none');
        $(this).parents().children('.task-save').removeClass('d-none');
    }
    function saveTask() {
        var task = $(this).parents().children('.task-label').children('.task-edit-input').val();
        $(this).parents().children('.task-label').html(task);
        $(this).addClass('d-none');
        $(this).parents().children('.task-edit').removeClass('d-none');
        saveTasks();
    }
    saveTasks();
    function deleteTask() {
        $(this).parents('.task-item-box').remove();
        saveTasks();
    }
    function completeTask() {
        if ($(this).is(':checked')) {
            $(this).parents().children('.task-label').addClass('completed');
        } else {
            $(this).parents().children('.task-label').removeClass('completed');
        }
        saveTasks();
    }
    function update_task_by_day() {
        $('#task-list').html('');
        loadTasks();
        add_even_new_task()
    }
    function add_even_new_task() {
        $('.task-edit').click(editTask);
        $('.task-save').click(saveTask);
        $('.task-delete').click(deleteTask);
        $('input[type="checkbox"]').click(completeTask);
        $('#day').change(update_task_by_day);
    }

    $('#add-task').click(function () {
        var day = $('#day').val();
        var tasks = JSON.parse(localStorage.getItem('tasks_by_week'))[day];
        var task_id = 1
        if (tasks) {
            task_id = tasks.length + 1;
        }
        var new_task = `
                        <div class="form-group task-item-box">
                            <input type="checkbox" name="task${task_id}" id="task${task_id}" class="from-control custom-checkbox">
                            <label for="task${task_id}" class="task-label "></label>
                            <i class="fas fa-trash task-delete"></i>
                            <i class="fas fa-pencil-alt task-edit"></i>
                            <i class="fas fa-check task-save d-none"></i>
                        </div>
        `
        $('#task-list').append(new_task);
        $('#task-list').children().last().children('.task-label').html('<input type="text" class="task-edit-input">');
        $('#task-list').children().last().children('.task-label').children('.task-edit-input').focus();
        $('#task-list').children().last().children('.task-save').removeClass('d-none');
        $('#task-list').children().last().children('.task-edit').addClass('d-none');
        add_even_new_task()
        saveTasks();
    });


    // main
    var days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    var today = days[new Date().getDay()];
    $('#day').val(today);
    if (JSON.parse(localStorage.getItem('tasks_by_week')))
        saveTasks();
    loadTasks();
    add_even_new_task()
    console.log($('#day').val());
});
