""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
def isBST(root, min, max):
    if not root:
        return True
    if root.data < min or root.data > max:
        return False
    return isBST(root.left, min, root.data - 1) and isBST(root.right, root.data + 1, max)

def checkBST(root):
    return isBST(root, float("-inf"), float("inf"))
