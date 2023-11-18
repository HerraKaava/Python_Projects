

class TreeNode:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    # The logic inside the insert() method is simple;
    # If the input value is
    def insert(self, value):
        """
        Inserts the input value into the correct position.
        If the input value is less than the value of the current node (self.value),
        the input value will be inserted to the left subtree,
        otherwise it will be inserted to the right subtree.

        If there is no left or right child,
        a new TreeNode is created with the given value and assigned as the left or right child accordingly.

        Note that if the input value will be inserted to e.g. left, and there is a value present already,
        the same function will be recursively applied to the node again.
        """
        if value < self.value:
            if self.left is None:    # If there is no left child, create one from the input value.
                self.left = TreeNode(value)
            else:   # If a node is already present, recursively call the insert() function onto that node.
                self.left.insert(value)
        else:   # If the input value is not less than the current node, we enter the right subtree.
            if self.right is None:    # If there is no right child, create one from the input value.
                self.right = TreeNode(value)
            else:    # If a node is already present, recursively call the insert() function onto that node.
                self.right.insert(value)

    # For the tree traversal, three different ways (which are essentially the same method implemented differently),
    # will be implemented.
    # The three methods include:
        # 1. Inorder traversal
        # 2. Preorder traversal
        # 3. Postorder traversal
    # These methods have different use cases; Preorder traversal and Postorder traversal are typically used
    # with prefix and postfix, respectively, and Inorder traversal is typically used in binary search tree.
    # The main difference is the order in which the nodes are visited and printed.
    # Below is an implementation of how each method prints a simple binary tree.

    # Creating the binary tree
    #       A
    #      / \
    #     B   C

    # Preorder traversal:   A, B, C
    # Inorder traversal:    B, A, C
    # Postorder traversal:  B, C, A

    def inorder_traversal(self):
        """
        An inorder traversal first visits the left child (including its entire subtree),
        then visits the node, and finally visits the right child (including its entire subtree).
        In inoder traversal, the order of operations is: left subtree --> node --> right subtree.

        Returns:
            None

        Prints:
            The values of the entire tree in ascending order.
        """
        # If the left node exists, we enter the left subtree.
        if self.left:
            # Recursively call the inorder_traversal() function on the left child.
            # This recursive call starts the inorder traversal on the left subtree.
            # The recursion continues until it reaches a node WITHOUT a left child (a leaf),
            # at which point it prints the value of that node.
            # Essentially we are going as left as possible until we find a leaf, and print that leaf.
            self.left.inorder_traversal()
        print(self.value)

        # The same operations will be conducted to the right subtree (if it exists).
        if self.right:
            self.right.inorder_traversal()
        # Note that it's not necessary to call print(self.value) here.
        # If one were to call print(self.value) here, it would result in duplicate prints,
        # because the value of the current node has already been printed before checking the right subtree.


    def preorder_traversal(self):
        """
        A preorder traversal first visits the node, then the left subtree, and finally the right subtree.
        In preorder traversal, the order of operations is: node --> left subtree --> right subtree.

        Returns:
            None

        Prints:
            The values of the entire tree.
            Note that the values not printed in ascending or descending order.
        """
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()


    def postorder_traversal(self):
        """
        A postorder traversal first visits the left subtree, then the right subtree, and finally the root.
        In postorder traversal, the order of oprations is: left subtree --> right subtree --> node.

        Returns:
            None

        Prints:
            The values of the entire tree.
        """
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value)


    def find(self, value):
        """
        Search for a specific value in the binary tree.

        Parameters:
            value: The value to be searched for in the tree.

        Returns:
            True if the value is found in the tree.
            False if the value is not found in the tree.
        """
        # If the value one is looking for is less than the current node (self.node) (and it exists),
        # It has to be located in the left subtree.
        if value < self.value:
            # If the value on the left is None (i.e. there is no left subtree),
            # the value one is looking for is not included in the tree.
            if self.left is None:
                return False
            else:
                # If there is node on the left, a recursive call will be used.
                return self.left.find(value)
        # If value > self.value --> right subtree
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        # If value == self.value (the current node) --> return True
        else:
            return True


if __name__ == "__main__":
    tree = TreeNode(6)
    tree.insert(5)
    tree.insert(2)
    tree.insert(4)
    tree.insert(1)
    tree.insert(2)
    tree.insert(4)
    tree.insert(5)
    tree.insert(19)
    tree.insert(19)
    tree.insert(29)
    tree.insert(11)
    tree.insert(4)
    tree.insert(2)

    tree.preorder_traversal()
    print()
    tree.inorder_traversal()
    print()
    tree.postorder_traversal()

    print(tree.find(29))    # True, because 29 is in the tree.
    print(tree.find(7))     # False, because 7 is not in the tree.







