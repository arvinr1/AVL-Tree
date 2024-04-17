
import unittest
from AVL-Tree import Binary_Search_Tree

class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.tree = Binary_Search_Tree()

    # Tree Creation and Basic Insertion
    def test_empty_tree(self):
        self.assertEqual(str(self.tree), '[ ]')

    def test_insert_single(self):
        self.tree.insert_element(10)
        self.assertEqual(str(self.tree), '[ 10 ]')

    def test_insert_multiple(self):
        for value in [10, 5, 15]:
            self.tree.insert_element(value)
        self.assertEqual(str(self.tree), '[ 5, 10, 15 ]')

    # Tree Traversal
    def test_in_order_traversal(self):
        for value in [10, 5, 15]:
            self.tree.insert_element(value)
        self.assertEqual(self.tree.in_order(), '[ 5, 10, 15 ]')

    def test_pre_order_traversal(self):
        for value in [10, 5, 15]:
            self.tree.insert_element(value)
        self.assertEqual(self.tree.pre_order(), '[ 10, 5, 15 ]')

    def test_post_order_traversal(self):
        for value in [10, 5, 15]:
            self.tree.insert_element(value)
        self.assertEqual(self.tree.post_order(), '[ 5, 15, 10 ]')

    def test_remove_one_child(self):
        for value in [20, 10, 30, 5]:
            self.tree.insert_element(value)
        self.tree.remove_element(30)
        self.assertEqual(str(self.tree), '[ 5, 10, 20 ]')

    def test_remove_two_children(self):
        for value in [20, 10, 30, 5, 25, 35]:
            self.tree.insert_element(value)
        self.tree.remove_element(30)  
        self.assertEqual(str(self.tree), '[ 5, 10, 20, 25, 35 ]')

    def test_balancing_after_removal(self):
        for value in [20, 10, 30, 5, 25, 35, 15]:
            self.tree.insert_element(value)
        self.tree.remove_element(35) 
        self.assertEqual(str(self.tree), '[ 5, 10, 15, 20, 25, 30 ]') 

    # Deletion and Balancing
    def test_remove_leaf(self):
        for value in [10, 5, 15]:
            self.tree.insert_element(value)
        self.tree.remove_element(5)
        self.assertEqual(str(self.tree), '[ 10, 15 ]')

    # Error Handling
    def test_insert_duplicate(self):
        self.tree.insert_element(10)
        with self.assertRaises(ValueError):
            self.tree.insert_element(10)

    def test_remove_nonexistent(self):
        with self.assertRaises(ValueError):
            self.tree.remove_element(10)

    # Tree Height
    def test_tree_height(self):
        for value in [10, 5, 15]:
            self.tree.insert_element(value)
        self.assertEqual(self.tree.get_height(), 2)

    # Conversion to List
    def test_to_list(self):
        for value in [10, 5, 15]:
            self.tree.insert_element(value)
        self.assertEqual(self.tree.to_list(), [5, 10, 15])

if __name__ == '__main__':
    unittest.main()
