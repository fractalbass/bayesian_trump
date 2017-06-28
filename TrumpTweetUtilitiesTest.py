#--------------------------------------------------------------
#  By Miles R. Porter
#  Painted Harmony Group, Inc
#  June 22, 2017
#  Please See LICENSE.txt
#--------------------------------------------------------------

import TrumpTweetUtilities
import pandas as pd
import unittest
import datetime

class TrumpTweetUtilitiesTest(unittest.TestCase):

    testData = pd.read_csv("./data/testdata.csv")

    def test_count_rows_group_by_date(self):
        ttu = TrumpTweetUtilities.TrumpTweetUtilities()
        c = ttu.test_count_rows_group_by_date(self.testData, 'created_at')
        self.assertIsNotNone(c, msg="Returned index is none.")
        self.assertTrue(c.loc[datetime.date(2017,6,25),"count"] == 3)
        self.assertTrue(c.loc[datetime.date(2017,6,26),"count"] == 4)
        self.assertTrue(c.loc[datetime.date(2017,6,27),"count"] == 3)

    def test_sum_column_in_grouped_rows_by_date(self):
        pass


# Dataframe is:

#date, tweet, someval

