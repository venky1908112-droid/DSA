import heapq

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        heap = []
        count = 0

        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, count, head))
                count += 1

        dummy = ListNode(0)
        temp = dummy

        while heap:
            _, _, node = heapq.heappop(heap)

            temp.next = node
            temp = temp.next

            if node.next:
                heapq.heappush(heap, (node.next.val, count, node.next))
                count += 1

        return dummy.next