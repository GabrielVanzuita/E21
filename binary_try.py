class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left_child = left
        self.right_child = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def binary_search(self, search_value):
        current_node = self.root
        while current_node:
            if search_value == current_node.data:
                return True
            elif search_value < current_node.data:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        return False

    def insert(self, data):
        new_node = TreeNode(data)
        # Se a árvore estiver vazia, define a raiz
        if self.root is None:
            self.root = new_node
            return

        current_node = self.root
        while True:
            if data < current_node.data:
                # Vai para a esquerda
                if current_node.left_child is None:
                    current_node.left_child = new_node
                    return
                else:
                    current_node = current_node.left_child
            elif data > current_node.data:
                # Vai para a direita
                if current_node.right_child is None:
                    current_node.right_child = new_node
                    return
                else:
                    current_node = current_node.right_child
            else:
                # Opcional: lidar com duplicatas conforme sua política (aqui, ignora)
                return
