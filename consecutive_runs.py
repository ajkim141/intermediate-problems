__author__ = 'Alex Kim'

import unittest

test_list = [1, 1, 3, 5, 6, 8, 10, 11, 10, 9, 8, 9, 10, 11, 7, 6]
# [3, 6, 7, 10, 14]


def run_length(lst, start, direction):

    """
    :param lst: A list of numbers.
    :param start: The index within lst at which to begin checking.
    :param direction: 1 if the consecutive run is increasing, -1 if decreasing.
    :return: The length of the consecutive run beginning at index start.
    """
    length = 0
    i = start

    while lst[i] + direction == lst[i + 1] and i < len(lst) - 1:
        length += 1
        i += 1
    return length


def find_runs(num_list):

    """
    :param num_list: A list of numbers within which to search for consecutive runs.
    :return: A list of indices within num_list at which consecutive runs start.
    """
    result = []
    i = 0

    while i < len(num_list) - 1:
        if num_list[i] + 1 == num_list[i + 1]:
            result.append(i)
            if i < len(num_list) - 2:
                i += run_length(num_list, i, 1)
            else:
                i += 1
        elif num_list[i] - 1 == num_list[i + 1]:
            result.append(i)
            if i < len(num_list) - 2:
                i += run_length(num_list, i, -1)
            else:
                i += 1
        else:
            i += 1
    return result


class TestRun(unittest.TestCase):

    def test_example(self):
        result = find_runs(test_list)
        self.assertEqual(result, [3, 6, 7, 10, 14], "Run Detection Failed")

if __name__ == '__main__':
    unittest.main()