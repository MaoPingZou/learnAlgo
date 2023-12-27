import random

# 此算法的运行时间为：1 + 1 + 10 + （1 + 5）* n = 6n + 12
def algorithm(n: int):
    a = 2              # 1 ns
    a = a + 1          # 1 ns
    a = a * 2          # 10 ns
    for _ in range(n): # 1 ns
        print(0)       # 5 ns 

# 算法 A 的时间复杂度为 常数阶
def algorithm_A(n: int):
    print(0)
# 算法 B 的时间复杂度为 线性阶
def algorithm_B(n: int):
    for _ in range(n):
        print(0)
# 算法 C 的时间复杂度为 常数阶
def algorithm_C(n: int):
    for _ in range(1000000):
        print(0)

# 常数阶：算法运行时间不随输入数据 n 的增大而增大
# 线性阶：算法运行时间随着输入数据 n 的增大呈线性增长

        
# 统计技巧：1、忽略常数项；2、省略所有系数；3、循环嵌套时使用乘法。
# T(n) = 2n(n+1)+(5n+1)+2 = 2n^2 + 7n + 3
# T(n) = n^2 + n
def algorithm_trick(n: int):
    a = 1           # +0（技巧 1）
    a = a + n       # +0（技巧 1）
    # +n（技巧 2）
    for i in range(5 * n + 1):
        print(0)
    # +n*n（技巧 3）
    for i in range(2 * n):
        for j in range(n + 1):
            print(0)

"""
时间复杂度由 T(n) 中最高阶的项来决定。
这是因为在 n 趋于无穷大时，最高阶的项将发挥主导作用，其他项的影响可以忽略。
"""
    
"""
常见的时间复杂度类型为：
O(1)  < O(log n) <  O(n) < O(n log n) < O(n^2) < O(2^n) < O(n!)
常数阶 <  对数阶   < 线性阶 <  线性对数阶  < 平方阶  < 指数阶  < 阶乘阶
"""

# 常数阶：算法运行时间不随输入数据 n 的大小而变化
def constant(n: int):
    """常数阶"""
    count = 0
    size = 100000
    for _ in size:
        count += 1
    return count

# 对数阶：每轮缩小到一半
def logarithmic(n: float) -> int:
    """对数阶（循环实现）"""
    count = 0
    while n > 1:
        # 减半
        n = n / 2
        count += 1
    return count

# 线性阶：算法运行时间随着数据量增大而增大
def linear(n: int) -> int:
    """线性阶"""
    count = 0
    for _ in range(n):
        count += 1
    return count

def linear_list(nums: list[int]) -> int:
    """线性阶（遍历数组）"""
    count = 0
    for i in nums:
        count += 1
    return count

# 线性对数阶：
def linear_log_recur(n: float) -> int:
    """线性对数阶"""
    # 递归终止条件
    if n <= 1:
        return 1
    count: int = linear_log_recur(n // 2) + linear_log_recur(n // 2)
    for _ in range(n):
        count += 1
    return count

# 平方阶
def square(n: int) -> int:
    """平方阶"""
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count

# 指数阶
def exponential(n: int) -> int:
    """指数阶(循环实现)"""
    count = 0
    base = 1
    # 每轮一分为二，形成数列 1，2，4，8，...，2^(n-1)
    for _ in range(n):
        for _ in range(base):
            count += 1
        base *= 2
    # count = 1 + 2 + 4 + 8 + ... + 2^(n - 1) = 2^n - 1
    return count


# 阶乘阶
# 当 n >= 4 时恒有 n!>2^n，所以阶乘阶比指数阶增长更快，在 n 较大时也是不可接受的
def factorial_recur(n: int) -> int:
    """阶乘阶（递归实现）"""
    if n == 0:
        return 1
    count = 0
    # 从 1 个分裂出 n 个
    for _ in range(n):
        count += factorial_recur(n - 1)
    return count


# 最佳、最差、平均时间复杂度
def random_numbers(n: int) -> list[int]:
    """生成一个数组，元素为：1, 2, 3, ..., n, 顺序被打乱"""
    # 生成数组：nums =: 1，2，3, ..., n
    nums = [i for i in range(1, n+1)]
    # 随机打乱元素
    random.shuffle(nums)
    return nums
def find_one(nums: list[int]) -> int:
    """查找数组 nums 中数字 1 所在索引"""
    for i in range(len(nums)):
        # 当元素 1 在数组头部时，达到最佳时间复杂度 O(1)
        # 当元素 1 在数组尾部时，达到最差时间复杂度 O(n)
        if nums[i] == 1:
            return i
    return -1

"""
最佳时间复杂度在实际中很少使用，因为通常只有很小概率下能达到。
相较之下，最差时间复杂度更为实用，因为它给出了一个效率安全值。也就是说，最差就是这样了，没有比这更差的效率了。但最差时间复杂度依然不能真实地反映出算法运行效率。
相比之下，平均时间复杂度可以体现算法在随机输入数据下的运行效率。
"""
