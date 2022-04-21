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


# This can be set to any corpus name to validate its contents
CORPUS_NAME = "tarot"


class Test001DataValidity(unittest.TestCase):
    """
    Valid data is important to how everything functions. Assertions
    here help to ensure that data files will not cause problems.
    """

    def setUp(self):
        self.file_name = "corpora/%s.json" % CORPUS_NAME
        with open(self.file_name) as json_file:
            self.loaded_data = json.load(json_file)

    def test_data_exists(self):
        self.assertTrue(exists(self.file_name))

    def test_raw_data_is_dict(self):
        self.assertIsInstance(self.loaded_data, dict)

    def test_valid_corpus_keyname(self):
        self.assertIn(CORPUS_NAME, self.loaded_data.keys())

    def test_corpus_data_is_list(self):
        self.assertIsInstance(self.loaded_data.get(CORPUS_NAME), list)

    def test_all_corpus_items_are_dicts(self):
        not_dicts = []
        for list_item in self.loaded_data.get(CORPUS_NAME):
            if not isinstance(list_item, dict):
                not_dicts.append(list_item)
        self.assertEqual(not_dicts, [])


class Test100ImportCorpus(unittest.TestCase):
    """
    Tests for the 'import_corpus' method.
    """
    def setUp(self):
        self.corpus_obj = corpora.CorpusObject()
        self.corpus_obj.import_corpus(CORPUS_NAME)

    def test_obj_can_import_something(self):
        self.assertGreater(len(self.corpus_obj), 0)

    def test_import_wipes_existing_data(self):
        first_len = len(self.corpus_obj)
        self.corpus_obj.import_corpus(CORPUS_NAME)
        second_len = len(self.corpus_obj)
        self.assertEqual(first_len, second_len)

    def test_imported_list_items_are_corpusrecords(self):
        not_corpusrecords = []
        for list_item in self.corpus_obj:
            if not isinstance(list_item, corpora.CorpusRecord):
                not_corpusrecords.append(list_item)
        self.assertEqual(not_corpusrecords, [])

    def test_import_sets_corpus_name(self):
        self.assertEqual(self.corpus_obj.name, CORPUS_NAME)


class Test200GetFieldMatches(unittest.TestCase):
    """
    Tests the 'get_field_matches' method of CorpusObject.
    """
    def setUp(self):
        self.corpus_obj = corpora.CorpusObject()
        self.corpus_obj.import_corpus(CORPUS_NAME)
        self.str_key_names = []
        self.list_key_names = []
        for key_name in self.corpus_obj[0].keys():
            if isinstance(self.corpus_obj[0].get(key_name), str):
                self.str_key_names.append(key_name)
            if isinstance(self.corpus_obj[0].get(key_name), list):
                self.list_key_names.append(key_name)


    def test_gfm_returns_known_match_in_list_field(self):
        field_name = self.list_key_names[0]
        known_match_strings = self.corpus_obj[0][field_name]
        results = self.corpus_obj.get_field_matches(
            field_name,
            [known_match_strings[0]]
        )
        self.assertGreater(len(results), 0)


    def test_gfm_returns_known_match_in_string_field(self):
        field_name = self.str_key_names[0]
        known_match_string = self.corpus_obj[0][field_name]
        results = self.corpus_obj.get_field_matches(
            field_name,
            [known_match_string]
        )
        self.assertGreater(len(results), 0)



class Test300GetCombinedListField(unittest.TestCase):
    """
    Tests for the 'get_combined_list_field' method.
    """
    def setUp(self):
        self.corpus_obj = corpora.CorpusObject()
        self.corpus_obj.import_corpus(CORPUS_NAME)
        self.str_key_names = []
        self.list_key_names = []
        for key_name in self.corpus_obj[0].keys():
            if isinstance(self.corpus_obj[0].get(key_name), str):
                self.str_key_names.append(key_name)
            if isinstance(self.corpus_obj[0].get(key_name), list):
                self.list_key_names.append(key_name)

    def test_gclf_results_contain_known_item(self):
        field_name = self.list_key_names[0]
        known_items = self.corpus_obj[0][field_name]
        self.assertIn(
            known_items[0],
            self.corpus_obj.get_combined_list_field(field_name)
        )


