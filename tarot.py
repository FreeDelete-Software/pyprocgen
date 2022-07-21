""""
tarot.py
========

Script interface for the tarot corpus.

"""

import corpora

# Set up the CorpusObject
card_corpus = corpora.CorpusObject()
card_corpus.import_corpus("tarot")


def get_data_from_cardname(card_name):
    print("Your input was: %s" % card_name )
