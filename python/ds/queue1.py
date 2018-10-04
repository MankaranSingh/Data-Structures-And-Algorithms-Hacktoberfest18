class queue:

    def __init__(self):
        self.lst=list()

    def enqueue(self, value):
        self.lst.append(value)

    def dequeue(self):
        self.lst.pop(0)

    def front(self):
        return self.lst[-1]

    def size(self):
        return len(self.lst)

    def __str__(self):
        return str(self.lst)

    
