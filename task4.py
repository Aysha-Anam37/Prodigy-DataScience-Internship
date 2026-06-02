import pandas as pd
import matplotlib.pyplot as plt

data = {'Post_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Platform': ['Instagram', 'Twitter', 'Facebook', 'Instagram', 'Twitter',
        'Facebook', 'Instagram', 'Twitter', 'Facebook', 'Instagram'],
    'Brand': ['Nike', 'Apple', 'Nike', 'Samsung', 'Apple',
        'Samsung', 'Nike', 'Apple', 'Samsung', 'Nike'],
    'Topic': [
        'Shoes', 'iPhone', 'Sports', 'Mobile', 'MacBook',
        'Galaxy', 'Fitness', 'AirPods', 'Camera', 'Running'],
    'Sentiment': [
        'Positive', 'Negative', 'Positive', 'Neutral', 'Positive',
        'Negative', 'Positive', 'Neutral', 'Positive', 'Negative'],
    'Likes': [450, 210, 520, 300, 680, 190, 740, 410, 560, 250],
    'Comments': [45, 18, 60, 27, 80, 15, 92, 38, 55, 22]}

df = pd.DataFrame(data)
print(df.head())

plt.figure(figsize=(8,6))
df['Sentiment'].value_counts().plot(kind='bar',color=['lightgreen', 'lavender', 'salmon'],
    edgecolor='black')
plt.title('Overall Sentiment Distribution', fontsize=14)
plt.xlabel('Sentiment')
plt.ylabel('Number of Posts')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig("sentiment_distribution.png", dpi=300)
plt.show()

brand_sentiment = pd.crosstab(df['Brand'],df['Sentiment'])
brand_sentiment.plot(kind='bar',figsize=(10,6),color=['salmon', 'lavender', 'lightgreen'],
    edgecolor='black')
plt.title('Brand-wise Sentiment Analysis', fontsize=14)
plt.xlabel('Brand')
plt.ylabel('Number of Posts')
plt.xticks(rotation=0)
plt.legend(title='Sentiment')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig("brand_sentiment_analysis.png", dpi=300)
plt.show()

plt.figure(figsize=(8,6))
df.groupby('Sentiment')['Likes'].mean().plot(kind='bar',color=['salmon', 'lavender', 'lightgreen'],
    edgecolor='black')
plt.title('Average Likes by Sentiment', fontsize=14)
plt.xlabel('Sentiment')
plt.ylabel('Average Likes')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig("likes_by_sentiment.png", dpi=300)
plt.show()