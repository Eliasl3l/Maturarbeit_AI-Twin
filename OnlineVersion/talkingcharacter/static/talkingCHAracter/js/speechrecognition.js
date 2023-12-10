//this file isnt in use /////////////////////////////////////////////////////////////////////////


// Initialize the Web Speech API
let recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();

recognition.onstart = function() {
    // Indicate that recognition has started, e.g., change a div's content or color
    document.getElementById("status").innerText = "Listening...";
};

recognition.onresult = function(event) {
    let transcript = event.results[0][0].transcript;

    // Indicate that speech was recognized
    document.getElementById("status").innerText = "Recognized: " + transcript;

    sendDataToServer(transcript);
};

function sendDataToServer(transcript) {
    // Indicate that the data is being sent to the server
    document.getElementById("status").innerText = "Sending to server...";

    fetch('/process_transcript/', {
        method: 'POST',
        body: JSON.stringify({
            'transcript': transcript
        }),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')  // Ensure CSRF token is sent for Django
        }
    })
    .then(response => response.json())
    .then(data => {
        // Indicate that the server has processed the data
        document.getElementById("status").innerText = "Data processed by server!";
    })
    .catch(error => {
        // Indicate if there's an error
        document.getElementById("status").innerText = "Error: " + error;
    });
}

// Helper function to get CSRF token from cookies
function getCookie(name) {
    let value = "; " + document.cookie;
    let parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
}