class Test400GetAllFieldValues(unittest.TestCase):
    """
    Tests for the 'get_all_field_values' method.
    """
    def setUp(self):
        self.corpus_obj = corpora.CorpusObject()
        self.corpus_obj.import_corpus(CORPUS_NAME)
        self.str_key_names = []
        self.list_key_names = []
        for key_name in self.corpus_obj[0].keys():
            if isinstance(self.corpus_obj[0].get(key_name), str):
                self.str_key_names.append(key_name)
            if isinstance(self.corpus_obj[0].get(key_name), list):
                self.list_key_names.append(key_name)

    def test_gafv_results_are_same_len_as_corpus(self):
        self.assertEqual(
            len(self.corpus_obj),
            len(self.corpus_obj.get_all_field_values(self.str_key_names[0]))
        )


class Test500CorpusRecord(unittest.TestCase):
    """Tests for the 'CorpusRecord' class"""
    def setUp(self):
        self.record_obj = corpora.CorpusRecord()

    def test_fresh_record_has_edges_attr_as_none(self):
        self.assertEqual(self.record_obj.edges, None)

    def test_record_can_add_to_blank_edges_attr(self):
        self.record_obj.add_edge("test.fieldspace", 0)
        self.assertEqual(
            self.record_obj.edges,
            {"test.fieldspace": [0]}
        )

    def test_record_can_add_edge_to_existing_fieldspace(self):
        self.record_obj.add_edge("test.fieldspace", 0)
        self.record_obj.add_edge("test.fieldspace", 1)
        self.assertEqual(
            self.record_obj.edges,
            {"test.fieldspace": [0, 1]}
        )

    def test_record_can_add_edges_with_multiple_fieldspaces(self):
        self.record_obj.add_edge("test.fieldspace", 0)
        self.record_obj.add_edge("other.fieldspace", 0)
        self.assertEqual(
            self.record_obj.edges,
            {"test.fieldspace": [0], "other.fieldspace": [0]}
        )

    def test_record_can_remove_single_edge(self):
        self.record_obj.add_edge("test.fieldspace", 0)
        self.record_obj.add_edge("test.fieldspace", 1)
        self.record_obj.rem_edge("test.fieldspace", 1)
        self.assertEqual(
            self.record_obj.edges,
            {"test.fieldspace": [0]}
        )

    def test_removing_the_only_edge_sets_attr_to_none(self):
        self.record_obj.add_edge("test.fieldspace", 1)
        self.record_obj.rem_edge("test.fieldspace", 1)
        self.assertEqual(self.record_obj.edges, None)


class Test600CompendiumObject(unittest.TestCase):
    """Tests for the 'CompendiumObject' class"""

    def setUp(self):
        self.compendium = corpora.CompendiumObject()

    def test_compendium_can_import_all_json_files(self):
        self.compendium.add_all_corpora()
        self.assertGreater(len(compendium.keys()), 0)

    def test_compendium_can_import_single_corpus_by_name(self):
        self.compendium.add_corpus(CORPUS_NAME)
        self.assertIn(CORPUS_NAME, compendium.keys())

    def PLACEHOLDER_test_compendium_can_generate_adjacency_list(self):
        """I don't know how to test this yet."""
        pass


if __name__ == '__main__':
    with open('banner.txt', 'r') as f:
        print(f.read())
    banner = '''
    _   _   _   _
   / \\ / \\ / \\ / \\
  ( U | N | I | T )
   \\_/ \\_/ \\_/ \\_/
  _   _   _   _   _
 / \\ / \\ / \\ / \\ / \\
( T | E | S | T | S )
 \\_/ \\_/ \\_/ \\_/ \\_/

for corpora.py and data validation
'''
    print(banner)
    unittest.main()
