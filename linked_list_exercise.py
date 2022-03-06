class Node:
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.next = nxt


class LinkedList:
    def __init__(self):
        self.head = None

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index value")
        if index == 0:
            self.head = Node(data, self.head)
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

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
            count +=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def print_linked_list(self):
        if self.head is None:
            print("Linked list is empty!!!")
            return
        itr = self.head
        ll_str = ''
        while itr:
            ll_str += str(itr.data) + "------->"
            itr = itr.next
        print(ll_str)

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurrence of data_after value in linked list
        # Now insert data_to_insert after data_after node
        itr = self.head
        count = 0
        while itr:
            if itr.data == data_after:
                self.insert_at(count+1, data_to_insert)
                break
            itr = itr.next
            count += 1

    def remove_by_value(self, data):
        # Remove first node that contains data
        itr = self.head
        count = 0
        while itr:
            if itr.data == data:
                self.remove_at(count)
            itr = itr.next
            count += 1


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_values(["banana","mango","grapes","orange"])
    linked_list.print_linked_list()
    linked_list.insert_after_value("mango","apple") # insert apple after mango
    linked_list.print_linked_list()
    linked_list.insert_after_value("grapes", "fig")  # insert fig after grapes
    linked_list.print_linked_list()

    linked_list.remove_by_value("orange") # remove orange from linked list
    linked_list.print_linked_list()
    linked_list.remove_by_value("fig")
    linked_list.print_linked_list()
    linked_list.remove_by_value("banana")
    linked_list.remove_by_value("mango")
    linked_list.remove_by_value("apple")
    linked_list.remove_by_value("grapes")
    linked_list.print_linked_list()