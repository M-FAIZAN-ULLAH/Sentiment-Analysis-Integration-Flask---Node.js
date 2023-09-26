import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from flask import Flask, request, jsonify

nltk.download('vader_lexicon')

app = Flask(__name__)
sia = SentimentIntensityAnalyzer()

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.json
    text = data.get('text', '')

    scores = sia.polarity_scores(text)
    compound_score = scores['compound']
    
    sentiment = 'positive' if compound_score >= 0 else 'negative'
    result = {'sentiment': sentiment, 'probability' : compound_score}

    return jsonify(result)

if __name__ == '__main__':
    app.run()
