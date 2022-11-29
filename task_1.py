class TreeNode:

    def __init__(self, parent, key: int):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent

    @property
    def level(self):

        if self.parent is None:
            return 0
        else:
            return self.parent.level + 1


    def insert(self, node):
        """Inserts a node into the subtree rooted at this node.

        Args:
            node: The node to be inserted.
        """
        if node is None:
            return
        if node.key < self.key:
            if self.left is None:
                node.parent = self
                self.left = node
                #self.level = node.parent.level + 1
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                node.parent = self
                self.right = node
                #self.level = node.parent.level + 1
            else:
                self.right.insert(node)

    def find(self, k):
        """Finds and returns the node with key k from the subtree rooted at this
        node.

        Args:
            k: The key of the node we want to find.

        Returns:
            The node with key k.
        """
        if k == self.key:
            return self
        elif k < self.key:
            if self.left is None:
                return None
            else:
                return self.left.find(k)
        else:
            if self.right is None:
                return None
            else:
                return self.right.find(k)



def add_children(tree, tree_node, level_order, levels):
    par = tree.find(tree_node)
    if par.left is not None:
        level_order.append(par.left.key)
        levels.append(par.left.level)
    if par.right is not None:
        level_order.append(par.right.key)
        levels.append(par.right.level)

def get_level_order_keys_and_levels(preorder_keys: list):
    root = TreeNode(None, preorder_keys[0])
    for i in preorder_keys[1:]:
        root.insert(TreeNode(None, i))

    level_order = [root.key]
    levels = [0]

    for i in range(len(preorder_keys)):
        add_children(root, level_order[i], level_order, levels)

    return level_order, levels


def solution():
    preorder_keys = list(map(int, input().split()))
    level_order_keys, levels = get_level_order_keys_and_levels(preorder_keys)
    print(' '.join(map(str, level_order_keys)))
    print(' '.join(map(str, levels)))


solution()
