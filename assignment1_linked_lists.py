class Node:
    def __init__(self, data):
        self.data = data    # Store the actual data
        self.next = None    # Pointer to next node
    
    def __str__(self):
        return f"Node({self.data})"

class LinkedList:
    def __init__(self):
        self.head = None    # First node in the list
        self.size = 0       # Number of nodes
    
    def is_empty(self):
        """Check if the list is empty"""
        return self.head is None
    

    
    def append(self, data):
        """Add element to end - ALREADY IMPLEMENTED"""
        new_node = Node(data)   # Create new node
        self.size += 1          # Update count
        
        # Special case: empty list
        if self.head is None:
            self.head = new_node
            return
        
        # Find the last node
        current = self.head
        while current.next:     # Traverse to end
            current = current.next
        current.next = new_node # Link new node
    
    def prepend(self, data):
        """Add element to beginning - ALREADY IMPLEMENTED"""
        new_node = Node(data)       # Create new node
        new_node.next = self.head   # Point to current head
        self.head = new_node        # Update head
        self.size += 1              # Update count
    
    # YOUR IMPLEMENTATIONS START HERE
    
    def get_at_position(self, position):
        """
        Get the data at a specific position (0-indexed)
        
        Args:
            position: Index to retrieve from (0 = first element)
        
        Returns:
            The data at that position
        
        Raises:
            ValueError: If position is out of range
        
        Example:
            ll = LinkedList()
            ll.append("A")
            ll.append("B") 
            ll.get_at_position(1)  # Returns "B"
        """
        current = self.head
        counter = 0
        while counter < position:
            current = current.next
            counter += 1

        return current.data

        # ToDo: Implement this method
        # Steps:
        # 1. Check if position is valid (0 <= position < size)
        # 2. Traverse the list 'position' number of times
        # 3. Return the data at that node
    
    def delete_at_position(self, position):
        """
        Delete the node at a specific position (0-indexed)
        
        Args:
            position: Index to delete from (0 = first element)
        
        Raises:
            ValueError: If position is out of range or list is empty
        
        Example:
            ll = LinkedList()
            ll.append("A")
            ll.append("B")
            ll.append("C")
            ll.delete_at_position(1)  # Removes "B", list becomes A -> C
        """
        current = self.head
        counter = 0
        # Move to node just infront of the node we want to remove
        while counter < position - 1:
            current = current.next
            counter += 1

        # Set the current node's next to the node behind the node we want to remove
        removing = current.next
        current.next = current.next.next
        return removing

        # ToDo: Implement this method
        # Steps:
        # 1. Check if list is empty
        # 2. Check if position is valid
        # 3. Handle special case: deleting head (position 0)
        # 4. Find the node before the one to delete
        # 5. Update pointers to skip the deleted node
        # 6. Update size
        pass
    


# Test your implementation
def test_basic_linked_list():
    """Test function to verify your LinkedList methods work correctly"""
    print("🧪 Testing Basic LinkedList Implementation...")
    
    # Create and populate list
    ll = LinkedList()
    
    # Build initial list: 0 -> 1 -> 2 -> 3
    ll.append(1)    # List: 1
    ll.append(2)    # List: 1 -> 2
    ll.append(3)    # List: 1 -> 2 -> 3
    ll.prepend(0)   # List: 0 -> 1 -> 2 -> 3
    
    print("List created and populated successfully")
    
    # Test get_at_position
    print("\n--- Testing get_at_position ---")
    try:
        for i in range(4):  # We know we added 4 items
            value = ll.get_at_position(i)
            print(f"Position {i}: {value}")
    except Exception as e:
        print(f"Error in get_at_position: {e}")
    
    # Test delete_at_position
    print("\n--- Testing delete_at_position ---")
    try:
        ll.delete_at_position(1)  # Remove element at position 1
        print("Position 1 deleted successfully")
    except Exception as e:
        print(f"Error in delete_at_position: {e}")
    
    print("\n Test completed!")

# Uncomment to test your implementation
test_basic_linked_list()