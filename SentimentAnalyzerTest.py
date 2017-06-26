#--------------------------------------------------------------
#  By Miles R. Porter
#  Painted Harmony Group, Inc
#  June 26, 2017
#  Please See LICENSE.txt
#--------------------------------------------------------------

import unittest
import SentimentAnalyzer as analyzer


class SentimentAnalyzerTest(unittest.TestCase):

    def test_analyze_sentiment(self):

        sa = analyzer.SentimentAnalyzer()

        self.assertTrue(sa.analyze_sentiment("This is a happy tweet.  Have a nice day.")=="pos")
        self.assertTrue(sa.analyze_sentiment("I am angry.  He is very disonest.  Sad.")=="neg")

