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
    
# 在单链表尾部插入新元素

head = createLinkedList([1, 2, 3, 4, 5])
p = head 
while p.next is not None:
    p = p.next

p.next = ListNode(6)


p = head 
while p is not None:
    print(p.val)
    p = p.next


# 在单链表中间插入新元素
head = createLinkedList([1, 2, 3, 4, 5])
p = head
for i in range(0, 2):
    print(p.val)
    p = p.next
   
# 此时 p 指向第 3 个节点
# 组装新节点的后驱指针
new_node = ListNode(66)
new_node.next = p.next

# 插入新节点
p.next = new_node

# 现在链表变成了 1 -> 2 -> 3 -> 66 -> 4 -> 5

p = head 
while p is not None:
    print(p.val)
    p = p.next

