#FIFO

class Queue(object):

	def __init__(self):
		self.queue = [];
		
	def isEmpty(self):
		return self.queue is []
		
	def enqueue(self,data):
		self.queue.append(data);
		
	def dequeue(self):
		data = self.queue[0];
		del self.queue[0];
		return data;
		
	def peek(self):
		return self.queue[0];
	
	def sizeQueue(self):
		return len(self.queue);

queue = Queue();
queue.enqueue(1);
queue.enqueue(2);
queue.enqueue(3);

print('size', queue.sizeQueue());

queue.dequeue();
queue.dequeue();

print('size:', queue.sizeQueue());


