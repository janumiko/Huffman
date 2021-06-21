from ..src.encode import calculate_frequency
    
def test_frequency_calculation():

    # test if dictionaries with pair character : frequency are calculated properly
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