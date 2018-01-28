# Each node in the linked list
class Node(object):
	
	#constructor	
	def __init__(self, data):
		self.data = data;
		self.nextNode = None; 


# Linked list
class LinkedList(object):
	
	#constructor	
	def __init__(self):
		self.head = None;
		self.size = 0;
		
	
	# O(1)
	def insertStart(self,data):
	
		self.size = self.size + 1;
		newNode = Node(data);

		if not self.head:
			self.head = newNode;
		else:
			newNode.nextNode = self.head;
			self.head = newNode;
	
	# O(1)		
	def size1(self):
		
		return self.size;
	
	# O(N) so that's why we stored size from the start itself
	def size2(self):
		
		actualNode = self.head;
		size = 0;
		
		while actualNode is not None:
			size += 1;
			actualNode = actualNode.nextNode;
			
		return size;
		
	# O(N)
	def insertEnd(self,data):
		
		self.size = self.size + 1;
		newNode = Node(data);
		actualNode = self.head;
		
		while actualNode.nextNode is not None:
			actualNode = actualNode.nextNode;
			
		actualNode.nextNode = newNode;	
		
	def remove(self, data):
		
		if self.head is None:
			return;
		
		self.size = self.size - 1;
		currentNode = self.head;
		previousNode = None; 
		
		while currentNode.data is not data:
			previousNode = currentNode;
			currentNode = currentNode.nextNode;
			
		# if people are trying to remove the head		
		if previousNode is None:
			self.head = currentNode.nextNode
		else:
		 	previousNode.nextNode = currentNode.nextNode;
	
	def traverseList(self):
		
		actualNode = self.head;
		
		while actualNode is not None:			
			print("%d" % actualNode.data);
			actualNode = actualNode.nextNode;


linkedList = LinkedList();

linkedList.insertStart(12);
linkedList.insertStart(13);
linkedList.insertStart(14);
linkedList.insertStart(15);
linkedList.insertStart(16);
linkedList.insertEnd(17);

linkedList.traverseList();
print("Size:" , linkedList.size1());

print("Remove 15");
linkedList.remove(15);

linkedList.traverseList();
print("Size:" , linkedList.size1());
