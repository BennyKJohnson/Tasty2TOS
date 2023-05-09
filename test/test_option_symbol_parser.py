import unittest
import json 
from src.option_symbol_parser import parse_option_symbol, parse_futures_option_symbol

class TestMain(unittest.TestCase):
    def test_parse_option_symbol(self):
        symbol = 'XLF   230616C00034000'
        data = parse_option_symbol(symbol)
        self.assertEqual(data['underlying_symbol'], 'XLF')
        self.assertEqual(data['expiration_date'], '230616')
        self.assertEqual(data['expiration_date_year'], '23')
        self.assertEqual(data['expiration_date_month'], '06')
        self.assertEqual(data['expiration_date_day'], '16')

        self.assertEqual(data['option_type'], 'C')
        self.assertEqual(data['strike_price_padded'], '00034000')
        self.assertEqual(data['strike_price'], 34.0)

    def test_parse_futures_option_symbol(self):
        symbol = './MESM3EX4K3 230526P3930'
        data = parse_futures_option_symbol(symbol)

        self.assertEqual(data['root_symbol'], 'EX4')
        self.assertEqual(data['futures_root_symbol'], 'MES')
        self.assertEqual(data['expiration_date'], '230526')
        self.assertEqual(data['expiration_date_year'], '23')
        self.assertEqual(data['expiration_date_month'], '05')
        self.assertEqual(data['expiration_date_day'], '26')
        self.assertEqual(data['is_call'], False)
        self.assertEqual(data['is_put'], True)
        self.assertEqual(data['strike_price'], 3930)
        self.assertEqual(data['product_code'], 'M3')
        self.assertEqual(data['option_contract_symbol'], 'EX4K3')
        self.assertEqual(data['underlying_symbol'], 'MESM3')


