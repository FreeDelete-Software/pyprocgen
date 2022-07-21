"""
test_tarot.py
=============

Unit tests for tarot.py. Requires corpora JSON data.

"""

import unittest
import tarot

class Test100GetDataFromCardname(unittest.TestCase):
    def setUp(self):
        self.the_data = tarot.get_data_from_cardname("The Fool")

    def test_data_is_dict(self):
        self.assertIsInstance(self.the_data, dict)


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
