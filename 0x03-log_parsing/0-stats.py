#!/usr/bin/python3
import sys


def print_statistics(total_size, status_counts):
    """
    Prints the statistics retrieved from the log file

    Args:
        total_size (int): total file size accumulated from the logs
        status_counts (int): total number of status code counts
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        print("{}: {}".format(code, status_counts[code]))


def main():
    """
    Retrieves the relevant data format from the collected logs
    """
    total_size = 0
    status_counts = {}

    try:
        for line_number, line in enumerate(sys.stdin, 1):
            try:
                parts = line.strip().split()
                ip_address = parts[0]
                date = parts[3][1:-1]
                status_code = int(parts[-2])
                file_size = int(parts[-1])

                # Assuming that lines not matching the format should be skipped
                if parts[5] != "GET" or parts[6] != "/projects/260" or parts[7] != "HTTP/1.1":
                    continue

                total_size += file_size
                if status_code in status_counts:
                    status_counts[status_code] += 1
                else:
                    status_counts[status_code] = 1

                # Print statistics after every 10 lines
                if line_number % 10 == 0:
                    print_statistics(total_size, status_counts)

            except (ValueError, IndexError):
                # Skip lines with incorrect format
                continue

    except KeyboardInterrupt:
        # Handle keyboard interruption and print final statistics
        print_statistics(total_size, status_counts)
        sys.exit(0)


if __name__ == "__main__":
    main()
