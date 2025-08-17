class Node:
    def __init__(self, data):
        self.data = data #The cargo of the node
        self.next = None #This links to next node in chain

# Create Individual Nodes
red = Node('Red')
blue = Node('Blue')
purple = Node('Purple')

# print(red.data) - prints red
# print(red.next) - prints none

# blue -> red -> purple
blue.next = red
red.next = purple

# Starting from blue print red
print(blue.next.data)

# Starting from blue print purple
print(blue.next.next.data)

black = Node("Black")
green = Node("Green")

purple.next = green # Adds green behind purple
green.next = black # Adds black behind green

# Traverse list
print("Traversing the list")
current = blue
while current:
    print(current.data) 
    current = current.next # Move to next node