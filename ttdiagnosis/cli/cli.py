import argparse


class TTDiagnosisCLI:
    CLI_VERSION = 'TTDiagnosis 1.0.0'

    def __init__(self):
        self.__run()

    def __run(self):
        self.parser = argparse.ArgumentParser(
            prog='ttdiagnosis',
            description='Tweet extraction bot using data mining to analyze sentiments with machine learning (NLP) \
            and send audio-transformed diagnostics to telegram using AWS Polly',
            epilog='By Joao Eliandro',
            usage='%(prog)s [options]',
        )

        self.parser.version = self.CLI_VERSION
        self.parser.add_argument('-v', '--version', action='version')

        self.parser.parse_args()
