class node:

    def __init__(self, value):
        self.data = value
        self.next = None
        

class linklist:

    def __init__(self):
        self.head=None
        
    def insertbeg(self, value):
        if self.head is None:
            self.head=node(value)
        else:
            temp=node(value)
            temp.next=self.head
            self.head=temp
        print('Value inserted')


    def delbeg(self):
        if self.head == None:
            print('List already empty')
            return None
        else:
            temp=self.head.data
            
            self.head=self.head.next
            return temp

    def delnode(self, value):
        if self.head==None:
            print('List already empty')
        if self.head.data==value:
            temp=self.head
            self.head=self.head.next
            del temp
            print('value deleted')
        else:
            current=self.head
            prev=None
            while current!=None or current.data!=int(value):
                prev=current
                current=current.next
                
            if current.data==value:
                temp=current
                prev.next=current.next
                del temp
                print('Value deleted')
            else:
                print('value not found')

    def __str__(self):
            
        current=self.head
        result=''
        if current!=None:
            while current!=None:
                result+=str(current.data) + '->'
                current=current.next
        return result

    def sortedlinklist(self, value):
        if self.head==None:
            self.head=node(value)
            print('Value inserted')
        elif value<self.head.data:
            temp=node(value)
            temp.next=self.head
            self.head=temp
            print('Value inserted')
        else:
            current=self.head
            prev=None
            while value>current.data:
                prev=current
                current=current.next
                temp=node(value)
                if current is None:
                    prev.next=temp
                    print('Value inserted')
                    
                    break
                else:
                    
                    current.next=temp
                    temp.next=current.next
                    
                    
                    print('Value inserted')
                    
                    break
            
                
                

                    
        
            
            
                
                
                
                
                
                
                
            
            
            
        
        
            

                    
                
                    
                
            
        
            
