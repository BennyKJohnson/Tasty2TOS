from src.tos_trade_formatter import convert_option_to_tos, convert_futures_option_to_tos
import unittest
from src.option_symbol_parser import parse_futures_option_symbol

class TestTosTradeWriter(unittest.TestCase):
    def test_convert_tos_buy_weekly_pm_put_option(self):
        option = {
            'underlying_symbol': 'WMT',
            'expiration_date_month': '05',
            'expiration_date_day': '12',
            'expiration_date_year': '23',
            'is_call': False,
            'strike_price': 148.0,
        }

        option_series = {
            'is_weekly': True,
        }
        expected = 'SELL -1 WMT 100 (Weeklys) 12 MAY 23 148 PUT @.72 LMT FIXED'
        actual = convert_option_to_tos(option, option_series, -1, 0.72)
        self.assertEqual(actual, expected)

    def test_convert_futures_call_option(self):
        option_details = parse_futures_option_symbol('./MESM3MESM3 230616C4425')
        option_series = {
            'is_weekly': True,
            'settlement_type': 'PM',
            'expiration-date': '2023-06-16',
        }

        actual = convert_futures_option_to_tos(option_details, option_series, -2, 14.12)
        expected = 'SELL -2 /MESM23:XCME 1/5 JUN 23 /MESM23:XCME 4425 CALL @14.12 LMT FIXED'
        self.assertEqual(actual, expected)

    def test_convert_futures_call_alt_option(self):
        option_details = parse_futures_option_symbol('./MESU3EXM3  230630C4570')
        option_series = {
            'is_weekly': True,
            'settlement_type': 'PM',
            'expiration-date': '2023-06-16',
        }

        actual = convert_futures_option_to_tos(option_details, option_series, -1, 7.75)
        expected = 'SELL -1 /MESU23:XCME 1/5 JUN 23 (Wk3) /EX3M23:XCME 4570 CALL @7.75 LMT FIXED'
        self.assertEqual(actual, expected)

    def test_convert_futures_call_alt2_option(self):
        option_details = parse_futures_option_symbol('./MESU3EX3N3 230721C4650')
        option_series = {
            'is_weekly': True,
            'settlement_type': 'PM',
            'expiration-date': '2023-07-21',
        }

        actual = convert_futures_option_to_tos(option_details, option_series, -1, 9.75)
        expected = 'SELL -1 /MESU23:XCME 1/5 JUL 23 (Wk3) /EX3N23:XCME 4650 CALL @9.75 LMT FIXED'
        self.assertEqual(actual, expected)

    def test_convert_futures_put_option(self):
        option_details = parse_futures_option_symbol('./MESM3EX4K3 230526P3930')
        option_series = {
            'is_weekly': True,
            'settlement_type': 'PM',
            'expiration-date': '2023-06-16',
        }

        actual = convert_futures_option_to_tos(option_details, option_series, -1, 21.25)
        expected = 'SELL -1 /MESM23:XCME 1/5 MAY 23 (Wk3) /EX4K23:XCME 3930 PUT @21.25 LMT FIXED'
        self.assertEqual(actual, expected)

