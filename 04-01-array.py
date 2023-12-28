import random
# 数组

"""
Q：为什么数组的索引是从0开始的？
A：从计算机的内存地址计算公式看，索引本质上是内存地址的偏移量。
首个元素的地址偏移量为是0，因此它的索引为0。

数组的优缺点：
优点：空间效率高、支持随机访问、缓存局部性
缺点：插入与删除效率较低、长度不可变、空间浪费

数组的典型应用：随机访问、搜索和排序、查找表、机器学习、数据结构实现
"""

# 1.初始化数组
arr: list[int] = [0] * 5 # [0, 0, 0, 0, 0]
nums: list[int] = [1, 3, 2, 5, 4]

# 2.访问元素
def random_access(nums: list[int]) -> int:
    """随机访问元素"""
    # 在区间 [0, len(nums) - 1]中随机抽取一个数字
    random_index = random.randint(0, len(nums) -1)
    # 通过索引获取并返回随机元素
    random_num = nums[random_index]
    return random_num


# 3.插入元素
def insert(nums: list[int], num: int, index: int):
    # 把索引 index 以及之后的所有元素向后移动一位
    for i in range(len(nums) - 1, index, -1):
        nums[i] = nums[i - 1]
    # 将 num 赋值给 index 的位置
    nums[index] = num
    
    
# 4.删除元素
def delete(nums: list[int], index:int):
    # 把索引 index 之后的所有元素向前移动一位
    for i in range(index, len(nums) - 1):
        nums[i] = nums[i + 1]

# 5.遍历数组
def traverse(nums: list[int]):
    count = 0
    # 通过索引遍历数组
    for i in range(len(nums)):
        count += nums[i]
    # 遍历数组元素
    for num in nums:
        count += num
    # 同时遍历索引和元素
    for i, num in enumerate(nums):
        count += nums[i]
        count += num

# 6.查找元素
def find(nums: list[int], target: int) -> int:
    # 直接遍历查找
    count = -1
    for num in nums:
        if num == target:
            count = num
    # 通过索引遍历查找
    for i in range(len(nums)):
        if nums[i] == target:
            count = nums[i]
    return count

# 7.扩容数组
def extend(nums: list[int], enlarge: int) -> list[int]:
    # 初始化一个扩展长度后的数组
    res = [0] * (len(nums) + enlarge)
    # 将原数组的值复制到新数组
    for i in range(len(nums)):
        res[i] = nums[i]
    # 返回扩展后的新数组
    

        

        
