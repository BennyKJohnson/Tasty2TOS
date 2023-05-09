import unittest
import threading
from test.mocks.fake_tastytrade_api_server import FakeTastyTradeApiServer
from src.tasty_trade_client import TastyTradeClient
from test.mocks.tastytrade_api_mock_responses import get_wmt_equity_option_chain_response_body, get_es_futures_option_chain_response_body

class TestTastyTradeClient(unittest.IsolatedAsyncioTestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

        self.tasty_trade = TastyTradeClient(
            username='fakeuser',
            password='password',
            url='http://localhost:5000'
        )

    @classmethod
    def setUpClass(cls):
        cls.fake_tasty_trade_api = FakeTastyTradeApiServer()
        cls.server_thread = threading.Thread(target=cls.fake_tasty_trade_api.start)
        cls.server_thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.fake_tasty_trade_api.stop()
        cls.server_thread.join()

    def test_create_session_makes_correct_http_request(self):
        tasty_trade_client = TastyTradeClient(
            'fakeuser',
            'password',
            'http://localhost:5000')
        session_token = tasty_trade_client.create_session()

        self.assertIsNotNone(session_token)
        self.assertEqual(session_token, 'SESSION_TOKEN')

        request = TestTastyTradeClient.fake_tasty_trade_api.last_request
        self.assertEqual(request['body']['login'], 'fakeuser')
        self.assertEqual(request['body']['password'], 'password')
        self.assertEqual(request['path'], '/sessions')

    def test_get_equity_options_chain_makes_correct_http_request(self):
        self.tasty_trade.get_equity_option_chains('WMT')

        request = TestTastyTradeClient.fake_tasty_trade_api.last_request
        self.assertEqual(request['method'], 'GET')
        self.assertEqual(request['path'], '/option-chains/WMT/nested')
        self.assertEqual(request['headers']['Authorization'], 'SESSION_TOKEN')

    def test_get_equity_options_chain_returns_correct_response(self):
        response = self.tasty_trade.get_equity_option_chains('WMT')
        self.assertEqual(response, get_wmt_equity_option_chain_response_body())

    def test_get_futures_option_chains(self):
        response = self.tasty_trade.get_futures_option_chains('ES')
        self.assertEqual(response, get_es_futures_option_chain_response_body())

        request = TestTastyTradeClient.fake_tasty_trade_api.last_request
        self.assertEqual(request['method'], 'GET')
        self.assertEqual(request['path'], '/futures-option-chains/ES/nested')
        self.assertEqual(request['headers']['Authorization'], 'SESSION_TOKEN')

if __name__ == '__main__':
    unittest.main()
