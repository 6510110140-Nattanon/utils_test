from algo.grid_challenges import gridChallenge 

import unittest

class TestGridChallenge(unittest.TestCase):
    def test_case_1_in_grudchallenge(self):
        lst = ['eabcd', 'fghij', 'olkmn', 'trpqs' ,'xywuv']
        result = gridChallenge(lst)
        self.assertEqual(result,"YES")
    def test_case_2_in_grudchallenge(self):
        lst = ['kc', 'iu']
        result = gridChallenge(lst)
        self.assertEqual(result,"YES")
    def test_case_3_in_grudchallenge(self):
        lst = ['uxf', 'vof', 'hmp']
        result = gridChallenge(lst)
        self.assertEqual(result,"NO")
    def test_case_4_in_grudchallenge(self):
        lst = ['abc', 'hjk', 'mpq', 'rtv']
        result = gridChallenge(lst)
        self.assertEqual(result,"YES")
    def test_case_5_in_grudchallenge(self):
        lst = ['mpxz', 'abcd', 'wlmf']
        result = gridChallenge(lst)
        self.assertEqual(result,"NO")