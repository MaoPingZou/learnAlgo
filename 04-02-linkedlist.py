# 链表

"""
链表 是一种线性数据结构。其中每一个节点都是一个节点对象。各个节点通过“引用”相连接。
“引用”记录下了下一个节点的内存地址，通过该地址可以从当前节点访问到下一个节点。

链表的优缺点：
优点：内存空间利用效率高、可灵活拓展、添加和删除元素效率高 O(1)
缺点：元素占用内存空间多、访问元素效率低 O(n)

常见链表类型：单向链表、环形链表、双向链表

典型应用场景
单向链表：栈（先进后出）、队列（先进先出）、哈希表（解决哈希冲突）、图
环形链表：高级数据结构（红黑树、B树）、浏览器历史（页面前进后退）、LRU 算法
双向链表：时间片轮转调度算法（CPU 调度算法）、数据缓冲区
"""

# 单向链表
class ListNode:
    """LinkedList Node Class"""
    def __init__(self, val):
        self.val: int = val               # 节点值
        self.next: ListNode | None = None # 指向下一个节点的引用

# 双向链表
class BidirectionalListNode:
    """Bidirectional LinkedList Node Class"""
    def __init__(self, val: int):
        self.val: int = val
        self.next: ListNode | None = None
        self.prex: ListNode | None = None

# 链表常用操作
#    ||
#    ||
#    \/

# 1、初始化链表
n0 = ListNode(1)
n1 = ListNode(5)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
# 构建节点之间的引用
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

# 2、插入节点
def insert(n0: ListNode, insertNode: ListNode):
    """在 currentNode 节点之后插入 insertNode 节点"""
    temp = n0.next
    insertNode.next = temp
    n0.next = insertNode

# 3、删除节点
def remove(n0: ListNode):
    """删除节点 currentNode 之后的一个节点"""
    if not n0.next:
        return
    # n0 -> P -> n1
    p = n0.next
    n1 = p.next
    n0.next = n1

# 4、访问节点
def access(head: ListNode, index: int) -> ListNode | None:
    """访问节点中索引为 index 的节点"""
    for _ in range(index):
        if not head:
            return
        head = head.next
    return head    
    
# 5、查找节点
def find(head: ListNode, target: int) -> int:
    """在链表中查找值为 target 的首个节点"""
    index = 0
    while head:
        if head.val == target:
            return index
        head = head.next
        index += 1
    return -1

