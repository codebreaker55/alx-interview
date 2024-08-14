#!/usr/bin/python3
"""a module for reading stdin line by line and computes metrics"""


import sys


if __name__ == '__main__':
    f_size, count = 0, 0
    stat_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    # Create a dictionary to store the count of each status code
    stats = {s: 0 for s in stat_codes}


def stdin_print(stats, f_size):
    """
    Print the status information
    Args:
        stat_counts (dict):
        A dictionary containing the count of each status code
        f_size (int): The total size of the file
    """
    print("File size: {:d}".format(f_size))
    for stat_codes, count in sorted(stats.items()):
        if count != 0:
            print("{}: {:d}".format(stat_codes, count))


try:
    # Process input from stdin
    for line in sys.stdin:
        # Print status every 10 lines
        if count != 0 and count % 10 == 0:
            stdin_print(stats, f_size)

        # Split the input line and update the count and file size
        st_list = line.split()
        count += 1

        try:
            f_size += int(st_list[-1])
        except ValueError:
            pass

        try:
            if st_list[-2] in stats:
                stats[st_list[-2]] += 1
        except IndexError:
            pass
    stdin_print(stats, f_size)


except KeyboardInterrupt:
    stdin_print(stats, f_size)
    raise
