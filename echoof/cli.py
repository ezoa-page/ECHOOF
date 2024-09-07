"""
This software is proprietary and may not be used, copied, modified, or distributed without the express permission of the copyright holder.
"""

import argparse
import logging
from echoof.base import base10_to_base95, base95_to_base10, base10_to_base220, base220_to_base10
from echoof.logger import logger

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Ezoa's Converter for Hexadecimal Operations Over Furcadia.")

    # Add --verbose flag
    parser.add_argument('--verbose', action='store_true', help='Enable verbose debug logging')

    # Set up subparsers for commands
    subparsers = parser.add_subparsers(dest='command')

    parser_base10_to_base95 = subparsers.add_parser('base10_to_base95', help='Convert base-10 number to base-95 string')
    parser_base10_to_base95.add_argument('number', type=int, help='Base-10 number to convert')

    parser_base95_to_base10 = subparsers.add_parser('base95_to_base10', help='Convert base-95 string to base-10 number')
    parser_base95_to_base10.add_argument('string', type=str, help='Base-95 string to convert')

    parser_base10_to_base220 = subparsers.add_parser('base10_to_base220', help='Convert base-10 number to base-220 string')
    parser_base10_to_base220.add_argument('number', type=int, help='Base-10 number to convert')

    parser_base220_to_base10 = subparsers.add_parser('base220_to_base10', help='Convert base-220 string to base-10 number')
    parser_base220_to_base10.add_argument('string', type=str, help='Base-220 string to convert')

    args = parser.parse_args()

    # If no command is provided, print the help message
    if args.command is None:
        parser.print_help()
        return

    # Set logging level to DEBUG if --verbose flag is set
    if args.verbose:
        logger.setLevel(logging.DEBUG)
        logger.debug("Verbose mode enabled.")
    else:
        logger.setLevel(logging.WARNING)

    logger.debug(f"Parsed arguments: {args}")

    # Command processing
    if args.command == 'base10_to_base95':
        result = base10_to_base95(args.number)
        logger.debug(f"Result: {result}")
        print(f"Base-10 to Base-95: {result}")

    elif args.command == 'base95_to_base10':
        result = base95_to_base10(args.string)
        logger.debug(f"Result: {result}")
        print(f"Base-95 to Base-10: {result}")

    elif args.command == 'base10_to_base220':
        result = base10_to_base220(args.number)
        logger.debug(f"Result: {result}")
        print(f"Base-10 to Base-220: {result}")

    elif args.command == 'base220_to_base10':
        result = base220_to_base10(args.string)
        logger.debug(f"Result: {result}")
        print(f"Base-220 to Base-10: {result}")

if __name__ == "__main__":
    main()
