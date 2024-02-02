#!/usr/bin/python3
""" Validation of utf-8 encoding in data sets """


def validUTF8(data):
    """
    Determines if a given dataset represents a valid UTF-8 encoding

    Args:
        data (list): List of integers representing the dataset

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False
    """
    trailing_bytes = 0

    for num in data:
        # Check if the current byte is a leading byte(starts with 0)
        if trailing_bytes == 0:
            if (num >> 7) == 0b0:
                continue            # Valid leading byte

            leading_ones = 0
            mask = 0b10000000
            while (num & mask) == mask:
                leading_ones += 1
                mask >>= 1

            if leading_ones == 1 or leading_ones > 4:
                return False

            trailing_bytes = leading_ones - 1

        else:
            # Check if current byte is a trailing byte (starts with 10)
            if (num >> 6) == 0b10:
                trailing_bytes -= 1
            else:
                return False

    # Check if all trailing_bytes are accounted for
    return trailing_bytes == 0
