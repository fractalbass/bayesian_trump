import pandas as pd
import matplotlib
from pylab import *
import TrumpTweetUtilities


class TrumpFreqAnalizer:

    def run(self):
        dt = pd.read_csv("./data/realdonaltrump-fullarchive.csv")
        util = TrumpTweetUtilities.TrumpTweetUtilities()
        counts_df = util.test_count_rows_group_by_date(dt,"created_at")
        print(counts_df)
        counts_df.plot(kind="line")
        plt.show(block=True)

tfa = TrumpFreqAnalizer()
tfa.run()
