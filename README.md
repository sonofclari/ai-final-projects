# Final Project

A web application that uses IBM Watson NLP to detect emotions in text. Users enter a statement and the app returns scores for five emotions — anger, disgust, fear, joy, and sadness — along with the dominant emotion.

## How It Works

The app sends the input text to the Watson NLP EmotionPredict API and parses the response into a structured format. A Flask server handles routing and serves the results to the browser as a formatted, human-readable string.

**Example output:**

```
For the given statement, the system response is 'anger': 0.006274985, 'disgust': 0.0025598293, 'fear': 0.009251528, 'joy': 0.9680386, 'sadness': 0.049744144. The dominant emotion is joy.
```

## Tech Stack

- **Python / Flask** — backend server and routing
- **IBM Watson NLP** — emotion prediction API
- **HTML / JavaScript** — frontend UI
- **Bootstrap 4** — styling

## Project Structure

```
oaqjp-final-project-emb-ai/
│
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py      # Watson NLP API call + response parsing
│
├── static/
│   └── mywebscript.js            # Frontend logic (XHR request + DOM update)
│
├── templates/
│   └── index.html                # Main UI page
│
├── server.py                     # Flask app with /emotionDetector route
├── test_emotion_detection.py     # Unit tests
└── README.md
```

## Getting Started

1. **Install dependencies**
   
   ```bash
   pip install flask requests
   ```
1. **Run the server**
   
   ```bash
   python server.py
   ```
1. **Open the app** in your browser at `http://localhost:5000`

## API Endpoint

|Method|Route                                  |Description                       |
|------|---------------------------------------|----------------------------------|
|GET   |`/`                                    |Serves the main UI                |
|GET   |`/emotionDetector?textToAnalyze=<text>`|Returns formatted emotion analysis|

## License

Apache 2.0 — see <LICENSE> for details.
