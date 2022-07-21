"""
test_tarot.py
=============

Unit tests for tarot.py. Requires corpora JSON data.

"""

import unittest
import tarot


# REMINDER:
# The current "list of dictionaries" structure that was adopted from the
# copied tarot data is somewhat confusing and may need to be changed. It might
# be best to make corpora.CorpusObject() into a dict. More research needed.

class Test100GetDataFromCardnames(unittest.TestCase):
    def setUp(self):
        self.the_data = tarot.get_data_from_cardnames(["The Fool"])

    def test_returned_data_is_dict(self):
        self.assertIsInstance(self.the_data, list)


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

     for tarot.py
'''
    print(banner)
    unittest.main()
