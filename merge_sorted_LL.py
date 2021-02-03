class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    '''
    Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together
    the nodes of the first two lists.

    https://leetcode.com/problems/merge-two-sorted-lists/
    '''

    dum = ListNode(-1)
    head = dum
    while l1 and l2:
        if l1.val <= l2.val:
            dum.next = l1
            l1 = l1.next
        else:
            dum.next = l2
            l2 = l2.next
        dum = dum.next
    if l1:
        dum.next = l1
    else:
        dum.next = l2
    return head.next
