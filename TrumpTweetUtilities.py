import pandas as pd

class TrumpTweetUtilities():

    def test_count_rows_group_by_date(self, dataframe, date_col):
        df = pd.DataFrame(dataframe[date_col].astype("datetime64"))
        counts = df.groupby(df[date_col].dt.date).count()
        dateArray = []
        countArray = []
        for index, row in counts.iterrows():
            dateArray.append(index)
            countArray.append(row[-1])

        newdf = pd.DataFrame(index=dateArray, data=countArray)
        newdf.columns = ["count"]

        return newdf

    def test_sum_column_in_grouped_rows_by_date(self, dataframe, date_col, value_col):
        return