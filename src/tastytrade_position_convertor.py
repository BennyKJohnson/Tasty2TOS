from .tasty_trade_option_chain_data_source import TastyTradeOptionChainsDataSource
from .tos_trade_formatter import convert_option_to_tos, convert_futures_option_to_tos
from .option_symbol_parser import parse_option_symbol, parse_futures_option_symbol
from .logger import Logger

class TastyTradePositionConvertor:
    def __init__(self, options_chains_data_source: TastyTradeOptionChainsDataSource, logger: Logger):
        self.option_chains_data_source = options_chains_data_source
        self.logger = logger

    def is_supported_position(self, trade):
        return trade['Type'] == 'FUTURES_OPTION' or trade['Type'] == 'OPTION'

    def convert_option_position_to_tos(self, position):
        try:
            option = parse_option_symbol(position['Symbol'])
            option_series = self.option_chains_data_source.get_equity_option_series(option)
            if option_series is None:
                self.logger.log_verbose('Failed to retrieve option series information for option ' + position['Symbol'])
                return None
            
            return convert_option_to_tos(option, option_series, int(position['Quantity']), abs(float(position['Trade Price'])))
        except Exception as e:
            self.logger.log_verbose(e)
            self.logger.log_verbose('Error converting option: ' + position['Symbol'])

    def convert_futures_option_position_to_tos(self, position):
        try:
            option = parse_futures_option_symbol(position['Symbol'])
            option_series = self.option_chains_data_source.get_futures_option_series(option)
            if option_series is None:
                self.logger.log_verbose('Failed to retrieve option series information for futures option ' + position['Symbol'])
                return None
            
            return convert_futures_option_to_tos(option, option_series, int(position['Quantity']), abs(float(position['Trade Price'])))
        except Exception as e:
            self.logger.log_verbose('Error converting futures option: ' + position['Symbol'])
            self.logger.log_verbose(e)

    def convert_position(self, position):
        if not self.is_supported_position(position):
            self.logger.log_verbose('Skipping unsupported position: ' + position['Symbol'])
            return None
        if position['Type'] == 'OPTION':
            tos_trade = self.convert_option_position_to_tos(position)
        if position['Type'] == 'FUTURES_OPTION':
            tos_trade = self.convert_futures_option_position_to_tos(position)
        
        return tos_trade

    def convert_positions(self, positions):
        tos_trades = []
        for position in positions:
            tos_trade = self.convert_position(position)
            if tos_trade is not None:
                    tos_trades.append(tos_trade)

        return tos_trades