import types


def flat_generator(list_of_lists):
    for sublist in list_of_lists:
        for item in sublist:
            yield item


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    expected_output = ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    for flat_iterator_item, check_item in zip(flat_generator(list_of_lists_1), expected_output):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == expected_output

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
