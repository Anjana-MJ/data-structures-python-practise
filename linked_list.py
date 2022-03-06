class Node:
	"""
	Represents individual element in the linked list.
	nxt is a pointer to the next element in the linked list
	"""
	def __init__(self, data=None, nxt=None):
		self.data = data
		self.next = nxt


class LinkedList:
	def __init__(self):
		# head variable is a variable which points to the head of the linked list
		self.head = None

	def insert_at_beginning(self, data):
		node = Node(data, self.head)
		self.head = node

	def insert_at_end(self, data):
		if self.head is None:
			self.head = Node(data, None)
			return
		itr = self.head
		while itr.next:
			itr = itr.next
		itr.next = Node(data, None)

	def insert_values(self, data_list):
		self.head = None
		for data in data_list:
			self.insert_at_end(data)

	def get_length(self):
		count = 0
		itr = self.head
		while itr:
			count +=1
			itr = itr.next
		return count

	def remove_at(self, index):
		if index < 0 or index >= self.get_length():
			raise Exception("Invalid index value")
		if index == 0:
			self.head = self.head.next
		itr = self.head
		count = 0
		while itr:
			if count == index - 1:
				itr.next = itr.next.next
				break
			itr = itr.next
			count += 1

	def insert_at(self, index, data):
		if index <0 or index > self.get_length():
			raise Exception("Invalid index value")
		if index == 0:
			self.insert_at_beginning(data)
		itr = self.head
		count = 0
		while itr:
			if count == index - 1:
				node = Node(data, itr.next)
				itr.next = node
				break
			itr = itr.next
			count += 1

	def print_linked_list(self):
		if self.head is None:
			print("Linked list is empty!!!!")
			return
		itr = self.head
		ll_str = ''
		while itr:
			ll_str += str(itr.data) + '----->'
			itr = itr.next
		print(ll_str)


if __name__ == '__main__':
	llist = LinkedList()
	llist.insert_values(["apple", "banana", "cherry", "raspberry", "blueberry"])
	llist.print_linked_list()
	llist.remove_at(3)
	llist.print_linked_list()
	llist.insert_at(0, 'fig')
	llist.print_linked_list()
	llist.insert_at(3, 'kivi')
	llist.print_linked_list()

	llist.insert_values([18,12,23,84,26,17])
	llist.print_linked_list()
	llist.remove_at(4)
	llist.print_linked_list()
