
class LinkedListStack:
    """基于链表实现的栈"""

    def __init__(self):
        """构造方法"""
        self._peek: ListNode | None = None
        self._size: int = 0
    
    def size(self) -> int:
        """获取栈的长度"""
        return self._size
    
    def is_empty(self) -> bool:
        """判断栈是否为空"""
        return not self._peek
    
    def push(self, val: int):
        """入栈"""
        node = ListNode(val)
        # 头插法
        node._next = self._peek
        # self._peek 变成了新插入的 node 节点
        self._peek = node
        # 栈的siez + 1
        self._size += 1
    
    def pop(self) -> int:
        """出栈"""
        num = self.peek()
        # 将后一个节点赋值给 self._peek
        self._peek = self._peek.next
        self._size -= 1
        return num
        
    def peek(self) -> int:
        """访问栈顶元素"""
        if self.is_empty():
            raise IndexError("栈为空")
        return self._peek.val

    def to_list(self) -> list[int]:
        """转换为列表用于打印"""
        arr = []
        node = self._peek
        while node:
            arr.append(node.val)
            node = node.next
        arr.reverse()
        return arr


class ListNode:
    def __init__(self, val: int):
        """构造方法"""
        self.val: int = val
        self.next: ListNode | None = None
    