#

import unittest
from src.homework.i_dictionaries_sets.dictionary import get_p_distance
from src.homework.i_dictionaries_sets.dictionary import get_p_distance_matrix


class TestPDistanceFunctions(unittest.TestCase):

    def test_p_distance (self):
        list1 = ['T','T','T','C','C','A','T','T','T','A']
        list2 = ['G','A','T','T','C','A','T','T','T','C']
        excepted = 0.4
        result = get_p_distance (list1, list2)
        self.assertAlmostEqual (result, excepted, delta=0.001, msg= "Expected {expected}, but got {result}")


    def test_get_p_distance_matrix (self):
        dna_lists = [
             ['T','T','T','C','C','A','T','T','T','A'],
             ['G','A','T','T','C','A','T','T','T','C'],
             ['T','T','T','C','C','A','T','T','T','T'],
             ['G','T','T','C','C','A','T','T','T','A']
         ]
        expected_matrix = [
             [0.0, 0.4, 0.1, 0.1],
             [0.4, 0.0, 0.4, 0.3],
             [0.1, 0.4, 0.0, 0.2],
             [0.1, 0.3, 0.2, 0.0]
         ]
        result_matrix = get_p_distance_matrix (dna_lists)
        for i in range (len (result_matrix)):
            for j in range (len (result_matrix [i])):
                self.assertAlmostEqual(result_matrix[i][j], expected_matrix [i][j], delta=0.001, msg="expected {expected_matrix[i][j]} at ({i}, {j}), but got {result_matrix[i][j]}")


if __name__ == "__main__":
    unittest.main()