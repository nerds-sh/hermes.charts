from argparse import ArgumentParser
from os import system
from glob import glob

class Arguments:
    @staticmethod
    def parse():
        parser = ArgumentParser()

        parser.add_argument('-c', '--chart',
                            required=True,
                            choices=['api', 'web', 'cam', 'mysql'],
                            help='The name of the chart you want to upgrade.')

        parser.add_argument('-e', '--environment',
                            required=True,
                            choices=['local', 'dev', 'staging', 'shared'],
                            help='The environment you want to install.')

        return parser.parse_args()

ARGS = Arguments.parse()

system(f'helm uninstall {ARGS.chart} --namespace hermes-{ARGS.environment}')
