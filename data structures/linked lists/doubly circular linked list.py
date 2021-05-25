class Node:
    def __init__(self,data,prev,next):
        self.data=data
        self.prev=prev
        self.next=next
    
class doublyCircularList:
    def __init__(self):
        self.head=None
        
    def insertAtBegining(self,data):
        if self.head is None:
            self.head=Node(data,self.head,self.head)
            self.head.prev=self.head
            self.head.next=self.head
            return
        itr=self.head
        self.head=Node(data,itr.prev,itr)
        itr.prev.next=self.head
        itr.prev=self.head
        
    def insertAtEnd(self,data):
        if self.head is None:
            self.insertAtBegining(data)
            return
        itr=self.head
        itr.prev.next=Node(data,itr.prev,itr)
        itr.prev=itr.prev.next
        
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
    l1=doublyCircularList()
    l1.insertAtBegining('mango')
    l1.insertAtBegining('banana')
    l1.insertAtEnd('papaya')
    l1.insertAtEnd('grapes')
    l1.insertAtBegining('oranges')
    l1.getList()
    elements=['mango','apple','banana','grapes','orange']
    l1.insertList(elements)
    l1.getList()
    