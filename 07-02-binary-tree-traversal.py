import deque
# 二叉树遍历

"""
常见的二叉树遍历方式有：层序遍历、前序遍历、中序遍历、后续遍历
"""

class TreeNode:
    """二叉树节点类"""
    def __init__(self, val: int):
        self.val: int = val                 # 节点值
        self.left: TreeNode | None = None   # 左子节点引用
        self.right: TreeNode | None = None  # 右子节点引用

## 层序遍历 level-order traversal
"""
层序遍历本质上属于【广度优先遍历 breadth-first traversal】，也称为【广度优先搜索 breadth-first search，BFS】，它体现了一种“一圈一圈向外扩展”的逐层遍历方式

BFS 通常借助【队列】数据结构来实现
"""
def level_order(root: TreeNode | None):

    # 初始化队列，加入根节点
    queue: deque[TreeNode] = deque()
    queue.append(root)
    # 初始化一个列表，用于保存遍历序列
    res = []
    while queue:
        node: TreeNode = queue.popleft() # 队列出队
        res.append(node.val)
        if node.left is not None:
            queue.append(node.left) # 左子节点入队
        if node.right is not None:
            queue.append(node.right) # 右子节点入队
    return res
    
## 前序遍历、中序遍历、后序遍历
"""
这三种遍历都属于【深度优先遍历 depth-first traversal】，也称为【深度优先搜索 depth-first search, DFS】，它体现了一种“先走到尽头，再回溯继续”的遍历方式

DFS 通常基于【递归】实现 （也可以通过【迭代】实现）
"""
res = []
def pre_order(root: TreeNode | None):
    """
    前序遍历：根节点 -> 左子树 -> 右子树
    """ 
    if root is None:
        return
    res.append(root.val)
    pre_order(root=root.left)
    pre_order(root=root.right)

def in_order(root: TreeNode | None):
    """
    中序遍历：左子树 -> 根节点 -> 右子树
    """ 
    if root is None:
        return
    pre_order(root=root.left)
    res.append(root.val)
    pre_order(root=root.right)

def post_order(root: TreeNode | None):
    """
    后序遍历：左子树 -> 右子树 -> 根节点
    """ 
    if root is None:
        return
    post_order(root=root.left)
    post_order(root=root.right)
    res.append(root.val)
    