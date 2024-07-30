import matplotlib.pyplot as plt

# Sentiment analysis results
texts = ["I love this product! It's amazing.", "This movie is terrible.", "The weather is so-so."]
compound_scores = [0.7096, -0.4767, 0.0]
positive_scores = [0.706, 0.0, 0.0]
negative_scores = [0.0, 0.638, 0.0]
neutral_scores = [0.294, 0.362, 1.0]
sentiments = ["Positive", "Negative", "Neutral"]

# Plot the sentiment scores in a bar graph
plt.figure(figsize=(10, 6))
plt.bar(texts, compound_scores, label='Compound Score')
plt.bar(texts, positive_scores, label='Positive Score')
plt.bar(texts, negative_scores, label='Negative Score')
plt.bar(texts, neutral_scores, label='Neutral Score')
plt.xlabel('Texts')
plt.ylabel('Sentiment Scores')
plt.title('Sentiment Analysis Results')
plt.legend()
plt.xticks(rotation=45)
plt.show()
