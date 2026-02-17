'''linkedlist
    linear datatype where the data is interlinked between the data
    the entire data is called a "NODE" block
    connectivity of n nodes is called linkedlist
    Types:
    1)single
    2)double
    3)circle'''


#creating a node
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None'''

#code to perform insertion operation in a single/singly linked list 
#insert at the end
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insert_at_end(head,val):
    new_node=node(val)
    if head is None:
        return new_node
    temp=head
    while temp.next:
        temp=temp.next
    temp.next=new_node
    return head
def print_list(head):
    temp=head
    while temp:
        print(temp.data,end="->")
        temp=temp.next
    print("Tail")
head=None
n=int(input("enter number of elements :"))
for i in range(n):
    val=int(input("enter a value:"))
    head=insert_at_end(head,val)
print("singly linked list :",print_list(head))'''



#code to perform insertion at end and deleting at end
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insert_at_end(head,val):
    new_node=node(val)
    if head is None:
        return new_node
    temp=head
    while temp.next:
        temp=temp.next
    temp.next=new_node
    return head
def delete_end(head):
    if head is None:#list empty
        print("list is empty")
        return None
    if head.next is None:#single element
        return None
    temp=head
    while temp.next.next:
        temp=temp.next
    temp.next=None
    return head
def print_list(head):
    temp=head
    while temp:
        print(temp.data,end="->")
        temp=temp.next
    print("Tail")
head=None
n=int(input("enter number of elements :"))
for i in range(n):
    val=int(input("enter a value:"))
    head=insert_at_end(head,val)
print("original singly linked list :",print_list(head))
head=delete_end(head)
print("after deleting element at the element:",print_list(head))'''



#code to perforn search operation on insert at end in singly linked list
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insert_at_end(head,val):
    new_node=node(val)
    if head is None:
        return new_node
    temp=head
    while temp.next:
        temp=temp.next
    temp.next=new_node
    return head
def search(head,key):
    pos=1
    temp=head
    while temp:
        if temp.data==key:
            return pos
        temp=temp.next
        pos+=1
    return -1
head=None
n=int(input("enter number of elements :"))
for i in range(n):
    val=int(input("enter a value:"))
    head=insert_at_end(head,val)
key=int(input("enter search element:"))
p=search(head,key)
if p==-1:
    print("search element not found!!!")
else:
    print("search element found at position:",p)'''