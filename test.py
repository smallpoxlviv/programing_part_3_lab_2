import unittest
from main import *


def get_filled_bst_zero():
	bst = BST(lambda hamster: (hamster.avarice, hamster.daily_norm))
	root = Hamster(1, 3)
	root_left = Hamster(2, 1)
	root_left_right = Hamster(3, 2)
	root_left_left = Hamster(0, 0)
	root_left_left_right = Hamster(0, 1)
	root_left_left_right_right = Hamster(1, 1)
	root_right = Hamster(0, 5)
	root_right_left = Hamster(1, 4)
	root_right_left_left = Hamster(0, 4)
	root_right_left_right = Hamster(2, 4)
	root_right_left_right_same = Hamster(2, 4)
	bst.add(root)
	bst.add(root_left)
	bst.add(root_left_right)
	bst.add(root_left_left)
	bst.add(root_left_left_right)
	bst.add(root_left_left_right_right)
	bst.add(root_right)
	bst.add(root_right_left)
	bst.add(root_right_left_left)
	bst.add(root_right_left_right)
	bst.add(root_right_left_right_same) 
	return bst


class TestBst(unittest.TestCase):

	def setUp(self):
		self.bst = BST(lambda hamster: (hamster.avarice, hamster.daily_norm))
		self.filled_bst_zero = get_filled_bst_zero()

	def test_add_same_node(self):
		node = Hamster(0, 0)
		same_node = Hamster(0, 0)
		self.bst.add(node)
		self.bst.add(same_node)
		self.assertEqual(self.bst.root.quantity, 2)

	def test_add_smaller_node(self):
		root = Hamster(0, 1)
		smaller_node = Hamster(0, 0)
		self.bst.add(root)
		self.bst.add(smaller_node)
		self.assertEqual(self.bst.root.left.data, smaller_node)	

	def test_add_bigger_node(self):
		root = Hamster(0, 0)
		bigger_node = Hamster(0, 1)
		self.bst.add(root)
		self.bst.add(bigger_node)
		self.assertEqual(self.bst.root.right.data, bigger_node)	

	def test_fill_large_bst(self):
		root = Hamster(1, 3)
		root_left = Hamster(2, 1)
		root_left_right = Hamster(3, 2)
		root_left_left = Hamster(0, 0)
		root_left_left_right = Hamster(0, 1)
		root_left_left_right_right = Hamster(1, 1)
		root_right = Hamster(0, 5)
		root_right_left = Hamster(1, 4)
		root_right_left_left = Hamster(0, 4)
		root_right_left_right = Hamster(2, 4)
		root_right_left_right_same = Hamster(2, 4)
		self.bst.add(root)
		self.bst.add(root_left)
		self.bst.add(root_left_right)
		self.bst.add(root_left_left)
		self.bst.add(root_left_left_right)
		self.bst.add(root_left_left_right_right)
		self.bst.add(root_right)
		self.bst.add(root_right_left)
		self.bst.add(root_right_left_left)
		self.bst.add(root_right_left_right)
		self.bst.add(root_right_left_right_same)
		self.assertEqual(self.bst.root.data, root)
		self.assertEqual(self.bst.root.left.data, root_left)
		self.assertEqual(self.bst.root.left.right.data, root_left_right)
		self.assertEqual(self.bst.root.left.left.data, root_left_left)
		self.assertEqual(self.bst.root.left.left.right.data, root_left_left_right)
		self.assertEqual(self.bst.root.left.left.right.right.data, root_left_left_right_right)
		self.assertEqual(self.bst.root.right.data, root_right)
		self.assertEqual(self.bst.root.right.left.data, root_right_left)
		self.assertEqual(self.bst.root.right.left.left.data, root_right_left_left)
		self.assertEqual(self.bst.root.right.left.right.data, root_right_left_right)
		self.assertEqual(self.bst.root.right.left.right.quantity, 2)	

	def test_get_min_element(self):
		min_element = self.filled_bst_zero.get_and_remove_min_element()
		self.assertEqual(min_element.data.avarice, 0)
		self.assertEqual(min_element.data.daily_norm, 0)

	def test_get_min_element_root(self):
		min_assert = Hamster(1, 1)	
		self.bst.add(min_assert)
		self.bst.add(Hamster(1, 2))
		min_element = self.bst.get_and_remove_min_element()
		self.assertEqual(min_element.data, min_assert)
		
	def test_remove_min_element_unique(self):
		self.filled_bst_zero.get_and_remove_min_element()
		new_min_element = self.filled_bst_zero.get_and_remove_min_element()
		self.assertEqual(new_min_element.data.daily_norm, 0)
		self.assertEqual(new_min_element.data.avarice, 1)

	def test_remove_min_element_unique_root(self):
		new_min_element_assert = Hamster(1, 2)
		self.bst.add(Hamster(1, 1))
		self.bst.add(new_min_element_assert)
		self.bst.get_and_remove_min_element()
		new_min_element = self.bst.get_and_remove_min_element().data
		self.assertEqual(new_min_element, new_min_element_assert)
		self.assertEqual(self.bst.root, None)

	def test_remove_min_element_not_unique(self):
		self.filled_bst_zero.add(Hamster(0, 0))
		self.filled_bst_zero.get_and_remove_min_element()
		new_min_element = self.filled_bst_zero.get_and_remove_min_element()
		self.assertEqual(new_min_element.data.daily_norm, 0)
		self.assertEqual(new_min_element.data.avarice, 0)

	def test_remove_min_element_not_unique_root(self):
		self.bst.add(Hamster(1, 1))
		self.bst.add(Hamster(1, 2))
		self.bst.add(Hamster(1, 1))
		self.bst.get_and_remove_min_element()
		new_min_element = self.bst.get_and_remove_min_element().data
		self.assertEqual(new_min_element.daily_norm, 1)
		self.assertEqual(new_min_element.avarice, 1)

	def test_input_data(self):
		stock, hamsters_count, hamster_bst = input_data('io/test/test_in.in')
		self.assertEqual(stock, 25)
		self.assertEqual(hamsters_count, 2)
		self.assertEqual(hamster_bst.root.data.daily_norm, 1)
		self.assertEqual(hamster_bst.root.data.avarice, 3)
		self.assertEqual(hamster_bst.root.left.data.daily_norm, 2)
		self.assertEqual(hamster_bst.root.left.data.avarice, 1)

	def test_output_data(self):
		result = 15
		file_path = 'io/test/test_out.out'
		output_data(file_path, result)
		with open(file_path, 'r') as file:
			assert_result = int(file.readline())
		self.assertEqual(assert_result, result)

	def test_main(self):
		file_in = 'io/in/hamstr_1.in'
		result = main(file_in)
		self.assertEqual(result, 2)
		file_in = 'io/in/hamstr_2.in'
		result = main(file_in)
		self.assertEqual(result, 3)
		file_in = 'io/in/hamstr_3.in'
		result = main(file_in)
		self.assertEqual(result, 1)
		file_in = 'io/test/test_main_1.in'
		result = main(file_in)
		self.assertEqual(result, 4)
		file_in = 'io/test/test_main_2.in'
		result = main(file_in)
		self.assertEqual(result, 4)


if __name__ == "__main__":
	unittest.main()
