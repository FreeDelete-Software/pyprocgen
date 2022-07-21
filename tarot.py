""""
tarot.py
========

Script interface for the tarot corpus.

"""

import corpora

# Set up the CorpusObject
card_corpus = corpora.CorpusObject()
card_corpus.import_corpus("tarot")


def get_data_from_cardnames(names_list: list):
    """
    Returns raw data (as list of dicts) for the given list of <names_list>
    """
    matching_cards = card_corpus.get_field_matches("name", names_list)
    return matching_cards
