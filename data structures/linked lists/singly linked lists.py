class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next =next
class linkedList:
    def __init__(self):
        self.head=None
        
    def insertAtBegining(self,data):
        node = Node(data,self.head)
        self.head=node
       
    def insertAtEnd(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
        
        
    def getLength(self):
        count=0
        itr=self.head
        while itr:
            itr=itr.next
            count+=1
        return count
    
    
    def insertAt(self,data,index):
        if self.head is None:
            print("list is empty!")
            return
        if index<0 or index>self.getLength():
            print('invalid index!')
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = Node(data,itr.next)
                break
            itr=itr.next
            count+=1
            
        
    def insertList(self,arr):
        self.head=None
        for i in arr:
            self.insertAtEnd(i)
        return
    
    def deleteAtIndex(self,index):
        if self.head is None:
            print("list is empty!")
            return
        if index<0 or index>self.getLength():
            print('invalid index!')
            return
        if index==0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next=itr.next.next
                break
            count+=1
            itr=itr.next
            
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
        
if __name__ == "__main__":
    l1 = linkedList()
    elements=['mango','apple','banana','grapes','orange']
    l1.insertList(elements)
    l1.insertAt('papaya', 2)
    
    l1.getList()
    
    l1.deleteAtIndex(3)
    
    l1.getList()