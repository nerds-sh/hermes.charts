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

        parser.add_argument('-s', '--set',
                            action='append',
                            default=[],
                            help='Extra value overwrites. Ex. `--set image.name=... --set image.tag=latest`.')

        return parser.parse_args()

ARGS = Arguments.parse()

system(f'helm install {ARGS.chart} charts/{ARGS.chart} '
       f'--namespace hermes-{ARGS.environment} '
       f'--create-namespace '
       f'{" ".join(map(lambda file: f"--values {file} ", glob(f"values/{ARGS.environment}/{ARGS.chart}/*.yaml")))} '
       f'{" ".join(map(lambda overwrite: f"--set {overwrite} ", ARGS.set))}')
