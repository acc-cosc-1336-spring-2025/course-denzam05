#
import unittest
from src.homework.h_strings.strings import get_hamming_distance
from src.homework.h_strings.strings import get_dna_complement

class Test_config (unittest.TestCase):

    def test_get_hamming_distance(self):

        s1= "GAGCCTACTAACGGGAT"
        s2= "CATCGTAATGACGGCCT"
        expected_distance = 7
        actual_distance= get_hamming_distance (s1, s2)
        self.assertEqual(actual_distance, expected_distance)

    def test_get_dna_complement(self):
        dna=  "AAAACCCGGT"
        expected_complement= "TTTTGGGCCA"
        actual_complement= get_dna_complement (dna)
        self.assertEqual (actual_complement, expected_complement)
    