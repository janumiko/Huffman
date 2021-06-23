from ..src.encode import calculate_frequency, create_tree


def test_frequency_calculation():

    frequency_1 = calculate_frequency("aabbcc")
    assert frequency_1[0] == ('a', 2)
    assert frequency_1[1] == ('b', 2)
    assert frequency_1[2] == ('c', 2)

    frequency_2 = calculate_frequency("abbccc")
    assert frequency_2[0] == ('c', 3)
    assert frequency_2[1] == ('b', 2)
    assert frequency_2[2] == ('a', 1)

    frequency_empty = calculate_frequency("")
    assert frequency_empty == []


def test_create_tree():

    tree_1 = create_tree([('a', 2), ('b', 2), ('c', 2)])
    assert tree_1 == {'b': '11', 'c': '10', 'a': '0'}

    tree_2 = create_tree([('c', 3), ('b', 2), ('a', 1)])
    assert tree_2 == {'a': '00', 'b': '01', 'c': '1'}
