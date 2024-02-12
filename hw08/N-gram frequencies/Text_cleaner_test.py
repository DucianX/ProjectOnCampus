from textcleaner import TextCleaner


def test():
    clr = TextCleaner()
    assert clr.process("ASHER") == [['asher']]
    assert clr.process(",") == [['COMMA']]
    assert clr.process("WON'T") == [["won't"]]
    assert clr.process("Yes, no, yes! ") == [['yes','COMMA', 'no', 'COMMA', 'yes']]
    assert clr.process("Today is yesterday. I am Travis Scott.") == [['today', 'is', 'yesterday','i', 'am', 'travis', 'scott']]
