#!/usr/bin/python3
#101-stats.py


def print_stats(total_size, status_codes):
    """
    Prints the computed statistics.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary containing status codes and their counts.

    Returns:
        None
    """
    print(f"File size: {total_size}")
    sorted_codes = sorted(status_codes.keys())
    for code in sorted_codes:
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def main():
    """
    Main function to read stdin, compute metrics, and print statistics.
    """
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            try:
                parts = line.split()
                total_size += int(parts[-1])
                status_code = int(parts[-2])
                if status_code in status_codes:
                    status_codes[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)

            except ValueError:
                pass  # Ignore lines with incorrect format

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()
