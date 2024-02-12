from ngramfrequencies import NgramFrequencies


def test():
    words = ['the', 'COMMA', 'a', 'COMMA_the', 'and_the', 'the_world_of']
    test_sample = NgramFrequencies(1)
    for _ in words:
        assert test_sample.add_item(_) == ''
