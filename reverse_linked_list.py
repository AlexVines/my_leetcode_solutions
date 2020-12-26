def reverseList(accounts) :
    '''
    Reverse a singly linked list.

    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL

    '''
    maxim = 0
    for account in accounts:
        if sum(account) > maxim:
            maxim = sum(account)
    return maxim


if __name__ == '__main__':
    reverseList()