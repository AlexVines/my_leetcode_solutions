from linked_list_simple import *

list1 = add_list([1, 2, 4])
list2 = add_list([1, 3, 4])


def merge_two_lists(l1, l2) -> ListNode:
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

res = merge_two_lists(list1, list2)
res.print()
