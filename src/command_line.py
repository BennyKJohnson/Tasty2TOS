import argparse

class CommandLine:
    def create_parser(self):
        parser = argparse.ArgumentParser(description='Convert tastytrade positions to Thinkorswim (TOS) trades')
        parser.add_argument('positions_csv_filepath', metavar='positions-filepath', type=str, help='The path to the tastytrade positions CSV file')
        parser.add_argument('--verbose', dest='verbose', action='store_true', help='Enable verbose logging')
        parser.add_argument('--username', dest='username', type=str, help='Username of the TastyTrade account to make API calls on')
        parser.add_argument('--password', dest='password', type=str, help='Username of the TastyTrade account to make API calls on')

        parser.set_defaults(verbose=False)

        return parser

    def get_arguments(self):
        args = self.create_parser().parse_args()

        return {
            'positions_csv_filepath': args.positions_csv_filepath,
            'verbose': args.verbose,
            'username': args.username,
            'password': args.password
        }
    
    def write_line(self, output):
        print(output)
