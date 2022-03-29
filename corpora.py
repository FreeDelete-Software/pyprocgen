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


    def where_list_key_contains_any(self, key_name, match_list):
        """
        Returns records with a list stored in a given <key_name> that
        contains any *exact* items in a given <match_list>.
        """
        results = []
        for record in self:
            for item in match_list:
                if (item in record[key_name]) and not (record in results):
                        results.append(record)
        return results


    def combine_all_lists(self, key_name):
        """
        Combines lists from all records stored in a given <key_name>.
        """
        results = []
        for record in self:
            for item in record[key_name]:
                if not (item in results):
                    results.append(item)
        results.sort()
        return results
