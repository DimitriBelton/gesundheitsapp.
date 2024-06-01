document.getElementById('logActivityForm').addEventListener('submit', async function (e) {
    e.preventDefault();
    let username = document.getElementById('activityUsername').value;
    let activity = document.getElementById('activity').value;
    let duration = document.getElementById('duration').value;
    let response = await fetch('/log_activity', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, activity, duration })
    });
    let result = await response.json();
    document.getElementById('message').textContent = result.message;
});

document.getElementById('deleteActivityLogForm').addEventListener('submit', async function (e) {
    e.preventDefault();
    let username = document.getElementById('deleteActivityUsername').value;
    let log_index = document.getElementById('activityLogIndex').value;
    let response = await fetch('/delete_activity_log', {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, log_index })
    });
    let result = await response.json();
    document.getElementById('message').textContent = result.message;
});
