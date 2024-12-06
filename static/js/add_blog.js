document.addEventListener("DOMContentLoaded", () => {

    document.getElementById("add-blog-form").addEventListener("submit", async function (event) {
        event.preventDefault(); // Prevent the default form submission


        let title = document.getElementById("title").value;
        let description = document.getElementById("description").value;

        // Form data using user input from the form
        const formData = {
            "title": title,          // Get value from form
            "description": description,          // Get value from form
        };

        let token=sessionStorage.getItem("token")

        const options = {
            method: 'POST',
            headers: {
                "header":token,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData) // Ensure the body is a JSON string
        };

        // Send the form data to the API endpoint
        await fetch('http://127.0.0.1:8000/add-post', options)
            .then(response => {
                console.log(response)
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log(data); 
                
                if (data.message) {
                    alert(data.message);  // Display the message sent by the server
                } else {
                    alert("Blog successfully added !");
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