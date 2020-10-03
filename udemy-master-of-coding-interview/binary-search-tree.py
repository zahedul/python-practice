import pprint
from node import Node


class BinarySearchTree:

    def __init__(self):
        self.root = None;

    def insert(self, value):
        new_node = Node(value)

        if self.root == None:
            self.root = new_node

        else:
            current_node = self.root

            while True:
                # print(f'value: {value}: {current_node}')
                # pretty_print({current_node})
                try:
                    if value < current_node.value: #left
                        if current_node.left is None:
                            current_node.left = new_node

                            break
                        current_node = current_node.left
                    else: #right
                        if current_node.right is None:
                            current_node.right = new_node
                            break
                        
                        current_node = current_node.right

                except Exception as e:
                    print('Exception: ', e);
                    break

    def lookup(self, value):
        if self.root is None:
            return False
        
        current_node = self.root

        while current_node:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            elif value == current_node.value:
                return current_node
            else:
                return False

    def remove(self, value):
        if self.root is None:
            return False
        
        current_node = self.root
        parent_node = None

        while current_node:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            elif current_node.value == value:
                if current_node.right == None:
                    if parent_node == None:
                        self.root = current_node.left
                    else:
                        if current_node.value > parent_node.valuee:
                            parent_node.left = current_node.left
                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.left
                elif current_node.right.left == None:
                    current_node.right.left = current_node.left
                    if parent_node == None:
                        self.root = current_node.right
                    else:
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.right
                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.right
                else:
                    left_most = current_node.right.left
                    left_most_parent = current_node.right
                    while left_most.left == None:
                        left_most_parent = left_most
                        left_most = left_most.left
                    
                    left_most_parent.left = left_most.right
                    left_most.left = current_node.left
                    left_most.right = current_node.right

                    if parent_node == None:
                        self.root = left_most
                    else:
                        if current_node.value < parent_node.value:
                            parent_node.left = left_most
                        elif current_node.value > parent_node.value:
                            parent_node.right = left_most
            return True


def pretty_print(clas, indent=0):
    print(' ' * indent +  type(clas).__name__ +  ':')
    indent += 4
    for k,v in clas.__dict__.items():
        if '__dict__' in dir(v):
            pretty_print(v,indent)
        else:
            print(' ' * indent +  k + ': ' + str(v))

def main():
    tree = BinarySearchTree()
    tree.insert(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)
    tree.remove(170)
    
    pretty_print(tree)

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()