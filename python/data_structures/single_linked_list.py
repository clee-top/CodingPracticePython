# This is a really simple data structure. Singly linked lists contain their value and a link to the next node and nothing else.
# Mostly used for very simple problems.

class SingleLinkedListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
