#--------------------------------------------------------------
#  By Miles R. Porter
#  Painted Harmony Group, Inc
#  June 28, 2017
#  Please See LICENSE.txt
#--------------------------------------------------------------

import pandas as pd
import matplotlib
from pylab import *
import TrumpTweetUtilities
import dateutil
import datetime

class TrumpSentimentAnalyzer:

    def run(self):
        df = pd.read_csv("./data/sentiment_analyzed3.csv", engine="python", parse_dates=["created_at"])
        #print(df)
        util = TrumpTweetUtilities.TrumpTweetUtilities()
        counts_df = util.sum_columns_in_grouped_rows_by_date(df,"created_at")
        #print(counts_df)
        #counts_df.plot(kind="line")
        counts_df.to_csv("./data/trump_sentiment_daily_counts.csv")
        counts_df.plot(kind="bar")
        plt.show(block=True)

tsa = TrumpSentimentAnalyzer()
tsa.run()
