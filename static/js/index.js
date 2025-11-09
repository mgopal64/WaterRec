    document.getElementById('water-plants').addEventListener('click', async () => {
      const resultElement = document.getElementById('result');
      resultElement.textContent = "Loading...";

      try {
        // Make a request to your Flask backend
        const response = await fetch('/api/weather', {
          method: 'GET',
        });
        if (!response.ok) {
          throw new Error(`Server error: ${response.status}`);
        }

        // Get the JSON or text result from Flask
        const data = await response.json();
        resultElement.textContent = data;

      } catch (error) {
        console.error(error);
        resultElement.textContent = `❌ An error occurred: ${error.message}`;
      }
    });