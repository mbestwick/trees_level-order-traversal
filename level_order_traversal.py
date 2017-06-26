"""
You are given a pointer to the root of a binary tree. You need to print the
level order traversal of this tree. In level order traversal, we visit the nodes
level by level from left to right. You only have to complete the function. For
example:

     1
      \
       2
        \
         5
        /  \
       3    6
        \
         4

For the above tree, the level order traversal is 1 -> 2 -> 5 -> 3 -> 6 -> 4.

Output Format
Print the values in a single line separated by a space.

"""


def levelOrder(root):
    to_visit = [root]
    while to_visit:
        # pop to_visit[0]
        curr = to_visit.pop(0)
        # print its data
        print curr.data,
        # if root.left, append
        if curr.left:
            to_visit.append(curr.left)
        # if root.right, append
        if curr.right:
            to_visit.append(curr.right)
