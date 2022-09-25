import turtle
import friction


randintx=friction.rix(3)
print(randintx)
# Id this a data format that needs to be strached in to 2 coordinates the data format is ?
# this is --> (5680, 0)

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

