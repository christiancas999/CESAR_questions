# If two requests on the queue have linked lists that intersect (like the example below),
# previous service could be improved to process only the difference between them.
# Write a method that receives two singly linked lists and return the intersecting node
# of the two lists (if exists). Note that the intersection is defined by reference, not value.
# (No need to change previous answer).

class Node:  
  
    def __init__(self, data):  
        self.data = data  
        self.next = None
  
class LinkedList:  
     
    def __init__(self):
        """Function to initialize head."""
        self.head = None
  
    def addNode(self, new_data):
        """Function to add a new node."""  
        new_node = Node(new_data)  
        new_node.next = self.head  
        self.head = new_node              
       
    def getCount(self):
        """Function to count the nodes from a linked list."""
        aux = self.head
        count = 0
        while aux is not None:
            count = count + 1
            aux = aux.next            
        return count

    def getDiff(self, count1, count2):
        """Function to get the difference between 2 linked lists"""
        if count1 > count2:
            diff = count1 - count2
            return diff
        else:
            diff = count2 - count1
            return diff

    def getIntersectionNode(self, diff, data1, data2):
        """Function to get the intersection Node"""
        for i in range (diff):                
                if data1 is None:
                    return -1
                data1 = data1.next                       
        while data1 is not None and data2 is not None:
            if data1.data == data2.data:
                return data1.data                
            data1 = data1.next
            data2 = data2.next
        return -1

  
messages = LinkedList()  
messages2 = LinkedList()  

messages.addNode("A")  
messages.addNode("B")  
messages.addNode("J") 
messages.addNode("H") 
messages.addNode("E")
messages.addNode("A")
messages.addNode("C")

messages2.addNode("A") 
messages2.addNode("B")
messages2.addNode("J")
messages2.addNode("F")
messages2.addNode("D")

n1 = messages.getCount()
n2 = messages2.getCount()

difference = messages.getDiff(n1, n2)
head1 = messages.head
head2 = messages2.head

node = messages.getIntersectionNode(difference, head1, head2)
if node != -1:
    print (f"Intersecting node: {node}")
else:
    print (f"There is not intersecting node")
  
 
"""
The algorithm complexity is O(m+n), because it is possible traverse both the lists in parallel to find the common Node.
The space complexity of this algorithm depends on the size of each list.
"""