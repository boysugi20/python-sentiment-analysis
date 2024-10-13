import sys
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import BertTokenizer, BertForSequenceClassification, pipeline

# Function for TextBlob sentiment analysis
def analyze_sentiment_textblob(feedback):
    analysis = TextBlob(feedback)
    if analysis.sentiment.polarity > 0:
        return 'Positive', analysis.sentiment.polarity
    elif analysis.sentiment.polarity == 0:
        return 'Neutral', analysis.sentiment.polarity
    else:
        return 'Negative', analysis.sentiment.polarity

# Function for VADER sentiment analysis
def analyze_sentiment_vader(feedback):
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(feedback)
    if sentiment['compound'] >= 0.05:
        return 'Positive', sentiment['compound']
    elif sentiment['compound'] <= -0.05:
        return 'Negative', sentiment['compound']
    else:
        return 'Neutral', sentiment['compound']

# Function for BERT sentiment analysis
def analyze_sentiment_bert(feedback):
    model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertForSequenceClassification.from_pretrained(model_name)
    sentiment_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
    
    result = sentiment_pipeline(feedback)

    label = result[0]['label']
    score = result[0]['score']
    
    # Mapping logic
    if "1 star" in label or "2 stars" in label:
        sentiment = "Negative"
    elif "3 stars" in label:
        sentiment = "Neutral"
    elif "4 stars" in label or "5 stars" in label:
        sentiment = "Positive"
    else:
        sentiment = "Unknown"
        
    return sentiment, score

# Main function to drive the script
def main():

    feedback = input("Enter the feedback text: ")
    
    sentiment, score = analyze_sentiment_textblob(feedback)
    print(f"TextBlob Sentiment: {sentiment} | Score: {score:.4f}")

    sentiment, score = analyze_sentiment_vader(feedback)
    print(f"VADER Sentiment: {sentiment} | Score: {score:.4f}")

    sentiment, score = analyze_sentiment_bert(feedback)
    print(f"BERT Sentiment: {sentiment} | Score: {score:.4f}")

if __name__ == "__main__":
    main()
