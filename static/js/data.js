document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("water-plants");
    const resultElement = document.getElementById("result");

    button.addEventListener("click", async () => {
        resultElement.textContent = "Loading...";

        try {
            // Make a request to Flask backend
            const response = await fetch("/api/weather");
            
            if (!response.ok) {
                throw new Error(`Server error: ${response.status}`);
            }

            const data = await response.json();

            // Display the result
            if (data.result === true) {
                resultElement.textContent = "✅ It's time to water the plants!";
            } else if (data.result === false) {
                resultElement.textContent = "🌿 No need to water right now.";
            } else if (data.error) {
                resultElement.textContent = `⚠️ Error: ${data.error}`;
            } else {
                resultElement.textContent = `Response: ${JSON.stringify(data)}`;
            }
        } catch (error) {
            console.error(error);
            resultElement.textContent = `❌ An error occurred: ${error.message}`;
        }
    });
});
