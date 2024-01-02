# 队列

from collections import deque

# 初始化队列
# 在 Python 中，一般将双向队列类 deque 当作队列使用
queue: deque[int] = deque()

# 元素入队
queue.append(1)
queue.append(5)
queue.append(3)
queue.append(2)
queue.append(4)

# 访问队首元素
front: int = queue[0]

# 元素出队
pop: int = queue.popleft()

# 获取队列的长度
size: int = len(queue)

# 判断队列是否为空
is_empty: bool = len(queue) == 0