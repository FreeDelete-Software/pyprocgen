"""
Utilities for handling corpora json files.
"""

import json

class CorpusObject(list):
    """
    Object which represents the contents of a corpus. 
    """

    def import_corpus(self, corpus_name):
        """
        Imports a corpus by name into the object.

        !NOTE! - This won't work if you specify a file extension or use
        improperly formatted files.

        For example:
        'my_corpus.json' should contain a dictionary (hash table) which has
        a 'description' key with a string-type value and a 'my_corpus' key 
        with a list(array)-type value. The json file should be in the same
        directory as this module.

        Importing this file would look like this:
        CorpusObject.import_corpus("my_corpus")
        """
        filename = "corpora/%s.json" % corpus_name
        with open(filename) as json_file:
            corpus = json.load(json_file)

        # Extend the interpretations list into self.
        self.extend(corpus.get(corpus_name))

        # Set attributes
        self.description = corpus.get("description")

