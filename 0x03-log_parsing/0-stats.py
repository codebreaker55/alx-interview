#!/usr/bin/python3
"""a module for reading stdin line by line and computes metrics"""


import sys


def stdin_print(stats: dict, f_size: int):
    """
    Print the status information
    Args:
        stat_counts (dict):
        A dictionary containing the count of each status code
        f_size (int): The total size of the file
    """
    print("File size: {:d}".format(f_size))
    for k in sorted(stats.keys()):
        if stats[k]:
            print("{}: {:d}".format(k, stats[k]))


f_size, count = 0, 0

stat_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
              "403": 0, "404": 0, "405": 0, "500": 0}

try:
    # Process input from stdin
    for st_line in sys.stdin:
        if count % 10 == 0 and count != 0:
            stdin_print(stat_codes, f_size)

            # Split the input line and update the count and file size
            st_list = st_line.split()
            count = count + 1

        try:
            f_size += int(st_list[-1])
        except Exception:
            pass

        try:
            if st_list[-2] in stat_codes:
                stat_codes[st_list[-2]] += 1
        except Exception:
            pass
    stdin_print(stats_codes, f_size)


except KeyboardInterrupt:
    stdin_print(stat_codes, f_size)
    raise
