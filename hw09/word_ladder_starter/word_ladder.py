from queue1 import Queue1
from stack import Stack


# class WordLadder:
#     """A class providing functionality to create word ladders"""
#     # TODO:
#     # Implement whatever functionality is necessary to generate a
#     # stack representing the word ladder based on the parameters
#     # passed to the constructor.
#     def __init__(self, w1, w2, wordlist):
#         self.queue = Queue1()
#         self.stack_of_word = Stack()
#         self.new_stack = Stack()
#         self.w1 = w1
#         self.w2 = w2
#         self.wordlist = wordlist

#     def make_ladder(self):
#         self.stack_of_word.push(self.w1)
#         self.queue.enqueue(self.stack_of_word)
#         if len(self.w1) != len(self.w2):
#             return None
#         # dequeue to create candidates
#         while not self.queue.isEmpty():
#             cur_stack = self.queue.dequeue()
#             # cur_word is a string
#             cur_word = cur_stack.peek()
#             alphas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
#                       'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
#                       'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#             candidate = cur_word
#             for i in range(len(cur_word)):
#                 # reset the candidate
#                 candidate = cur_word
#                 for j in range(0, 26):
#                     if candidate[i] != alphas[j]:
#                         # substitute one character
#                         new_word = cur_word[:i] + alphas[j] + cur_word[i+1:]
#                         if new_word in self.wordlist:
#                             new_stack = cur_stack.copy()
#                             new_stack.push(new_word)
#                             if new_word == self.w2:
#                                 return new_stack
#                             else:
#                                 self.queue.enqueue(new_stack)

#         # if the Q is empty, return None
#         if self.queue.isEmpty():
#             return None
class WordLadder:
    def __init__(self, w1, w2, wordlist):
        self.stack = Stack()
        self.queue = Queue1()
        self.w1 = w1
        self.w2 = w2
        self.wordlist = wordlist  # Convert to set for efficiency

    def make_ladder(self):
        self.stack.push(self.w1)
        self.queue.enqueue(self.stack)
        if len(self.w1) != len(self.w2):
            return None
        alphas = 'abcdefghijklmnopqrstuvwxyz'

        while not self.queue.isEmpty():
            cur_stack = self.queue.dequeue()
            cur_word = cur_stack.peek()

            for i in range(len(cur_word)):
                for char in alphas:
                    if char != cur_word[i]:
                        new_word = cur_word[:i] + char + cur_word[i+1:]
                        if new_word in self.wordlist:
                            new_stack = cur_stack.copy()
                            new_stack.push(new_word)
                            if new_word == self.w2:
                                return new_stack
                            else:
                                self.queue.enqueue(new_stack)

        return None
