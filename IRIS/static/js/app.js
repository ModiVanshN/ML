document.addEventListener('DOMContentLoaded', () => {
    // Add event listener to the form submission
    document.querySelector('form').addEventListener('submit', (e) => {
      e.preventDefault();
  
      // Get the input values
      const sepalLength = document.querySelector('#sepal-length').value;
      const sepalWidth = document.querySelector('#sepal-width').value;
      const petalLength = document.querySelector('#petal-length').value;
      const petalWidth = document.querySelector('#petal-width').value;
  
      // Validate input values
      if (!sepalLength ||!sepalWidth ||!petalLength ||!petalWidth) {
        alert('Please fill in all the fields!');
        return;
      }
  
      // Create a JSON object to send to the server
      const data = {
        'sepal-length': sepalLength,
        'sepal-width': sepalWidth,
        'petal-length': petalLength,
        'petal-width': petalWidth
      };
  
      // Send a POST request to the /predict endpoint
      fetch('/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      })
     .then((response) => response.json())
     .then((result) => {
        // Redirect to the result page using the relative URL
        window.location.href = result.url;
      })
     .catch((error) => {
        console.error('Error:', error);
      });
    });
  });