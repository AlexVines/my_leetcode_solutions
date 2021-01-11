class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def add(self, value):
        itr = self
        while itr.next:
            itr = itr.next
        itr.next = ListNode(value, None)

    def print(self):
        while self.next:
            print(self.val)
            self = self.next
        print(self.val)


def get_decimal_value(head: ListNode) -> int:
    val = 0
    while head is not None:
        val = 2 * val + head.val
        head = head.next
    return val


def add_list(nums):
    link = ListNode(nums[0])
    for i in range(1, len(nums)):
        link.add(nums[i])
    return link


# nums_list = [1, 0, 0, 1, 1, 1]
# ln = add_list(nums_list)
# ln.print()
