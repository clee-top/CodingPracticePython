"""
The goal is to reconstruct a binary search tree.  As input, you get two arrays.  The first is an in-order traversal of the desired tree, and the second is a post-order traversal of the tree.

Let’s start with some assumptions you’d like to make, so we can save ourselves the hassle of checking all of them in code:
* The arrays are the same length
* They are legitimate inputs
* There are no duplicate entries


         10
        /    \
      8       16
    /    \      \
   4      9      20

In order:   4, 8, 9, 10, 16, 20
Post order: 4, 9, 8, 20, 16, 10

If you’re aware of any basic libraries that can help with any of the grunt work, feel free to use them.

Write the code that reconstructs the binary tree.
What are the interesting test cases?
"""

# In order array gives you sub-trees that allow you to figure out where each subtree in reference to the root.
# The post order array gives you the guaranteed root.


# Psuedocode solution
# Write function to find the root in post order. 
# Write function that uses that root in in-order to identify and recurse on left and right sub-trees.
# Recurse should be on insert method.

# Below is the definition given by prospective employer(Cruise) during a coderpad. Solution worked.

in_order_list = [4, 8, 9, 10, 16, 20]
post_order_list = [4, 9, 8, 20, 16, 10]


# Use this as a node for your tree.
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Compare the new value with the parent node
        # Check existence
        if self.data:
            # See if it's less than or greater than (I.E need to add on the left or right)
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            # Check the other value/side of the tree.
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()


# Get first node in there. Iterate through the rest.
in_order_tree_root = Node(in_order_list[0])

for index in range(1,len(in_order_list)):
    in_order_tree_root.insert(in_order_list[index])
    # print("The current value I'm looking to add to the tree is: {}".format(str(in_order_list[index])))

in_order_tree_root.PrintTree()