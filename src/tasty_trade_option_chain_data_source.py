from .tasty_trade_client import TastyTradeClient
from .logger import Logger

def get_expiration_date_str(option_details):
    return f'20{option_details["expiration_date_year"]}-{option_details["expiration_date_month"]}-{option_details["expiration_date_day"]}'

class TastyTradeOptionChainsDataSource:
    def __init__(self, tasty_trade_client: TastyTradeClient, logger: Logger):
        self.tt_client = tasty_trade_client
        self.logger = logger
        self.option_chains_by_underlying = {}

    def find_option_series(self, option_series, expiration_date):
        for series in option_series:
            if series['expiration-date'] == expiration_date:
                return series

        return None
    
    def find_futures_options_series(self, options_series, option_details):
        expiration_date = get_expiration_date_str(option_details)
        for series in options_series:
            if series['expiration-date'] == expiration_date and series['option-contract-symbol'] == option_details['option_contract_symbol']:
                return series
        return None

    def get_equity_option_series(self, option_details):
        underlying = option_details['underlying_symbol']
        expiration_date_str = get_expiration_date_str(option_details)

        option_chains = None
        if not underlying in self.option_chains_by_underlying:
            self.logger.log_verbose('Retrieving option chains for ' + underlying + '...')
            option_chains = self.tt_client.get_equity_option_chains(underlying)
            self.option_chains_by_underlying[underlying] = option_chains
        else:
            option_chains = self.option_chains_by_underlying[underlying]
        expirations = []
        for item in option_chains['data']['items']:
            expirations += item['expirations']
        option_series = self.find_option_series(expirations, expiration_date_str)
        if option_series is None:
            return None
         
        return {
            'is_weekly': option_series['expiration-type'] == 'Weekly',
            'settlement_type': option_series['settlement-type'],
            'expiration-date': option_series['expiration-date'],
        }
    
    def get_futures_option_series(self, option_details):
        option_chains = self.tt_client.get_futures_option_chains(option_details['futures_root_symbol'])
        expirations = []
        for item in option_chains['data']['option-chains']:
            expirations += item['expirations']

        self.logger.log_verbose('Retrieving option chains for ' + option_details['futures_root_symbol'] + '...')
        option_series = self.find_futures_options_series(expirations, option_details)

        return {
            'is_weekly': option_series['expiration-type'] == 'Weekly',
            'settlement_type': option_series['settlement-type'],
            'expiration-date': option_series['expiration-date'],
        }