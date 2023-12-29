class Mylist:
    """
    实现一个简易版版本的列表，将包括以下3个重点设计：

    1、初始容量：选取一个合理的数组初始容量。这里选择 10 作为初始容量。
    2、数量纪录：变量 size，用于记录当前元素数量，随着元素插入和删除实时更新。
               根据这个变量的值可以定位列表尾部，以及判断是否需要扩容。
    3、扩容机制：如若列表容量已满，在插入新元素时需要进行扩容。
               首先创建一个新的数组，然后将源数组依次移动到新数组。
               本版本中的新数组扩容至原来的 2 倍。
    """

    def __init__(self):
        """构造函数"""
        self._capacity: int = 10 # 列表容量
        self._arr: list[int] = [0] * self._capacity # 数组（储存列表元素）
        self._size: int = 0 # 列表长度（当前元素数量）
        self._extend_ratio: int = 2 # 每次列表扩容的倍数
    
    def size(self) -> int:
        """获取列表长度（当前元素数量）"""
        return self._size
    
    def capacity(self) -> int:
        """获取列表容量"""
        return self._capacity
    
    def get(self, index: int) -> int:
        """访问元素"""
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        return self._arr[index]
    
    def set(self, num: int, index: int):
        """更新元素"""
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        self._arr[index] = num

    
    def add(self, num: int):
        """在尾部添加元素"""
        # 如果元素超出容量，触发扩容机制
        if self._size == self.capacity():
            self.extend_capacity()
        self._arr[self._size] = num
        self._size += 1

    def insert(self, num: int, index: int):
        """在中间插入元素"""
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        # 元素数量超出容量时，触发扩容机制
        if self._size == self.capacity():
            self.extend_capacity()
        # 将索引 index 以及之后的元素都向后移动一位
        for j in range(self._size - 1, index - 1, -1):
            # 将当前位置的值赋值给后一位
            self._arr[j + 1] = self._arr[j]
        # 对 index 位置赋值
        self._arr[index] = num
        # 更新元素数量
        self._size += 1
        
    def remove(self, index: int) -> int:
        """删除元素"""
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        num = self._arr[index]
        # 将索引 index 之后的元素都往前移动一位
        for i in range(index, self._size - 1):
            self._arr[i] = self._arr[i + 1]
        # 更新元素数量
        self._size -= 1
        # 返回被删除的元素值
        return num
    
    def extend_capacity(self):
        """列表扩容"""
        # 新建一个长度为原数组 _extend_ratio 倍的数组
        self._arr = self._arr + [0] * self.capacity()
        # 更新列表容量
        self._capacity = len(self._arr)
    
    def to_array(self) -> list[int]:
        """返回有效长度的列表"""
        return self._arr[ : self._size]