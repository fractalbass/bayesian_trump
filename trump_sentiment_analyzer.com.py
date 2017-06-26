import nltk.classify.util
import pandas
import SentimentAnalyzer

#Load the trump tweets and classify each.
df = pandas.read_csv("/Users/milesporter/data-science/bayesian-trump/realdonaltrump-fullarchive.csv")
tweet_txt = df["text"]
analyzer = SentimentAnalyzer.SentimentAnalyzer()

pos_sentiment = []
neg_sentiment = []

for tweet in tweet_txt:
    results = analyzer.analyze_sentiment(tweet)
    print("{0}: {1}".format(results,tweet))
    pos_sentiment.append(int(results=="pos"))
    neg_sentiment.append(int(results=="neg"))

df["pos"] = pos_sentiment
df["neg"] = neg_sentiment

print(df[["created_at","text","pos","neg"]])
df[["created_at","text","pos","neg"]].to_csv("/Users/milesporter/data-science/bayesian-trump/sentiment_analyzed.csv")
print("Complete.")