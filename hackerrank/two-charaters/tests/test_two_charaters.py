from algo.two_charaters import alternate

import unittest

class TestAlternate(unittest.TestCase):
    def test_give_beabeefeab_to_alternate(self):
        x = 'beabeefeab'
        result = alternate(x)
        self.assertEqual(result,5)

    def test_give_asdcbsdcagfsdbgdfanfghbsfdab_to_alternate(self):
        x = "asdcbsdcagfsdbgdfanfghbsfdab"
        result = alternate(x)
        self.assertEqual(result,8)

    def test_give_cwomzxmuelmangtosqkgfdqvkzdnxerhravxndvomhbokqmvsfcaddgxgwtpgpqrmeoxvkkjunkbjeyteccpugbkvhljxsshpoymkryydtmfhaogepvbwmypeiqumcibjskmsrpllgbvc_to_alternate(self):
        x = "cwomzxmuelmangtosqkgfdqvkzdnxerhravxndvomhbokqmvsfcaddgxgwtpgpqrmeoxvkkjunkbjeyteccpugbkvhljxsshpoymkryydtmfhaogepvbwmypeiqumcibjskmsrpllgbvc"
        result = alternate(x)
        self.assertEqual(result,8)

    def test_give_ab_to_alternate(self):
        x = 'ab'
        result = alternate(x)
        self.assertEqual(result,2)

    def test_give_a_to_alternate(self):
        x = 'a'
        result = alternate(x)
        self.assertEqual(result,0)
        
