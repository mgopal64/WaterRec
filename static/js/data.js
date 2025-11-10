document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("data");
    const resultData = document.getElementById("latest_data");

    button.addEventListener("click", async () => {
        resultData.textContent = "Loading...";

        try {
            // Make a request to Flask backend
            const getData = await fetch("/api/data");
            
            if (!getData.ok) {
                throw new Error(`Server error: ${getData.status}`);
            }

            const data = await getData.json();
            resultData.textContent = JSON.stringify(data, null, 2)

        } catch (error) {
            console.error(error);
            resultData.textContent = `An error occurred: ${error.message}`;
        }
    });
});
