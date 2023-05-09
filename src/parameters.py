from dataclasses import dataclass

@dataclass
class Parameters:
    positions_csv_filepath: str
    tasty_trade_username: str
    tasty_trade_password: str
    verbose: bool