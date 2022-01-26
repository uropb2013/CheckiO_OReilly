new_array = []


def flat_list_new(array):
    global new_array
    for item in array:
        if isinstance(item, list):
            flat_list_new(item)
        else:
            new_array.append(item)


def flat_list(array):
    global new_array
    flat_list_new(array)
    res_array = new_array.copy()
    new_array.clear()
    return res_array


if __name__ == '__main__':
    print(flat_list([1, [2, 2, 2], 4]))
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')