import copy


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return "<Node %s>" % self.data


def linkedlreverse(start, end=None, last=None):
    if start.next == end:
        start.next = last
        return start
    start_copy = copy.copy(start)
    start.next = last
    print "Start: ", start, start.next
    return linkedlreverse(start_copy.next, end, start)
