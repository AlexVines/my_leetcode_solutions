def reverseList(head):
    '''
    Reverse a singly linked list.

    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL

    https://leetcode.com/problems/reverse-linked-list/
    '''
    prev = None
    while head:
        temp = head
        head = head.next
        temp.next = prev
        prev = temp
    return prev
