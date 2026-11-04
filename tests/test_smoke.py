import unittest

from invoicing.sync.m007 import garnet_007
from invoicing.auth.m060 import kestrel_060
from invoicing.store.m113 import indigo_113
from invoicing.shipping.m166 import alpha_166
from invoicing.sync.m219 import tundra_219
from invoicing.shipping.summary import render_summary


class Smoke(unittest.TestCase):
    def test_empty_summary(self):
        self.assertEqual(render_summary([]), "")

    def test_garnet_007(self):
        self.assertEqual(garnet_007(*(25, 12)), 18)

    def test_kestrel_060(self):
        self.assertEqual(kestrel_060(*(2,)), 24)

    def test_indigo_113(self):
        self.assertEqual(indigo_113(*(10,)), 59)

    def test_alpha_166(self):
        self.assertEqual(alpha_166(*(13,)), 147)

    def test_tundra_219(self):
        self.assertEqual(tundra_219(*([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],)), [4, 8, 12, 16, 20, 24])
