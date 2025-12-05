document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("data");
    const resultData = document.getElementById("latest_data");
    const rawData = document.getElementById("raw_data");

    button.addEventListener("click", async () => {
        resultData.textContent = "Loading...";

        try {
            // Make a request to Flask backend
            const getData = await fetch("/api/data");
            
            if (!getData.ok) {
                throw new Error(`Server error: ${getData.status}`);
            }

            const data = await getData.json();
            resultData.textContent = "Daily Rain In: " + data.dailyrainin + " | " + "Date: " + data.date + " | " + "Feels Like: " + data.feelsLike + " | " + "Dew Point: " + data.dewPoint + " | " + "Humidity: " + data.humidity + " | " + "Last Rain Date: " + data.lastRain + " | " + "Temperature in Fahrenheit: " + data.tempf;

            rawData.textContent = JSON.stringify(data, null, 2)
// { "baromabsin": 29.75, "baromrelin": 29.75, "dailyrainin": 0, "date": "2025-10-09T11:21:00.000Z", "dateutc": 1760008860000, "dewPoint": 31.99, "fao_penman": -0.16903705541809788, "feelsLike": 33.8, "hourlyrainin": 0, "humidity": 93, "lastRain": "2025-10-07T21:06:00.000Z", "leafwet1x": 0, "leafwetday": 0, "leafwetsum": 0, "sds": "0", "sis": "0", "solarradday": 0, "solarradiation": 0, "tempf": 33.8, "trustdevicetime": "1", "tz": "America/Detroit", "winddir": 343, "windgustmph": 0, "windspeedmph": 0 }

        } catch (error) {
            console.error(error);
            resultData.textContent = `An error occurred: ${error.message}`;
        }
    });
});
