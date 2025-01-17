class Node:
    def __init__(self, value):
        """ Node class.  This does not need to be modified. """
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        """ Initialize head/tail to none (be sure to update these when approriate). """
        self.head = None  
        self.tail = None 

    def insert_start(self, value):
        """ Inserts a Node with Value to the start of the LinkedList. """
        new_node = Node(value)  # Create a new node with the given value
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        return 

    def insert_end(self, value):
        """ inserts a Node with Value to the end of the LinkedList. """
        new_node = Node(value)  # Create a new node with the given value
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return

    def search_for_node_by_value(self, value):
        """ Searches for a Node with Value in the LinkedList. """
        #initalize value for current node
        curr = self.head
        #iterate through linked list while current node is  not None
        while curr is not None: 
            if curr.value == value:
                return True
            #move to the next node
            curr = curr.next
        return False
        
        return

    def delete_node_by_value(self, value):
        """ Deletes a Node with Value in the LinkedList. 
            If the node does not exist, then does nothing.
        """
        temp = self.head

        #easiest case: if the head node is the node to be deleted by its value
        if (temp is not None):
            if (temp.value == value):
                self.head = temp.next
                if self.head is None:
                    self.tail = None
                temp = None
                return
        
        #iterate through the linked list to find the node to be deleted by its value
        while (temp is not None):
            if temp.value == value:
                break
            #move to the next node
            prev = temp
            temp = temp.next
        
        #if the node to be deleted is not in the linked list, return
        if (temp == None):
            return
        
        #unlink the node from the linked list
        prev.next = temp.next
        if prev.next is None:
            self.tail = prev
        temp = None

    def print_linked_list(self):
        """ Prints the linked list in front to back order. """
        node = self.head
        while node: 
            print(node.value)
            node = node.next
        return