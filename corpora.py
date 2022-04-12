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
            corpus_file = json.load(json_file)

        # Clear Existing contents
        self.clear()

        # Convert data items to CorpusRecord class
        for item in corpus_file.get(corpus_name):
            if isinstance(item, dict):
                record = CorpusRecord(item)
                self.append(record)

        # Set attributes
        self.description = corpus_file.get("description")


    def get_field_matches(self, field_name, match_list):
        """
        Returns records with a given <field_name> that
        contains any *exact* items in a given <match_list>.
        """
        results = []
        for record in self:
            for item in match_list:
                if (item in record[field_name]) and not (record in results):
                        results.append(record)
        return results


    def get_combined_list_field(self, field_name):
        """
        Combines lists from all records stored in a given <field_name>.
        """
        results = []
        for record in self:
            for item in record[field_name]:
                if not (item in results):
                    results.append(item)
        results.sort()
        return results


    def get_all_field_values(self, field_name):
        """
        Returns a list of values from all records stored in a specified <field_name>
        """
        results = []
        for record in self:
            results.append(record[field_name])
        return results


class CorpusRecord(dict):
    """Currently just a placeholder"""
    pass
