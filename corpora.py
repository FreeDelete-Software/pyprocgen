"""
Utilities for handling corpora json files.

Example data is provided under CC0 terms here:
https://github.com/FreeDelete-Software/corpora

Important notes on data files:

- JSON data is intended to be covered under separate copyright terms.
- All JSON files should be stored in the 'corpora' directory.
- Data files which are improperly formatted *will* cause issues. 
- The unit tests in test_corpora.py perform some basic sanity checks on data.
"""

import json

class CorpusObject(list):
    """
    Object which represents the contents of a corpus. 
    """

    def import_corpus(self, corpus_name):
        """
        Imports a corpus by name into the object.

        !NOTE! - This won't work if you specify a path or extension. 

        Importing my_corpus.json would look like this:
        my_corpus_object.import_corpus("my_corpus")
        """
        filename = "corpora/%s.json" % corpus_name
        with open(filename) as json_file:
            corpus = json.load(json_file)

        # Clear Existing contents
        self.clear()

        # Extend the data into self.
        self.extend(corpus.get(corpus_name))

        # Set attributes
        self.description = corpus.get("description")


    def get_records_with_list_items(self, key_name, match_list):
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


    def get_all_list_items_combined(self, key_name):
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


    def get_values_in_key(self, key_name):
        """
        Returns a list of values from all records stored in a specified <key_name>
        """
        results = []
        for record in self:
            results.append(record[key_name])
        return results


