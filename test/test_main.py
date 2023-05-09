import unittest
import json 
from src.option_symbol_parser import parse_option_symbol, parse_futures_option_symbol
from src.main import parse_tastytrade_positions_csv
from .mocks.mock_logger import MockLogger

class TestMain(unittest.TestCase):
    def test_parse_tastytrade_positions(self):
        data = parse_tastytrade_positions_csv('test/resources/tasty.csv', MockLogger())
        self.assertEqual(data[0]['Account'], '6AB09999')
        self.assertEqual(data[0]['Symbol'], './MESM3MESM3 230616C4425')