# --------------------------------------------------------------
#  By Miles R. Porter
#  Painted Harmony Group, Inc
#  June 27, 2017
#  Please See LICENSE.txt
# --------------------------------------------------------------

import pandas
import SentimentAnalyzer

#Load the trump tweets and classify each.
df = pandas.read_csv("./data/realdonaldtrump-fullarchive.csv", parse_dates=["created_at"])
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

#Save off the trump dataframe with the pos and neg fields for each tweet
df[["created_at","text","pos","neg"]].to_csv("/Users/milesporter/data-science/bayesian-trump/sentiment_analyzed3.csv")
print("Complete.")
