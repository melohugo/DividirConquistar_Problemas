class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge_list(l1, l2):
            aux = ListNode(0)
            atual = aux
            while l1 and l2:
                if l1.val < l2.val:
                    atual.next = l1
                    l1 = l1.next
                else:
                    atual.next = l2
                    l2 = l2.next
                atual = atual.next
            atual.next = l1 or l2
            return aux.next

        def merge_sort(lists):
            if len(lists) == 1:
                return lists[0]
            if len(lists) == 2:
                return merge_list(lists[0], lists[1])
            m = len(lists) // 2
            esquerda = merge_sort(lists[:m])
            direita = merge_sort(lists[m:])
            return merge_list(esquerda, direita)

        return merge_sort(lists)
