class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next
    
class circularList:
    def __init__(self):
        self.head=None
    
    def insertAtBegining(self,data):
        if self.head is None:  
            self.head=Node(data,self.head)
            self.head.next=self.head
            return
        itr=self.head
        while itr.next is not self.head:
            itr=itr.next
        self.head=Node(data,self.head)
        itr.next=self.head
    
    def insertAtEnd(self,data):
        if self.head is None:
            self.head=Node(data,self.head)
            self.head.next=self.head
            return
        itr=self.head
        while itr.next is not self.head:
            itr=itr.next
        itr.next=Node(data,self.head)
        
    def insertList(self,arr):
        self.head=None
        for i in arr:
            self.insertAtEnd(i)
        
        
    def getList(self):
        itr=self.head
        while itr:
            if itr.next is self.head:
                print(itr.data,'->end')
                return
            print(itr.data,'->',end='')
            itr=itr.next
        
if __name__ == '__main__':
    l1=circularList()
    l1.insertAtBegining('mango')
    l1.insertAtBegining('banana')
    l1.insertAtBegining('papaya')
    l1.insertAtBegining('apple')
    l1.insertAtEnd('grapes')
    l1.insertAtEnd('orange')
    l1.getList()
    elements=['mango','apple','banana','grapes','orange']
    l1.insertList(elements)
    l1.getList()