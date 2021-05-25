class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next
    
class doublyLinkedList:
    def __init__(self):
        self.head=None
        
    def insertAtBegining(self,data):
        self.head=Node(data,None,self.head)
    
    def insertAtEnd(self,data):
        if self.head is None:
            self.head=Node(data,None,None)
            return
        
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,itr,None)
        
    def insertList(self,arr):
        self.head=None
        for i in arr:
            self.insertAtEnd(i)
        return
            
    def insertAfter(self,i,data):
        
        itr= self.head
        while itr:
            if itr.data == i:
                itr.next=Node(data,itr,itr.next.next)
                itr.next.next.prev=itr.next
                return
            itr = itr.next
            
    def removeByValue(self,data):
        if self.head.data==data:
            self.head=self.head.next
            self.head.prev=None
            return
        itr=self.head
        while itr:
            if itr.next.data == data:
                itr.next=itr.next.next
                itr.next.prev=itr
                return
            itr = itr.next
            
        
    def getList(self):
        if self.head is None:
            print("list is empty")
            return
        else:
            itr=self.head
            while itr:
                print(itr.data,"->",end='')
                itr=itr.next
            print('end')
        
    def getReverseList(self):
        itr=self.head
        while itr.next:
            itr=itr.next
        while itr.prev:
            print(itr.data,'<-',end='')
            itr=itr.prev
        print('start')
        
if __name__ == '__main__':
    l1=doublyLinkedList()
    l1.insertAtBegining('mango')
    l1.insertAtEnd('banana') 
    l1.getList()
    
    elements=['mango','apple','banana','grapes','orange']
    l1.insertList(elements)
    l1.getList()
    l1.getReverseList()
    l1.insertAfter('mango','papaya')
    l1.getList()
    l1.removeByValue('mango')
    l1.getList()