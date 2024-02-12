from word_ladder import WordLadder


def test():
    valid_words = {}
    with open('words_alpha.txt') as word_file:
        for w in word_file.read().split():
            if len(w) in valid_words.keys():
                # Add to an existing set
                valid_words[len(w)].add(w)
            else:
                # Initialize a set with one element
                valid_words[len(w)] = {w}

    w1, w2 = "love", "hate"
    wl = WordLadder(w1, w2, valid_words[len(w1)])
    test_stack = wl.make_ladder()
    assert test_stack.output1() == ["love", "hove", "have", "hate"]

    w1, w2 = "angel", "devil"
    wl = WordLadder(w1, w2, valid_words[len(w1)])
    test_stack2 = wl.make_ladder()
    assert test_stack2.output1() == ["angel", "anger", "aeger", "leger", "lever", "level", "devel", "devil"]

    w1, w2 = "earth", "ocean"
    wl = WordLadder(w1, w2, valid_words[len(w1)])
    test_stack3 = wl.make_ladder()
    assert test_stack3.output1() == ["earth", "barth", "barih", "baris", "batis", "bitis", "aitis", "antis", "antas", "antal", "ontal", "octal", "octan", "ocean"]
