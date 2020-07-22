import unittest

from json_structure.main import structure


class TestStructureFunction(unittest.TestCase):

    def test_simple_structure(self):
        d = {'age': 15, 'name': 'John'}
        self.assertEqual(structure(d), {'age': int, 'name': str})

    def test_complex_structure(self):
        d = {'age': 15, 'name': 'John', 'friends': [{'age': 20, 'name': 'Jacob'}]}
        self.assertEqual(structure(d), {'age': int, 'name': str, 'friends': [{'age': int, 'name': str}, ]})

    def test_complex_structure_with_several_values_for_same_list(self):
        d = {'age': 15, 'name': 'John', 'friends': [{'age': 20, 'name': 'Jacob'}, {'age': 30,
                                                                                   'first_name': 'J',
                                                                                   'last_name': 'W'}]}
        self.assertEqual(structure(d), {'age': int, 'name': str, 'friends': [{'age': int, 'name': str},
                                                                             {'age': int, 'first_name': str,
                                                                              'last_name': str}]})


if __name__ == '__main__':
    unittest.main()
