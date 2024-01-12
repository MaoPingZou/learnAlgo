# AVL 树

"""
原来之所以叫 AVL 树，是因为取的发明这个数据结构的两位联合作者的名字首字母。

AVL 树其实是一个 平衡二叉搜索树 Balanced Binary Search Tree，它的特征：
- 即是二叉搜索树也是平衡二叉树，因此同时满足这两类二叉树的所有性质：
    - 对于根节点，左子树所有节点的值 < 根节点 < 右子树所有节点的值。任意节点的左、右子树也都是二叉搜索树。（二叉搜索树特征）
    - 任意节点的左子树和右子树的高度之差的绝对值不超过 1 （平衡二叉树特征）
- 各种操作的时间复杂度都保持在 O(log n) 级别

AVL 树常见术语：
1、节点高度：是指该节点到它的最远叶节点的距离，即所经过的“边”的数量。(叶节点的高度为0，而空节点的高度为 -1)
2、节点平衡因子：定义为节点左子树的高度减去节点右子树的高度，同时规定空节点的平衡因子为0。（当节点平衡因子的绝对值大于 1 ，说明该节点是一个失衡节点。）

AVL 树有一个明显的特点，就是：它有旋转操作。
这个操作能够在不影响二叉树的中序遍历序列的前提下，使失衡节点重新恢复平衡。换句话说就是，旋转操作既能保持“二叉搜索树”的性质，也能使树重新变成“平衡二叉树”。

旋转操作分为四类：右旋、左旋、先左旋后右旋、先右旋后左旋。
如何选择旋转操作，参考下面表格：
+-----------------+---------------+---------------+
| 失衡节点的平衡因子 | 子节点的平衡因子 | 应采用的旋转方法 |
+-----------------+---------------+---------------+
|   > 1 (左偏树)   |     >= 0      |   右旋         |
+-----------------+---------------+---------------+
|   > 1 (左偏树)   |     < 0       |   先左旋后右旋  |
+-----------------+---------------+---------------+
|   < -1 (右偏树)  |     <= 0      |   左旋         |
+-----------------+---------------+---------------+
|   < -1 (右偏树)  |     > 0       |   先右旋后左旋  |
+-----------------+---------------+---------------+
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))
from tree_node import TreeNode, print_tree

class AVLTree:
    """AVL 树"""

    def __init__(self):
        """构造方法"""
        self._root = None
    
    def get_root(self) -> TreeNode | None:
        """获取根节点"""
        return self._root
    
    def heigh(self, node: TreeNode | None) -> int:
        """获取节点高度"""
        # 空节点高度为 -1，叶节点高度为 0
        if node is not None:
            return node.height
        return -1
    
    def update_height(self, node: TreeNode | None):
        """更新节点高度"""
        # 节点高度等于最高子树高度 + 1
        node.height = max([self.heigh(node.left), self.heigh(node.right)]) + 1
    
    def balance_factor(self, node: TreeNode | None) -> int:
        """获取平衡因子"""
        # 空节点平衡因子为 0
        if node is None:
            return 0
        # 平衡因子值 = 左子树高度 - 右子树高度
        return self.heigh(node.left) - self.heigh(node.right)

    def right_rotate(self, node: TreeNode | None) -> TreeNode | None:
        """右旋"""
        child = node.left
        grand_child = child.right
        # 以 child 为原点，将 node 向右旋转
        child.right = node
        node.left = grand_child
        # 更新节点高度
        self.update_height(node)
        self.update_height(child)
        # 返回旋转后子树的根节点
        return child

    def left_rotate(self, node: TreeNode | None) -> TreeNode | None:
        """左旋"""
        child = node.right
        grand_child = child.left
        # 以 child 为原点，将 node 向左旋转
        child.left = node
        node.right = grand_child
        # 更新节点高度
        self.update_height(node)
        self.update_height(child)
        # 返回旋转后子树的根节点
        return child

    def rotate(self, node: TreeNode | None) -> TreeNode | None:
        """执行旋转操作，使该子树重新恢复平衡"""
        # 获取节点 node 的平衡因子
        balance_factor = self.balance_factor(node)

        # 左偏树
        if balance_factor > 1:
            if self.balance_factor(node.left) >= 0:
                # 右旋
                return self.right_rotate(node)
            else:
                # 先左旋后右旋
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        # 右偏树
        elif balance_factor < -1:
            if self.balance_factor(node.right) <= 0:
                # 左旋
                return self.left_rotate(node)
            else:
                # 先右旋后左旋
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)
        # 平衡树，无须旋转，直接返回
        return node
    
    def insert(self, val):
        """插入节点"""
        self._root = self.insert_helper(self._root, val)
    
    def insert_helper(self, node: TreeNode | None, val: int) -> TreeNode:
        """递归插入节点（辅助方法）"""
        if node is None:
            return TreeNode(val)
        # 1. 查找插入位置并插入节点
        if val < node.val:
            node.left = self.insert_helper(node.left, val)
        elif val > node.val:
            node.right = self.insert_helper(node.right, val)
        else:
            # 重复节点不插入
            return node
        # 更新节点高度
        self.update_height(node)
        # 2. 执行旋转操作，使该子树重新恢复平衡
        return self.rotate(node)
    
