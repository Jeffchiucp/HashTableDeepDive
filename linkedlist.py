#!python

#from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        self.nodeCount = 0
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(repr(self.items()))

    def items(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

        
    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        # Node counter initialized to zero
        node_count = 0
        # Start at the head node
        current = self.head
        # Loop until the current node is None, which is one node past the tail
        while current is not None:
            # Count one for this node
            node_count += 1
            # Skip to the next node
            current = current.next
        # Now node_count contains the number of nodes
        return node_count
        
    def length(self):
        """Alternative way to return the length of the linked list"""
        return self.nodeCount

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        new_node = Node(item)
        self.nodeCount += 1
        # Check if this linked list is empty
        if self.tail == None and self.head == None:
            self.tail = new_node
            self.head = new_node
        elif self.tail == self.head:
            self.tail = new_node
            self.head.next = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if the linked list is None when head and tail is none
        # Update head to new node 
        if self.head == None and self.tail == None:
            self.tail = new_node
            self.head = new_node
        elif self.head == self.tail:  
            self.head = new_node
            self.head.next = self.tail
        else:
           # Otherwise insert new node before head
        # Update head to new node regardless
            new_node.next = self.head
            self.head = new_node

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        """Best case running time: Omega(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        current = self.head
        previous = None
        while current is not None:
            if current.data == item:
                if current is not self.head and current is not self.tail:
                    previous.next = current.next
                    current.next = None
                    break
                if current is self.head:
                    self.head = current.next
                    current.next = None
                if current is self.tail:
                    if previous is not None:
                        previous.next = None
                    self.tail = previous
                return
            previous = current
            current = current.next
        raise ValueError('Item not found: {}'.format(item))


    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: Omega(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        current = self.head  # Constant time to assign a variable reference
        # Loop until the current node is None, which is one node past the tail
        while current is not None:  # Up to n iterations if we don't exit early
            # Check if the current node's data satisfyies the quality function
            if quality(current.data):  # Constant time to call quality function
                # We found data satisfying the quality function, so exit early
                return current.data  # Constant time to return data
            # Skip to the next node
            current = current.next  # Constant time to reassign a variable
        # We never found data satisfying quality, but have to return something
        return None  # Constant time to return None

    def replace(self, quality, new_data):
        """replace an item from this linked list satisfying the given quality"""
        current = self.head

        while current is not None:
            if quality(current.data):
                return
            current = current.next
        self.append(new_data)


    def replace(self, item, new_item):
        """replace an item with new_item by using the helper function finding the item"""
        node = self.find_node(item)
        node.data = new_item

    def find_node(self, item):
        """Returns the first node it encounters where data is equal to item"""
        current_node = self.head
        while current_node is not None:
            if current_node.data == item:
                return current_node
            current_node = current_node.next

def test_linked_list():
    ll = LinkedList()
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())

    # import pdb; pdb.set_trace()
    ll.delete('A')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('B')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())

    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    import pdb; pdb.set_trace()

    ll.find_node('A')
    print("___________________")
    ll.replace('B', 'A')
    ll.replace('A', 'M')
    print(ll)

if __name__ == '__main__':
    test_linked_list()