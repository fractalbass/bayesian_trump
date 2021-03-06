#--------------------------------------------------------------
#  By Miles R. Porter
#  Painted Harmony Group, Inc
#  June 22, 2017
#  Please See LICENSE.txt
#--------------------------------------------------------------

import pandas as pd
import dateparser
import datetime

class TrumpTweetUtilities():

    def count_rows_group_by_date(self, dataframe, date_col):
        #df = pd.DataFrame(dataframe[date_col].astype("datetime64"))
        counts = dataframe.groupby(dataframe[date_col].dt.date).count()
        dateArray = []
        countArray = []
        for index, row in counts.iterrows():
            dateArray.append(index)
            countArray.append(row[-1])

        newdf = pd.DataFrame(index=dateArray, data=countArray)
        newdf.columns = ["count"]

        return newdf

    def sum_columns_in_grouped_rows_by_date(self, dataframe, date_col):
        dataframe["created_at"] = dataframe["created_at"].apply(lambda x: self.tryConvert(x))
        pos_counts = dataframe.groupby(dataframe[date_col]).agg({'pos':['sum','count']})
        neg_counts = dataframe.groupby(dataframe[date_col]).agg({'neg':['sum','count']})
        d = {"count": pos_counts["pos"]["count"].values,
             "pos": pos_counts["pos"]["sum"].values,
             "neg": neg_counts["neg"]["sum"].values}
        newdf = pd.DataFrame(d, index=pos_counts.index)
        return newdf

    def tryConvert(self, x):
        duh = None
        if isinstance(x, datetime.datetime):
            duh = x.date()
        else:
            try:
                duh = dateparser.parse(x).date()
            except:
                print("Failed to parse {0} ".format(x))
        return duh

