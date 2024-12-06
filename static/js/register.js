document.addEventListener("DOMContentLoaded", () => {

  document.getElementById("register-form").addEventListener("submit", async function (event) {
    event.preventDefault(); // Prevent the default form submission

    // Get values from the form fields
    let username = document.getElementById("username").value;
    let firstname = document.getElementById("firstname").value;
    let lastname = document.getElementById("lastname").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let phone = document.getElementById("phone").value;
    let address = document.getElementById("address").value;

    // Form data using user input from the form
    const formData = {
      "username": username,          // Get value from form
      "first_name": firstname,       // Get value from form
      "last_name": lastname,         // Get value from form
      "email": email,                // Get value from form
      "password": password,          // Get value from form
      "phone": phone,                // Get value from form (phone as string)
      "address": address             // Get value from form
    };


    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData) // Ensure the body is a JSON string
    };

    // Send the form data to the API endpoint
    await fetch('http://127.0.0.1:8000/register', options)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log(data);  // Handle the response from the server

        if (data.message) {
          alert(data.message);  // Show success or any message sent by the server
        } else {
          alert("Registration completed successfully!");
        }

      })
      .catch(error => {
        console.error('Fetch error:', error);  // Handle any errors

        alert("An error occurred. Please try again later.");
      });
  });
})