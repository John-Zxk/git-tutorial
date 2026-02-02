class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        

# class Node:
#     def __init__(self, prev, element, next):
#         self.val = element
#         self.next = next
#         self.prev = prev

# 输入一个数组，转换为一条单链表
def createLinkedList(arr: 'List[int]')-> 'ListNode':
    if arr is None or len(arr) == 0:
        return None
    
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head
    
# 增

# 在单链表头部插入新元素    
head = createLinkedList([1, 2, 3, 4, 5])

newNode = ListNode(0)
newNode.next = head
head = newNode
# 遍历单链表
p = head
while p is not None:
    print(p.val)
    p = p.next