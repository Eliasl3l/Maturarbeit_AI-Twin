function updateStatus() {
    fetch('/get_server_status/')
    .then(response => response.json())
    .then(data => {
        document.getElementById('statusText').textContent = data.status;
    })
    .catch(error => {
        console.error('Error fetching status:', error);
        document.getElementById('statusText').textContent = 'Error fetching status';
    });

    // Fetch every 1 seconds (you can adjust the interval as needed)
    setTimeout(updateStatus, 1000);
}

// Start the status update loop
updateStatus();
