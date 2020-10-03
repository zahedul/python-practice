from node import Node


class BinarySearchTree:
    
    def __init__(self):
        self.root = null;
    
    def insert(self, value):
        new_node = Node(value)

        if self.root == null:
            self.root = new_node
        else:
            current_node = self.root

            while True:
                if value < current_node.value: #left
                    if not current_node.left:
                        current_node.left = new_node
                        return self
                    current_node = current_node.left
                else: #right
                    if current_node.right:
                        current_node.right = new_node
                        return self
                    
                    current_node = current_node.right

        

    def lookup(self, value):
        pass

def main():
    pass

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()