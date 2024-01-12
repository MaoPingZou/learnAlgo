# 二叉搜索树

"""
「二叉搜索树 binary search tree」 满足以下条件：
1、对于根节点，左子树中所有节点的值 < 根节点的值 < 右子树中所有节点的值
2、任意节点的左、右子树也是二叉搜索树，即同样满足条件 1 
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from tree_node import TreeNode, print_tree

class BinarySearchTree:
    """二叉搜索树"""

    def __init__(self):
        """构造方法"""
        # 初始化空树
        self._root = None
    
    def get_root(self) -> TreeNode | None:
        """获取二叉树根节点"""
        return self._root

    def search(self, num: int) -> TreeNode | None:
        """查找节点"""
        cur = self._root
        # 循环查找，越过叶节点后跳出
        while cur is not None:
            # 目标节点在 cur 的右子树中
            if cur.val < num:
                cur = cur.right
            elif cur.val > num:
                cur = cur.left
            # 找到目标节点
            else:
                break
        return cur
    
    def insert(self, num: int):
        """插入一个节点"""
        # 若树为空，则初始化根节点
        if self._root is None:
            self._root = TreeNode(num)
            return
        # 循环查找，越过根节点后跳出
        cur, pre = self._root, None
        while cur is not None:
            # 找到重复节点，直接返回
            if cur.val == num:
                return
            # 将当前值作为下一次遍历的前一个值
            pre = cur
            if cur.val < num:
                # 如果插入的值大于当前节点值，遍历 cur 的右子树进行插入
                cur = cur.right
            else:
                # 否则，遍历 cur 的左子树中进行插入
                cur = cur.left
        # 插入节点
        node = TreeNode(num)
        if pre.val < num:
            pre.right = node
        else:
            pre.left = node
                
    def remove(self, num: int):
        """移除节点"""
        # 若树为空，直接返回
        if self._root is None:
            return
        # 循环查找，越过叶子节点后直接跳出
        cur = self._root
        pre = None
        while cur is not None:
            # 找到待删除节点，跳出循环
            if cur.val == num:
                break
            # 将当前值作为下一个循环的前一个值
            pre = cur
            if cur.val < num:
                # 待删除节点在当前节点的右子树上
                cur = cur.right
            else:
                # 待删除节点在当前节点的左子树上
                cur = cur.left
        # 如果没有待删除节点，直接返回
        if cur is None:
            return
        
        # 子节点数量 = 0 or 1
        if cur.left is None or cur.right is None:
            # 当子节点的数量为 0 或 1 时，child = null / 该子节点
            child = cur.left or cur.right
            # 删除节点
            if cur != self._root:
                if pre.left == cur:
                    pre.left = child
                else:
                    pre.right = child
            else:
                # 若删除节点为根节点，则重新指定根节点
                self._root = child
        # 子节点数量为 2
        else:
            # 获取中序遍历中 cur 的下一个节点
            temp: TreeNode = cur.right
            # 循环遍历当前节点右子节点形成的子树的左节点
            while temp.left is not None:
                temp = temp.left
            # 递归删除节点 temp
            self.remove(temp.val)
            # 用 temp 的值覆盖 cur 的值
            cur.val = temp.val
            
            
"""测试代码"""
if __name__ == "__main__":
    # 初始化二叉搜索树
    bst = BinarySearchTree()
    nums = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    # 该序列会生成一个完美二叉树
    for num in nums:
        bst.insert(num)
    print("\n初始化的二叉树为\n")
    print_tree(bst.get_root())

    # 查找节点
    node = bst.search(7)
    print("\n查找到的节点对象为：{}，节点值 = {}".format(node, node.val))

    # 插入节点
    bst.insert(16)
    print("\n插入节点 16 后， 二叉树为：\n")
    print_tree(bst.get_root())

    # 删除节点
    # 0 个子节点
    bst.remove(1)
    print("\n删除节点 1 后，二叉树为：\n")
    print_tree(bst.get_root())

    # 1 个子节点
    bst.remove(2)
    print("\n删除节点 2 后，二叉树为：\n")
    print_tree(bst.get_root())

    # 2 个子节点
    bst.remove(4)
    print("\n删除节点 4 后，二叉树为\n")
    print_tree(bst.get_root())
