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

in_order_list = [4, 8, 9, 10, 16, 20]
post_order_list = [4, 9, 8, 20, 16, 10]
