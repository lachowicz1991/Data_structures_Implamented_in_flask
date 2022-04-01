class Node:
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node


class LinkedList:
	def __init__(self):
		self.head = None
		self.last_node = None

	def print_linked_list(self):
		linked_list_string = ""
		node = self.head
		if node is None:
			print(None)
		while node:
			linked_list_string += f"{str(node.data)} -> "
			node = node.next_node

		linked_list_string += "None"

		return linked_list_string

	def insert_at_beginning(self, data):
		if self.head is None:
			self.head = Node(data, None)
			self.last_node = self.head

		new_node = Node(data, self.head)
		self.head = new_node

	def insert_at_end(self, data):
		if self.head is None:
			self.insert_at_beginning(data)

		else:
			self.last_node.next_node = Node(data, None)
			self.last_node = self.last_node.next_node

	def to_array(self):
		arr = []
		if self.head is None:
			return arr
		node = self.head
		while node:
			arr.append(node.data)
			node = node.next_node

		return arr

	def get_user_by_id(self, user_id):
		node = self.head
		while node:
			if node.data['id'] is int(user_id):
				return node.data
			node = node.next_node
		return None

