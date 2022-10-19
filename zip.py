import argparse
import subprocess

DEFAULT_SOURCE = '/var/log'


def main(source, decompress):
    subprocess.run(f'gzip -r {source} {"-d" * decompress}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', type=str, default=DEFAULT_SOURCE)
    parser.add_argument('-d', '--decompress', action='store_true', default=False)
    args = parser.parse_args()

    main(args.source, args.decompress)
