class BST:

    class Node:
        def __init__(self, key, data, parent = None):
            self.quantity = 1
            self.key = key
            self.data = data
            self.parent = parent
            self.left = None
            self.right = None

    def __init__(self, lambda_key):
            self.lambda_key = lambda_key
            self.root = None;

    def add(self, data):
        if self.root is None:
            self.root = self.Node(self.lambda_key(data), data)
            return

        new_key = self.lambda_key(data)
        current = self.root
        while True:
            if current.key < new_key:
                if current.right is None:
                    current.right = self.Node(new_key, data, current)
                    break
                else:
                    current = current.right
            elif current.key > new_key:
                if current.left is None:
                    current.left = self.Node(new_key, data, current)
                    break
                else:
                    current = current.left
            else:
                current.quantity += 1
                break

    def get_and_remove_min_element(self):
        current = self.root
        while True:
            if current.left is None:
                min_element = current
                break
            current = current.left

        if min_element.quantity == 1:
            if min_element.right is not None:
                if min_element == self.root:
                    min_element.right.parent = None
                    self.root = min_element.right
                    min_element.right = None
                else:
                    min_element.parent.left = min_element.right
                    min_element.right.parent = min_element.parent
            else:
                if min_element == self.root:
                    self.root = None
                else:
                    min_element.parent.left = None
                    min_element.parent = None
        else:
            min_element.quantity -= 1

        return min_element
        