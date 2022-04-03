"""
Test module for corpora.py. Also validates data files.

!NOTE! - Requires data not included with pyprocgen.
Compatible (and CC0-licensed) data is available here:
https://github.com/FreeDelete-Software/corpora
"""
import unittest
import corpora

from os.path import exists
import json


# This should be set to a *compatible* corpus name with a more complex structure.
DEFAULT_CORPUS = "tarot"


class TestDataValidity(unittest.TestCase):
    """
    Valid data is important to how everything functions. Assertions
    here help to ensure that data files will not cause problems.
    """

    def setUp(self):
        self.file_name = "corpora/%s.json" % DEFAULT_CORPUS
        with open(self.file_name) as json_file:
            self.loaded_data = json.load(json_file)

    def test_data_exists(self):
        self.assertTrue(exists(self.file_name))

    def test_raw_data_is_dict(self):
        self.assertIsInstance(self.loaded_data, dict)

    def test_valid_corpus_keyname(self):
        self.assertIn(DEFAULT_CORPUS, self.loaded_data.keys())

    def test_corpus_data_is_list(self):
        self.assertIsInstance(self.loaded_data.get(DEFAULT_CORPUS), list)

    def test_first_corpus_item_is_dict(self):
        this_corpus = self.loaded_data.get(DEFAULT_CORPUS)
        self.assertIsInstance(this_corpus[0], dict)


class TestCorpusObjectImport(unittest.TestCase):

    def setUp(self):
        self.corpus_obj = corpora.CorpusObject()

    def test_obj_can_import_valid_corpus(self):
        self.corpus_obj.import_corpus(DEFAULT_CORPUS)
        self.assertGreater(len(self.corpus_obj), 0)


if __name__ == '__main__':

    banner = '''
                                                                   
                 ____  __  ______  _________  _________ ____  ____ 
                / __ \\/ / / / __ \\/ ___/ __ \\/ ___/ __ `/ _ \\/ __ \\
               / /_/ / /_/ / /_/ / /  / /_/ / /__/ /_/ /  __/ / / /
              / .___/\\__, / .___/_/   \\____/\\___/\\__, /\\___/_/ /_/ 
             /_/    /____/_/                    /____/
                      _   _   _   _     _   _   _   _   _  
                     / \\ / \\ / \\ / \\   / \\ / \\ / \\ / \\ / \\ 
                    ( U | N | I | T ) ( T | E | S | T | S )
                     \\_/ \\_/ \\_/ \\_/   \\_/ \\_/ \\_/ \\_/ \\_/
                      for corpora.py and data validation
'''
    print(banner)
    unittest.main()
