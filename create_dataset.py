import pandas as pd
import random
import numpy as np

comments_positive = [
    "Amazing gameplay and no lag at all!",
    "Loved the stream quality, keep it up!",
    "Great commentary and visuals!",
    "I’m having a blast watching this!",
    "Everything is perfect, thanks!",
]

comments_negative = [
    "Too much buffering, not enjoyable.",
    "Audio was off sync. Please fix!",
    "Stream kept freezing every few minutes.",
    "The video quality is poor.",
    "Network is causing delays.",
]

neutral_comments = [
    "Stream is okay.",
    "Nothing special, just another game.",
    "Mediocre experience.",
    "Decent audio but poor video.",
    "Could be better, could be worse."
]

network_conditions = ['Excellent', 'Good', 'Moderate', 'Poor', 'Very Poor']
stream_quality = ['1080p', '720p', '480p', '360p']

def random_satisfaction(comment):
    if comment in comments_positive:
        return round(random.uniform(0.8, 1.0), 2)
    elif comment in comments_negative:
        return round(random.uniform(0.0, 0.4), 2)
    else:
        return round(random.uniform(0.4, 0.8), 2)

data = []
for _ in range(2000):
    category = random.choices(['positive', 'negative', 'neutral'], weights=[0.4, 0.4, 0.2])[0]
    if category == 'positive':
        comment = random.choice(comments_positive)
    elif category == 'negative':
        comment = random.choice(comments_negative)
    else:
        comment = random.choice(neutral_comments)
    
    net_cond = random.choice(network_conditions)
    quality = random.choice(stream_quality)
    satisfaction = random_satisfaction(comment)
    
    # Add some random noise
    satisfaction += np.random.normal(0, 0.05)
    satisfaction = min(max(satisfaction, 0.0), 1.0)
    
    data.append([comment, net_cond, quality, round(satisfaction, 2)])

df = pd.DataFrame(data, columns=['comment', 'network', 'quality', 'satisfaction'])
df.to_csv('noisy_stream_data.csv', index=False)
print("Dataset created.")
