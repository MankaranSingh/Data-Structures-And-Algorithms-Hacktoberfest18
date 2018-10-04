class node:

    def __init__(self, value):
        self.data = value
        self.next = None
        

class linkstack:

    def __init__(self):
        self.top=None

    def push(self, value):
        if self.top=None:
            self.top=node(value)
            print('Value added')
        else:
            temp=node(value)
            temp.next=self.top
            self.top=temp
            print('Value inserted')

    def pop(self):
        if self.top=None:
            print('Stack underflow')
            return None 
        else:
            temp=self.top
            value=self.top.data
            self.top=self.top.next
            del temp
            return value

    def isEmpty(self):
        if self.top is None:
            print('Stack is empty')
        else:
            print('Stack is not empty')

    def getTop(self):
        if self.top is None:
            print('Stack empty')
            return None
        else:
            return self.top.data

    def __str__(self):
        result=''
        current=self.top
        while current!=None:
            result+=str(current.data) + '->'
            current=current.next
        return result


s=linkstack()
s.push(5)
s.push(6)
a=s.pop
a**2
s.push(a)
s.isEmpty
print(s.getTop)
print(s)


            
    
