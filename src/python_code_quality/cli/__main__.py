#!/usr/bin/env python
"""python_code_quality command line interface."""

import argparse
import logging
from pathlib import Path

from python_code_quality.api import run
from python_code_quality.utils.logging import configure_logging

logger = logging.getLogger(__name__)


def _argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python-code-quality",
        usage="%(prog)s config_file [options [args]]",
        epilog="_________________python-code-quality___________________",
        prefix_chars="-",
        add_help=True,
        description=("python-code-quality config_file --option"),
    )

    _ = parser.add_argument(
        "config_file",
        metavar="config_file",
        type=str,
        help="name of the file containing the python-code-quality configuration.",
    )

    _ = parser.add_argument(
        "--option",
        action="store_true",
        help="example option.",
        default=False,
        required=False,
    )

    console_verbosity = parser.add_mutually_exclusive_group(required=False)

    _ = console_verbosity.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help=("console output will be quiet."),
        default=False,
    )

    _ = console_verbosity.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help=("console output will be verbose."),
        default=False,
    )

    _ = parser.add_argument(
        "--log",
        action="store",
        type=str,
        help="name of log file. If specified, this will activate logging to file.",
        default=None,
        required=False,
    )

    _ = parser.add_argument(
        "--log-level",
        action="store",
        type=str,
        help="log level applied to logging to file.",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="WARNING",
        required=False,
    )

    return parser


def main() -> None:
    """Entry point for console script as configured in pyproject.toml.

    Runs the command line interface and parses arguments and options entered on the console.
    """
    parser = _argparser()
    args = parser.parse_args()

    # Configure Logging
    # ..to console
    log_level_console: str = "WARNING"
    if any([args.quiet, args.verbose]):
        log_level_console = "ERROR" if args.quiet else log_level_console
        log_level_console = "INFO" if args.verbose else log_level_console
    # ..to file
    log_file: Path | None = Path(args.log) if args.log else None
    log_level_file: str = args.log_level
    configure_logging(log_level_console, log_file, log_level_file)

    config_file: Path = Path(args.config_file)
    option: bool = args.option

    # Check whether python-code-quality config file exists
    if not config_file.is_file():
        logger.error(f"python-code-quality.py: File {config_file} not found.")
        return

    logger.info(
        f"Start python-code-quality.py with following arguments:\n\t config_file: \t{config_file}\n\t option: \t\t\t{option}\n"  # noqa: E501
    )

    # Invoke API
    run(
        config_file=config_file,
        option=option,
    )


if __name__ == "__main__":
    main()
