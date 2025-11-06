// Simplified logic
let cumulative_ET0 = 0;  // Reset after each irrigation/rain
let THRESHOLD = 35;       // mm (adjustable: 30-40 range)

// Daily update
cumulative_ET0 += daily_ET0;

if (cumulative_ET0 >= THRESHOLD) {
    recommend_irrigation = true;
    // After irrigation, reset:
    cumulative_ET0 = 0;
} else {
    recommend_irrigation = false;
}