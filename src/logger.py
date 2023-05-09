class Logger:
    def __init__(self, cli, is_verbose = True):
        self.cli = cli
        self.is_verbose = is_verbose

    def log_verbose(self, message):
        if self.is_verbose:
            self.cli.write_line(message)