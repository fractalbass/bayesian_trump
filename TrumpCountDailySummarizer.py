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

class TrumpFreqAnalizer:

    def run(self):
        dt = pd.read_csv("./data/realdonaldtrump-fullarchive.csv")
        util = TrumpTweetUtilities.TrumpTweetUtilities()
        counts_df = util.count_rows_group_by_date(dt,"created_at")

        #Sentiment stuff here.


        print(counts_df)
        counts_df.plot(kind="line")
        counts_df.to_csv("./data/trump_daily_counts.csv")
        plt.show(block=True)

tfa = TrumpFreqAnalizer()
tfa.run()
