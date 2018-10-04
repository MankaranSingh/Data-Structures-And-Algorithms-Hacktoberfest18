class bnode:
    def __init__(self, value):
        self.data=value
        self.left=None
        self.right=None

class binarysearchtree:

    def __init__(self):
        self.root=None

    def insert(self,value):
        temp=bnode(value)
        if self.root is None:
            self.root=bnode(value)
            print('Value inserted')
        else:
            child=self.root
            parent=None
            while child!=None:
                parent=child
                if value>child.data:
                    child=child.right
                else:
                    child=child.left
                    
            if value<=parent.data:
                parent.left=bnode(value)
            else:
                parent.right=bnode(value)
            print('Value inserted')
                
            
    
