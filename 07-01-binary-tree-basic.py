# 二叉树

"""
二叉树是一种【非线形】数据结构，代表“祖先”和“后代”之间的派生关系，体现了“一分为二”的分治逻辑。

二叉树中最基本的单元是树节点，每个节点包含值、左子节点引用和右子节点引用

在二叉树中，除叶节点外，其他所有节点都包含子节点和非空子树。
"""

"""
二叉树常见术语：

-【根节点 root node】：位于二叉树的顶层，没有父节点
-【叶节点 Leaf node】：没有子节点的节点，其两个指针都是指向 None
-【边 edge】：两个节点之间的连线，即节点引用（指针）
- 节点所在的【层 level】：根节点所在层为1，从顶至底递增
- 节点的【度 degree】：节点的子节点数量，在二叉树中，度的取值范围为0、1、2
- 二叉树的【高度 height】：从根节点到最远叶节点所经过的边的数量
- 节点的【深度 depth】：从根节点到该节点所经过的边的数量
- 节点的【高度 height】：从该节点到距离该节点最远的叶节点所经过的边的数量
"""

"""
常见二叉树类型

- 完美二叉树 perfect binary tree（满二叉树）：所有层的所有节点都被完全填满
- 完全二叉树 complete binary tree：只有最底层的节点未被填满，且最底层节点尽量靠左填充
- 完满二叉树 full binary tree：除了叶子节点外，其余所有节点都有两个字节点
- 平衡二叉树 balance binary tree：树中任意节点的左子树和右子树的高度之差的绝对值不超过 1
"""

"""
二叉树的退化

理想状态：满二叉树（完美二叉树 perfect binary tree），可以充分发挥二叉树“分治”的优势
最差状态：退化为链表，时间复杂度退化至O(n)
"""

class TreeNode:
    """二叉树节点类"""
    def __init__(self, val: int):
        self.val: int = val                 # 节点值
        self.left: TreeNode | None = None   # 左子节点引用
        self.right: TreeNode | None = None  # 右子节点引用
    

# 二叉树的基本操作
## 初始化节点
n1 = TreeNode(val=1)
n2 = TreeNode(val=2)
n3 = TreeNode(val=3)
n4 = TreeNode(val=4)
n5 = TreeNode(val=5)
## 构建节点之间的引用（指针）
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5

## 插入节点
p = TreeNode(0)
# 在 n1 -> n2 中间插入节点 P
n1.left = p
p.left = n2
## 删除节点 p
n1.left = n2
## 需要注意的是：1、插入节点可能会改变二叉树的原有逻辑结构
##             2、删除节点通常意味着删除该节点以及其所有子树
