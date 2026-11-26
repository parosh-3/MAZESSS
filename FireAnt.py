from collections import deque

class FireAnt:
    def __init__(self, addToQueue):
        self.queue = deque()
        self.queue.append(addToQueue)


    def add_to_queue(self, element):
        self.queue.append(element)   

    def get_and_remove(self):
        if self.queue:
            return self.queue.popleft()

    def is_empty(self) -> bool:
        return not self.queue
    