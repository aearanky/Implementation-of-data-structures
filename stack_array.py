# implement stack with arrays

class Stack(object):

	def __init__(self):
		self.stack = [];
		
	def isEmpty(self):
		return self.stack is []
	
	def push(self,data):
		self.stack.append(data)
		
	# LIFO => return the last item
	def pop(self):
		data = self.stack[-1]; #index of last item from the top
		del self.stack[-1];
		return data;
		
	def peek(self):
		data = self.stack[-1]; #index of last item from the top
		return data;
		
	def sizeStack(self):
		return len(self.stack);
		


stack = Stack();
stack.push(1);
stack.push(2);
stack.push(3);

print(stack.sizeStack());
print("Popped: ", stack.pop());

print(stack.sizeStack());
print("Peek: ", stack.peek());

print(stack.sizeStack());

