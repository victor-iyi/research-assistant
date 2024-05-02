import argparse
import logging
from rich.logging import RichHandler


def _start(args: argparse.Namespace) -> None:
    logging.info(args)


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-p', '--path', type=str, default=None,
        help='Path to a local file.'
    )
    parser.add_argument(
        '-u', '--url', type=str, default=None,
        help='URL to a remote file.'
    )

    # Parse the command line arguments.
    args: argparse.Namespace = parser.parse_args()

    # Set the logging level.
    logging.basicConfig(
        level=logging.INFO,
        format='%(message)s',
        # datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            RichHandler(),
        ],
    )

    _start(args)


if __name__ == '__main__':
    main()
