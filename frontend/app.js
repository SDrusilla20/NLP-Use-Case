// Initialize sentiment counts (these will be updated dynamically)
let sentimentCounts = {
    Positive: 0,
    Neutral: 0,
    Negative: 0
};

// Function to update the sentiment bar chart
function updateSentimentChart() {
    const ctx = document.getElementById('sentimentChart').getContext('2d');

    // Create or update the sentiment chart
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Positive', 'Neutral', 'Negative'], // Sentiment types
            datasets: [{
                label: 'Sentiment Distribution',
                data: [sentimentCounts.Positive, sentimentCounts.Neutral, sentimentCounts.Negative],
                backgroundColor: ['#4CAF50', '#FFC107', '#F44336'],
                borderColor: ['#388E3C', '#FF9800', '#F44336'],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Function to simulate updating QoS suggestions and sentiment data
function updateSuggestions() {
    // Example values for QoS suggestions
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

    // Simulate sentiment data (for real-time updates)
    const randomSentiment = Math.random();
    if (randomSentiment < 0.3) {
        sentimentCounts.Positive++;
    } else if (randomSentiment < 0.7) {
        sentimentCounts.Neutral++;
    } else {
        sentimentCounts.Negative++;
    }

    // Update the sentiment chart after data change
    updateSentimentChart();
}

// Initial chart render (before simulating updates)
updateSentimentChart();