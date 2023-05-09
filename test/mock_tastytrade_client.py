class MockTastyTradeClient():
    def set_get_equity_option_chains_response(self, get_equity_option_chain_response):
        self.get_equity_option_chains_response = get_equity_option_chain_response

    def set_get_futures_option_chains_response(self, get_futures_option_chains_response):
        self.get_futures_option_chains_response = get_futures_option_chains_response

    def get_equity_option_chains(self, symbol):
        return self.get_equity_option_chains_response
    
    def get_futures_option_chains(self, symbol):
        return self.get_futures_option_chains_response