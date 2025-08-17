class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None # Keeps track of first node

    def is_empty(self):
        """Check if we have any nodes"""
        return self.head is None
    
    # Adding/Appending Nodes to end of list
    def append(self, data):
        new_node = Node(data)

        if self.is_empty(): # Checks if list is empty 
            self.head = new_node # If list is empty new_node is set as head node 
            return # This breaks out of function

        current = self.head # Starts at the beginning of chain/list
        while current.next: # Checking if there is a next node
            current = current.next # If there is, then move over to next node

        # Once the while loop finishes current should be a new node at the end
        current.next = new_node

    def traverse(self):
        print("===== List Contents =====")
        if self.is_empty():
            return "List is empty"
        
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def insert_at_postition(self, position, data): # NEED TO UPDATE
        """Adding a node at a position (0-index)"""
        new_node = Node(data) #Creates new node

        current = self.head
        counter = 0
        while counter < position - 1:
            current = current.next
            counter += 1

            new_node.next = current.next

songs = LinkedList()
print(songs.is_empty()) # Will return True

songs.append("Jump")
songs.append("Empty")
songs.append("Maze")
songs.append("Blind Eyes Red")
songs.append("Freak")

songs.traverse()

songs.insert_at_postition(2, "Communication")

songs.traverse()
print(songs.get_at_position(4))

