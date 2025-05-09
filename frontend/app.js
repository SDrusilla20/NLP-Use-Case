// Initialize sentiment counts (these will be updated dynamically)
let sentimentCounts = {
    Positive: 0,
    Neutral: 0,
    Negative: 0
};

// Function to update the sentiment bar chart
function createSentimentChart() {
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

function updateSuggestions() {
    // Generate a random satisfaction score
    const predictedSatisfaction = Math.random().toFixed(2); // Value between 0 and 1
    let sentimentLabel = '';
    let suggestedAction = '';

    // Derive sentiment and action from satisfaction score
    if (predictedSatisfaction < 0.4) {
        sentimentLabel = 'Negative';
        suggestedAction = 'Adjust bitrate or resolution';
        sentimentCounts.Negative++;
    } else if (predictedSatisfaction < 0.8) {
        sentimentLabel = 'Neutral';
        suggestedAction = 'Check network stability';
        sentimentCounts.Neutral++;
    } else {
        sentimentLabel = 'Positive';
        suggestedAction = 'All good! Continue streaming';
        sentimentCounts.Positive++;
    }

    // Update the dashboard
    document.getElementById('predicted-satisfaction').innerText = predictedSatisfaction;
    document.getElementById('suggested-action').innerText = suggestedAction;
    document.getElementById('sentiment').innerText = sentimentLabel;

}

// Initial chart render (before simulating updates)
createSentimentChart();