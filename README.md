# RA2212704010013
# Live Streaming QoS Dashboard

This project provides a complete NLP-based pipeline to simulate, analyze, and visualize **Quality of Service (QoS)** for live video game streaming platforms. It uses a **data-driven approach** leveraging big data simulation, **BERT-based sentiment analysis**, and **PyTorch-based deep neural networks** to classify user satisfaction levels.

## 🧠 Project Highlights

- ✅ Synthetic noisy data generation simulating live stream conditions
- ✅ BERT-based sentiment analysis using HuggingFace Transformers
- ✅ Deep Neural Network (DNN) regression model built with PyTorch
- ✅ Dashboard frontend showing confusion matrix and satisfaction suggestions

---

## 📁 Project Structure

| File | Description |
|------|-------------|
| `create_noisy_dataset.py` | Generates a realistic + noisy dataset simulating network, quality, and sentiment |
| `sentiment_analysis.py` | Analyzes textual feedback using BERT and adds a sentiment label |
| `dnn_classifier.py` | Trains a PyTorch-based regression model to predict user satisfaction |
| `realtime_qos_simulation.py` | Loads the model and makes satisfaction predictions on sample inputs |
| `visualize_results.py` | Creates and saves a confusion matrix image for model predictions |
| `index.html` | Simple HTML dashboard displaying confusion matrix and suggestions |
| `style.css` | CSS file for styling the dashboard UI |
| `app.js` | (Optional) JS to simulate UI updates (not used in static version) |
| `confusion_matrix.png` | Saved visualization of prediction accuracy |

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/qos-streaming-dashboard.git
cd qos-streaming-dashboard
```

### 2. Install dependencies

Ensure you're using Python 3.13+, and install the required Python packages:

```bash
pip install pandas scikit-learn torch matplotlib transformers
```

### 3. Run the pipeline step-by-step

```bash
# Step 1: Generate dataset
python create_noisy_dataset.py

# Step 2: Analyze sentiment using BERT
python sentiment_analysis.py

# Step 3: Train the PyTorch model
python dnn_pytorch.py

# Step 4: Predict satisfaction (simulate real-time)
python realtime_predict.py

# Step 5: Visualize model results
python visualize_results.py
```

This will generate `confusion_matrix.png` used in the dashboard.

## 🌐 Frontend Dashboard

A simple HTML/CSS dashboard to display:
- The confusion matrix image
- Simulated QoS suggestion output

### How to Use

1. Place these files in the same folder:
   - `index.html`
   - `style.css`
   - `confusion_matrix.png`
2. Open `index.html` in your web browser.
3. No live backend or JavaScript updates are required—this is a static display dashboard.

## 📊 Sample Output

```
Predicted satisfaction: 0.28
→ Suggested action: Adjust bitrate or resolution
```

## 💡 Future Improvements

- Real-time feedback integration via Flask or FastAPI
- Interactive dashboard with live updates
- Integration with actual streaming platforms
- Expanded machine learning model with more features

## License

This project is licensed under the MIT License - see the LICENSE file for details.
