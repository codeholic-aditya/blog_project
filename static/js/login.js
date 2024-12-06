document.addEventListener("DOMContentLoaded", () => {

    document.getElementById("login-form").addEventListener("submit", async function (event) {
        event.preventDefault(); // Prevent the default form submission


        let username = document.getElementById("username").value;
        let password = document.getElementById("password").value;

        // Form data using user input from the form
        const formData = {
            "username": username,          // Get value from form
            "password": password,          // Get value from form
        };


        const options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData) // Ensure the body is a JSON string
        };

        // Send the form data to the API endpoint
        await fetch('http://127.0.0.1:8000/login', options)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                if (data.token) {
                    sessionStorage.setItem("token", data.token);  // Store the token in sessionStorage
                    // console.log("Token saved:", data.token);
                } else {
                    console.log("No token found in the response.");
                }

                if (data.message) {
                    alert(data.message);  // Display the message sent by the server
                } else {
                    alert("Login successful!");
                }
            })
            .catch(error => {
                console.error('Fetch error:', error);  // Log the error

                // Show a generic error message
                alert("An error occurred. Please try again later.");
            });

    });
})

// window.location.pathname