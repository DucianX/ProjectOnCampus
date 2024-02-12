from stack import Stack


class AnBnCn:
    """Class for evaluating strings of N a's followed by N b's"""
    def __init__(self):
        self.stack_a = Stack()
        self.stack_b = Stack()

    def accept(self, in_string):
        """Takes a string and returns a boolean
        indicating whether the string matches the pattern"""
        expect_a = True
        expect_b = True
        once_had_a = False
        for char in in_string:
            if char == 'a':
                once_had_a = True
                if expect_a:  # make sure a won't appear behind b
                    self.stack_a.push(char)
                else:
                    return False
            elif char == 'b':
                if once_had_a:
                    # make sure 'b' won't appear before at least one 'a'
                    expect_a = False  # no more 'a'
                    # if expect_b:  # make sure b won't appear behind c
                    #     if self.stack_a.is_empty():
                    #         # make sure the stack won't be empty too soon
                    #         return False
                    #     else:
                    #         self.stack_a.pop()
                    #         self.stack_b.push(char)
                    # else:
                    #     return False
                    # lower is the improved version of it.
                    if (expect_b and not self.stack_a.is_empty()):# make sure b won't appear behind c
                            self.stack_a.pop()
                            self.stack_b.push(char)
                    else:
                        return False
                else:
                    return False
            elif char == 'c':
                expect_b = False  # no more 'b'
                if not expect_a:  # make sure c does not appear right after a
                    if self.stack_b.is_empty():
                        # make sure the stack won't be empty too soon
                        return False
                    else:
                        self.stack_b.pop()
                else:
                    return False

        return (self.stack_b.is_empty() and self.stack_a.is_empty())
        # At the end of the day, two stacks should both be empty

    def clear(self):
        self.stack = Stack()
