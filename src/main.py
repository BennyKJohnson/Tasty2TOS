from csv import DictReader
from .tastytrade_position_convertor import TastyTradePositionConvertor
from .tasty_trade_option_chain_data_source import TastyTradeOptionChainsDataSource
from .command_line import CommandLine
from .parameters import Parameters
from .config import Config
from .tasty_trade_client import TastyTradeClient
from .logger import Logger

def parse_tastytrade_positions_csv(filename, logger):
    logger.log_verbose('Parsing tastytrade positions from ' + filename)
    data = []
    with open(filename) as csv_file:
        reader = DictReader(csv_file)

        for row in reader:
            data.append(row)

        return data

def run(parameters, cli):
    logger = Logger(cli, is_verbose=parameters.verbose)
    positions = parse_tastytrade_positions_csv(parameters.positions_csv_filepath, logger=logger)
    logger.log_verbose('Found {} positions'.format(len(positions)))

    tastytrade_client = TastyTradeClient(parameters.tasty_trade_username, parameters.tasty_trade_password)
    tastytrade_option_chains_data_source = TastyTradeOptionChainsDataSource(tastytrade_client, logger)
    tos_trades = TastyTradePositionConvertor(tastytrade_option_chains_data_source, logger).convert_positions(positions)

    for tos_trade in tos_trades:
        cli.write_line(tos_trade)

def main():
    cli = CommandLine()
    config = Config()

    run(get_parameters(config, cli.get_arguments()), cli)

def get_parameters(config, arguments):
    return Parameters(
        positions_csv_filepath=arguments['positions_csv_filepath'],
        verbose=arguments['verbose'],
        tasty_trade_username=arguments.get('username') or config.get('TASTY_TRADE_USERNAME'),
        tasty_trade_password=arguments.get('password') or config.get('TASTY_TRADE_PASSWORD')
    )
