import pandas as pd
import matplotlib
from pylab import *

class TrumpFreqAnalizer:

    def run(self):
        dt = pd.read_csv("realdonaltrump-fullarchive.csv")
        df = pd.DataFrame(dt["created_at"].astype("datetime64"))
        #df.groupby(df["date"]).count().plot(kind="bar")
        graph = df.groupby(df["created_at"].dt.date).count()
        graph["pos"] = df[[graph]]["pos"].sum()
        # Display everything.  Because we are running this in pycharm, we set block to TRUE.  This
        # prevents the map window from closing right away.
        graph.plot(kind="line")
        plt.show(block=True)

tfa = TrumpFreqAnalizer()
tfa.run()
