# This is a really simple data structure. Double linked lists are exactly the same as single linked lists, but they contain a link to their previous node as well.

class DoubleLinkedListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.previous = None
