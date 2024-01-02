# 基于链表的队列实现
# 将链表的“头节点”和“尾节点”分别视为“队首”和“队尾”，规定队尾仅可添加节点，队首仅可删除节点。


class LinkedListQueue:
    """基于链表的队列实现"""

    def __init__(self):
        """构造方法"""
        self._front: ListNode | None = None # 头节点 front
        self._rear: ListNode | None = None # 尾节点 rear
        self._size: int = 0
    
    def size(self) -> int:
        """获取队列的长度"""
        return self._size

    def is_empty(self) -> bool:
        """判断队列是否为空"""
        return not self._front
    
    def push(self, num: int):
        """入队"""
        # 在尾节点后添加 num
        node = ListNode(num)
        # 如果队列为空，则令头、尾节点都指向该节点
        if self._front is None:
            self._front = node
            self._rear = node
        # 如果队列不为空，则将该节点添加到尾节点后
        else:
            self._rear.next = node
            self._rear = node
        self._size += 1
    
    def pop(self) -> int:
        """出队"""
        num = self.peek()
        # 删除头节点
        self._front = self._front.next
        self._size -= 1
        return num
    
    def peek(self) -> int:
        """访问队首元素"""
        if self.is_empty():
            raise IndexError("队列为空")
        return self._front.val
    
    def to_list(self) -> list[int]:
        """转换为列表用于打印"""
        queue = []
        temp = self._front
        while temp:
            queue.append(temp.val)
            temp = temp.next
        return queue
    
class ListNode:
    def __init__(self, val: int):
        """构造方法"""
        self.val: int = val
        self.next: ListNode | None = None