import unittest
from src.tasty_trade_option_chain_data_source import TastyTradeOptionChainsDataSource
from src.option_symbol_parser import parse_futures_option_symbol
from test.mocks.tastytrade_api_mock_responses import get_wmt_equity_option_chain_response_body, get_mes_futures_option_chain_response_body
from .mock_tastytrade_client import MockTastyTradeClient
from .mocks.mock_logger import MockLogger

class TestTastyTradeOptionChainsDataSource(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tasty_trade_client = MockTastyTradeClient()

    def test_get_equity_option_chain(self):
        TestTastyTradeOptionChainsDataSource.tasty_trade_client.set_get_equity_option_chains_response(get_wmt_equity_option_chain_response_body())
        option_chains_data_source = TastyTradeOptionChainsDataSource(TestTastyTradeOptionChainsDataSource.tasty_trade_client, MockLogger())
        result = option_chains_data_source.get_equity_option_series({
            'underlying_symbol': 'WMT',
            'expiration_date_month': '06',
            'expiration_date_day': '16',
            'expiration_date_year': '23',
        })

        self.assertIsNotNone(result)

    def test_get_futures_option_series(self):
        TestTastyTradeOptionChainsDataSource.tasty_trade_client.set_get_futures_option_chains_response(get_mes_futures_option_chain_response_body())

        option_details = parse_futures_option_symbol('./MESM3EX4K3 230526P3930')
        option_chains_data_source = TastyTradeOptionChainsDataSource(TestTastyTradeOptionChainsDataSource.tasty_trade_client, MockLogger())
        result = option_chains_data_source.get_futures_option_series(option_details)

        self.assertEqual(result['is_weekly'], True)
        self.assertEqual(result['settlement_type'], 'PM')
        self.assertEqual(result['expiration-date'], '2023-05-26')

if __name__ == '__main__':
    unittest.main()
