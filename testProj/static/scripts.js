// scripts.js
document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();
    var formData = new FormData(this);
    
    fetch('/login', {
        method: 'POST',
        body: JSON.stringify(Object.fromEntries(formData)),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('message').textContent = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
