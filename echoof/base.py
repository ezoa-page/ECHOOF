"""
This software is proprietary and may not be used, copied, modified, or distributed without the express permission of the copyright holder.
"""

from echoof.logger import logger

def base10_to_base95(base10num):
    logger.debug(f"Converting base-10 number {base10num} to base-95.")

    if base10num == 0:
        logger.debug("Base-10 number is 0, returning space (' ').")
        return chr(32)  # Return a space if the number is 0, as 0 % 95 + 32 = 32

    if base10num < 0:
        logger.error("Negative numbers cannot be converted.")
        raise Exception("Negative numbers cannot be converted.")

    base95num = ""

    while base10num > 0:
        remainder = base10num % 95
        ascii_char = chr(remainder + 32)
        base95num = ascii_char + base95num
        base10num //= 95
        logger.debug(f"Intermediate base-95 string: {base95num}")

    logger.debug(f"Final base-95 string: {base95num}")
    return base95num

def base95_to_base10(base95num):
    logger.debug(f"Converting base-95 string '{base95num}' to base-10.")
    base10num = 0

    for power, char in enumerate(reversed(base95num)):
        value = ord(char) - 32
        base10num += value * (95 ** power)
        logger.debug(f"Character: {char}, Value: {value}, Power: {power}, Intermediate base-10 number: {base10num}")

    logger.debug(f"Final base-10 number: {base10num}")
    return base10num

def base10_to_base220(base10num):
    logger.debug(f"Converting base-10 number {base10num} to base-220.")

    if base10num == 0:
        logger.debug("Base-10 number is 0, returning '#' character.")
        return chr(35)  # Return '#' if the number is 0, as 0 % 220 + 35 = 35

    base220num = ""

    while base10num > 0:
        remainder = base10num % 220
        ascii_char = chr(remainder + 35)
        base220num = base220num + ascii_char
        base10num //= 220
        logger.debug(f"Intermediate base-220 string: {base220num}")

    logger.debug(f"Final base-220 string: {base220num}")
    return base220num

def base220_to_base10(base220num):
    logger.debug(f"Converting base-220 string '{base220num}' to base-10.")
    base10num = 0
    power = 0

    for char in base220num:
        value = ord(char) - 35
        base10num += value * (220 ** power)
        logger.debug(f"Character: {char}, Value: {value}, Power: {power}, Intermediate base-10 number: {base10num}")
        power += 1

    logger.debug(f"Final base-10 number: {base10num}")
    return base10num
