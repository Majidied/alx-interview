#!/usr/bin/python3
"""
log parsing
"""

import sys
import re


def output(log: dict) -> None:
    """
    helper function to display stats
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code]:
            print("{}: {}".format(code, log["code_frequency"][code]))


if __name__ == "__main__":
    regex = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)'
    )  # nopep8

    line_count = 0
    log = {}
    log["file_size"] = 0
    log["code_frequency"] = {
        str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]
    }

    try:
        for line in sys.stdin:
            match = regex.match(line)
            if match:
                status_code, file_size = match.groups()
                log["file_size"] += int(file_size)
                if status_code in log["code_frequency"]:
                    log["code_frequency"][status_code] += 1
                else:
                    log["code_frequency"][status_code] = 1

            line_count += 1
            if line_count % 10 == 0:
                output(log)

    except KeyboardInterrupt:
        output(log)
        sys.exit()

    finally:
        output(log)
