from datetime import datetime
from typing import List


def sum_light(els: List[datetime]):
    seconds = 0
    for i in range(0, len(els), 2):
        seconds += int((els[i+1] - els[i]).total_seconds())
    return seconds


if __name__ == '__main__':
    print("Example:")
    print(sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
        datetime(2015, 1, 12, 11, 10, 10),
        datetime(2015, 1, 12, 12, 10, 10),
    ]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_light(els=[
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
    ]) == 610

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ]) == 1220

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
        datetime(2015, 1, 12, 11, 10, 10),
        datetime(2015, 1, 12, 12, 10, 10),
    ]) == 4820

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 1),
    ]) == 1

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 13, 11, 0, 0),
    ]) == 86410

    print("The first mission in series is completed? Click 'Check' to earn cool rewards!")

