# 列表

"""
抽象的数据结构概念，表示元素的有序集合。
支持元素访问、修改、添加、删除和遍历等操作。
与数组相比，列表无须考虑容量限制问题。

列表可以基于数组或链表实现。
"""

# 列表常用操作

# 初始化列表
nums1: list[int] = [] # 无初始值
nums2: list[int] = [1,3,2,4,5] # 有初始值

# 访问元素
num1: int = nums1[1] # 访问索引为 1 的元素

# 更新元素值
nums2[1] = 0 # 更新索引 1 的值为 0

# 插入元素
nums1.clear() # 清空列表

## 在尾部添加元素
nums1.append(1)
nums1.append(2)
nums1.append(3)
nums1.append(4)

## 在中间插入元素
nums1.insert(3, 6) # 在索引为 3 的位置插入数字 6

# 删除元素
nums1.pop(3) # 删除索引为 3 的数字

# 遍历列表
for num in nums1: # 直接遍历元素
    print(num)
for i in range(len(nums1)): # 根据索引遍历
    print(nums1[i])

# 拼接列表
list1: list[int] = [6,7,8,9,10]
list2: list[int] = [1,2,3,4,5]
listAll = list2 + list1

# 排序列表
listAll.sort() # 升序
listAll.sort(reverse=True) # 倒序

