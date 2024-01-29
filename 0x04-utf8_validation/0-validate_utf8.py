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
            elif (num >> 5) == 0b110:
                trailing_bytes = 1  # 1 trailing byte for 2-byte char
            elif (num >> 4) == 0b1110:
                trailing_bytes = 2  # 2 trailing bytes for 3-byte char
            elif (num >> 3) == 0b11110:
                trailing_bytes = 3  # 3 trailing bytes for 4-byte char
            else:
                return False
        else:
            # check if current byte is a trailing byte (starts with 10)
            if (num >> 6) == 0b10:
                trailing_bytes -= 1  # Valid byte, reduce the count
            else:
                return False

    # Check if all trailing_bytes are accounted for
    return trailing_bytes == 0
