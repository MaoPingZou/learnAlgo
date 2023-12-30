# 栈

"""
特性：先入后出、线性数据结构

"""

# 初始化栈
# Python 没有内置的 栈 类，可以把 list 当作栈使用
stack: list[int] = []

# 元素入栈
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
stack.append(6)

# 访问栈顶元素
peek: int = stack[-1]
print("peek ==> " + str(peek))

# 弹出栈顶元素
pop: int = stack.pop()
print("pop ==> " + str(pop))

# 获取栈的长度
size: int = len(stack)
print("size ==> " + str(size))

# 判断栈是否为空
isEmpty: bool = len(stack) == 0
print("isEmpty ==> " + str(isEmpty))