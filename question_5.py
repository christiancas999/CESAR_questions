# When different email clients are used on a same thread, the discussion 
# get messy because old messages are included again and get duplicated. 
# Given a email thread (represented by a singly unsorted linked list of messages), 
# write a function that remove duplicated messages from it.  

class Node:  
  
    def __init__(self, data):  
        self.data = data  
        self.next = None
  
class LinkedList:  
     
    def __init__(self):
        """Function to initialize head."""
        self.head = None
      
    def addNode(self, new_data):
        """Function to add a new node and sort the nodes."""
        curr = self.head

        # Add new Node
        if curr is None:
            n = Node(new_data)            
            self.head = n
            return
            
        # Sort Nodes          
        if curr.data > new_data:
            n = Node(new_data)            
            n.next = curr
            self.head = n
            return

        while curr.next is not None:
            if curr.next.data > new_data:
                break
            curr = curr.next
        n = Node(new_data)        
        n.next = curr.next
        curr.next = n
        return

    def printList(self):
        """Function to print the LinkedList."""  
        aux = self.head  
        while(aux):  
            print(aux.data , end = ' ') 
            aux = aux.next
                
    def removeDuplicates(self):
        """Function to remove duplicate LinkedList.""" 
        aux = self.head 
        if aux is None: 
            return
        while aux.next is not None: 
            #Compare head node with next node
            if aux.data == aux.next.data: 
                new = aux.next.next
                aux.next = new 
            else: 
                aux = aux.next
        return self.head 
  
  

messages = LinkedList()  

# Example A
  
#messages.addNode(21)  
#messages.addNode(18)  
#messages.addNode(12) 
#messages.addNode(12) 
#messages.addNode(21)
#messages.addNode(18) 
#messages.addNode(18)

# Example B

messages.addNode("A")  
messages.addNode("A")  
messages.addNode("J") 
messages.addNode("A") 
messages.addNode("C")
messages.addNode("C")
messages.addNode("A")

print ("Linked List of messages: ") 
messages.printList()  
print("\nLinked List without duplicate messages:") 
messages.removeDuplicates() 
messages.printList()

"""
The algorithm complexity is O(n), because it looks for a duplicate Node in the next position to remove it. 
This check is performed in entire list.
The space complexity of this algorithm depends of messages size and amount of messaged duplicated.
"""
 