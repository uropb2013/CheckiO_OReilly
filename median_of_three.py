from typing import Iterable


def median_three(els: Iterable[int]) -> Iterable[int]:
    # your code here
    if len(list(els)) < 3:
        return els
    new_list = list(els).copy()
    result_list = [new_list[0], new_list[1]]
    for i in range(2, len(new_list)):
        if new_list[i - 2] >= new_list[i - 1] >= new_list[i] or new_list[i - 2] <= new_list[i - 1] <= new_list[i]:
            result_list.append(new_list[i - 1])
        elif new_list[i - 2] >= new_list[i] >= new_list[i - 1] or new_list[i - 2] <= new_list[i] <= new_list[i - 1]:
            result_list.append(new_list[i])
        else:
            result_list.append(new_list[i - 2])
    return result_list


if __name__ == '__main__':
    print("Example:")
    print(list(median_three([5, 2, 9, 1, 7, 4, 6, 3, 8])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(median_three([1, 2, 3, 4, 5, 6, 7])) == [1, 2, 2, 3, 4, 5, 6]
    assert list(median_three([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
