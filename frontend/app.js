// Function to simulate updating QoS suggestions (you can replace this with API calls)
function updateSuggestions() {
    // Example values (these would come from your model or backend)
    const predictedSatisfaction = Math.random().toFixed(2); // Random value between 0 and 1
    let suggestedAction = '';

    // Determine suggested action based on satisfaction value
    if (predictedSatisfaction < 0.3) {
        suggestedAction = 'Adjust bitrate or resolution';
    } else if (predictedSatisfaction < 0.6) {
        suggestedAction = 'Check network stability';
    } else {
        suggestedAction = 'All good! Continue streaming';
    }

    // Update the HTML with the new values
    document.getElementById('predicted-satisfaction').innerText = predictedSatisfaction;
    document.getElementById('suggested-action').innerText = suggestedAction;
}