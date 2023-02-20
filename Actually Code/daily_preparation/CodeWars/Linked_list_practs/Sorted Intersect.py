"""Linked Lists All Methods
Write a SortedIntersect() function which creates and 
returns a list representing the intersection of two lists
that are sorted in increasing order. Ideally, each list should 
only be traversed once. The resulting list should not contain duplicates.

var first = 1 -> 2 -> 2 -> 3 -> 3 -> 6 -> null
var second = 1 -> 3 -> 4 -> 5 -> -> 6 -> null
sortedIntersect(first, second) === 1 -> 3 -> 6 -> null
"""


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def sorted_intersect(first, second):
    pass