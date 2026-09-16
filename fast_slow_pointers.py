class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    """Floyd's cycle detection: slow moves 1 step, fast moves 2.
    They meet iff there's a cycle.

    Use when: linked-list cycle detection, "find duplicate number"
    (treat array as implicit linked list via indices).
    Time: O(n). Space: O(1).
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def find_middle(head):
    """Fast/slow pointers: when fast reaches the end, slow is at the
    middle (second middle for even length).

    Use when: need the middle node without knowing the length up front,
    e.g. splitting a list in half.
    Time: O(n). Space: O(1).
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next, b.next = b, c
    assert not has_cycle(a)
    c.next = a
    assert has_cycle(a)

    a.next = b = ListNode(2)
    b.next = ListNode(3)
    b.next.next = ListNode(4)
    assert find_middle(a).val == 3
    print("ok")
