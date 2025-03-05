class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.other_index = 0
        self.inner_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.other_index < len(self.list_of_list):
            current_list = self.list_of_list[self.other_index]
            if self.inner_index < len(current_list):
                value = current_list[self.inner_index]
                self.inner_index += 1
                return value
            else:
                self.inner_index = 0
                self.other_index += 1
        raise StopIteration


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]