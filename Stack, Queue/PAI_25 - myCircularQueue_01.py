class MyCircularQueue:

	def __init__(self, k: int):
		self.circular_queue = [None] * k
		self.front = 0
		self.end = -1
		self.max_size = k
		self.size = 0

	def enQueue(self, value: int) -> bool:
		if self.size >= self.max_size or self.end >= self.max_size:
			return False
		if self.end + 1== self.max_size:
			self.end = 0
		else:
			self.end += 1
		self.circular_queue[self.end] = value
		self.size += 1
		return True

	def deQueue(self) -> bool:
		if self.size == 0:
			return False
		self.circular_queue[self.front] = None
		self.size -= 1
		if self.front + 1== self.max_size:
			self.front = 0
		else:
			self.front += 1
		return True


	def Front(self) -> int:
		if self.size == 0:
			return -1
		return self.circular_queue[self.front]

	def Rear(self) -> int:
		if self.size == 0:
			return -1
		return self.circular_queue[self.end]


	def isEmpty(self) -> bool:
		return self.size == 0

	def isFull(self) -> bool:
		return self.size == self.max_size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()



t = MyCircularQueue(3)
print(t.enQueue(2))
print(t.Rear())
print(t.Front())
