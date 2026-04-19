import unittest
from conversor import converter

class TestConversor(unittest.TestCase):

    def test_usd_para_brl(self):
        self.assertEqual(converter(1, "USD", "BRL"), 5.0)

    def test_brl_para_usd(self):
        self.assertEqual(converter(5, "BRL", "USD"), 1.0)

    def test_moeda_invalida(self):
        with self.assertRaises(ValueError):
            converter(10, "ABC", "USD")

if __name__ == "__main__":
    unittest.main()