// script.js

document.getElementById('login-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
  
    // Here, you can add the code to handle the form submission, such as making an API request to the server for authentication.
  
    // For now, we'll just log the entered username and password.
    console.log('Username:', username);
    console.log('Password:', password);
  });
  