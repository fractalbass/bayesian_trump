# bayesian_trump

This repo contains various scripts and test that demonstrate bayesian analysis of
trumps by President Donald Trump.  This repository is referenced by a blog post:

[http://datascience.netlify.com/general/2017/06/30/data_science_6.html]()

The code "pipeline" is intended to work like this:

realdonaldtrump-fullaarchive.csv -> TrumpCountDailySummarizer.py -> trump_daily_counts.csv ->
TrumpCountAnalyzer.py -> Graphs for Trump Daily Tweet Counts

Similarly, the code "pipeline" for analyzing the tweet Sentiments is:

realdonaldtrump-fullarchive.csv -> TrumpSentimentDailySummarizer.py -> trump_sentiment_daily_counts.csv ->
TrumpCountAnalyzer.py -> Graph for Trump Daily Tweet Sentiment Counts

