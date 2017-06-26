# --------------------------------------------------------------
#  By Miles R. Porter
#  Painted Harmony Group, Inc
#  June 26, 2017
#  Please See LICENSE.txt
# --------------------------------------------------------------

from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.tokenize import TweetTokenizer


class SentimentAnalyzer:

    classifier = None
    tknzr = TweetTokenizer()

    def __init__(self):
        def word_feats(words):
            return dict([(word, True) for word in words])

        negids = movie_reviews.fileids('neg')
        posids = movie_reviews.fileids('pos')

        negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
        posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]

        negcutoff = int(len(negfeats))
        poscutoff = int(len(posfeats))

        trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
        # testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
        print('Train based on %d documents.' % (len(trainfeats)))

        self.classifier = NaiveBayesClassifier.train(trainfeats)

    def analyze_sentiment(self, raw_text):
        tokenized_text = [self.tknzr.tokenize(raw_text)]
        txt = dict((t, True) for t in tokenized_text[0])
        results = self.classifier.classify(txt)
        return results