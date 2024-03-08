class TreeNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

def build_tree():
    # Construction de l'arbre à partir de l'exemple
    node_g = TreeNode("G")
    node_f = TreeNode("F")
    node_e = TreeNode("E")
    node_d = TreeNode("D")
    node_c = TreeNode("C", [node_f, node_g])
    node_b = TreeNode("B", [node_d, node_e])
    root = TreeNode("A", [node_b, node_c])
    return root

def print_preorder(node):
    if node:
        print(node.value, end=" ")
        for child in node.children:
            print_preorder(child)

if __name__ == "__main__":
    root = build_tree()
    print("Parcours préfixé de l'arbre binaire:")
    print_preorder(root)