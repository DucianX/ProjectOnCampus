from stack import Stack
# Is there any wrong with my code? I succeed in manually running
# tests but always fail the "^" test.


class StringProcessor:
    """Class for processing strings"""
    def __init__(self):
        self.string_stack = Stack()

    def process_string(self, line):
        self.result_list = []
        decoded_string = ''
        # Reset the list!
        # Otherwise the elements from last call will remain in it.
        for char in line:
            if char == '*':
                self.result_list.append(self.string_stack.pop())
                # print("pop one char")
            elif char == '^':
                TWO = 2
                for i in range(TWO):
                    if not self.string_stack.empty():
                        self.result_list.append(self.string_stack.pop())
            else:
                self.string_stack.push(char)

        if len(self.result_list) > 0:
            decoded_string = ''.join(self.result_list[::1])
            return decoded_string
        else:
            return ""
