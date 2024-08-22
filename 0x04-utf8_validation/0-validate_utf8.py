#!/usr/bin/python3
"""utf-8 validation module"""


def validUTF8(data):
    """
    a method that determines if a given data set,
    represents a valid UTF-8 encoding
    Args:
        data (list): A list of integers,
        where each integer represents 1 byte of data
    Return:
        True if data is a valid UTF-8 encoding, else return False
    """
    number_bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for byt in data:
    # get the binary representation, only need the least significant 8 bits

        mask_byte = 1 << 7

        if number_bytes == 0:

            while mask_byte & byt:
                number_bytes += 1
                mask_byte = mask_byte >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                        return False

        else:
            if not (byt & mask_1 and not (byt & mask_2)):
                return False

        # reduce the number of bytes to process by 1 after each integer
        number_bytes -= 1

    if number_bytes == 0:
        return True

    return False
