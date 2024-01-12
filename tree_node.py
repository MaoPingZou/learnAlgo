class TreeNode:
    """二叉树节点类"""

    def __init__(self, val: int = 0):
        self.val: int = val  # 节点值
        self.height: int = 0  # 节点高度
        self.left: TreeNode | None = None  # 左子节点引用
        self.right: TreeNode | None = None  # 右子节点引用

class Trunk:
    def __init__(self, prev, string: str | None = None):
        self.prev = prev
        self.str = string

def show_trunks(p: Trunk | None):
    if p is None:
        return
    show_trunks(p.prev)
    print(p.str, end="")

def print_tree(
    root: TreeNode | None, prev: Trunk | None = None, is_right: bool = False
):
    """
    打印二叉树
    This tree printer is borrowed from TECHIE DELIGHT
    https://www.techiedelight.com/c-program-print-binary-tree/
    """
    if root is None:
        return

    prev_str = "    "
    trunk = Trunk(prev, prev_str)
    print_tree(root.right, trunk, True)

    if prev is None:
        trunk.str = "———"
    elif is_right:
        trunk.str = "/———"
        prev_str = "   |"
    else:
        trunk.str = "\———"
        prev.str = prev_str

    show_trunks(trunk)
    print(" " + str(root.val))
    if prev:
        prev.str = prev_str
    trunk.str = "   |"
    print_tree(root.left, trunk, False)