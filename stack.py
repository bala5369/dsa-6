'''stacks:linear datastructure,which stores in a LIFO order
stack functions:
    1)insertion->push()-append()
    2)deletion->pop()-pop()
    3)view->peek()-[-1]
    4)stack full=stack overflow()
    5)empty->isempty()
    6)last in first out 
    7)len()-sizeof()'''


#code to demonstrate stack operations
'''stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)
print("stack after pushing:",stack)
deleted=stack.pop()
print("stack after deleting one time:",stack)
deleted=stack.pop()
print("stack after deleting two times:",stack)
print("stack element at the top/element ready to delete:",stack[-1])
print("remaining elements /size of the stack/length is:",len(stack))'''


#code to take user-defined input to create a stack
'''stack=[]
n=int(input("enter size of the stack:"))
for i in range(n):
    val=int(input("enter value:"))
    stack.append(val)
print("stack:",stack)
print("pop:",stack.pop())
print("stack:",stack)'''

#code to create stack using a class and access the elements in the stack
'''class stack:
    def __init__ (self):
        self.stack=[]
    def push(self,val):
        self.stack.append(val)
    def pop(self):
        if len(self.stack)==0:
            return "stack empty......."
        return self.stack.pop()
    def peek(self):
        if len(self.stack)==0:
            return "stack empty......."
        return self.stack[-1]
    def display(self):
        return self.stack
s=stack()
s.push(2)
s.push(22)
s.push(222)
s.push(2222)
s.push(22222)
print("stack is:",s.display())
print("popped element is:",s.pop())
print("stack elements after popping:",s.display())
print("peek element is:",s.peek())'''

#code to reverse a string using a stack
'''n=input("enter a string:")
stack=[]
for ch in n:
    stack.append(ch)
rev_str=""
while stack:
    rev_str+=stack.pop()
print("reversed string:",rev_str)'''

#code to check the balancing paranthesis using stack
#code to check an expression to balance
'''n=input("enter the paranthesis sequence/expression:")
stack=[]
balanced=True
for ch in n:
    if ch in "([{":
        stack.append(ch)
    elif ch in "}])":
        if not stack:
            balanced=False
            break
        top=stack.pop()
        if (ch==')' and top!='(' or ch=='{' and top!='}' or ch=='[' and top!=']'):
            balanced=False
            break
if balanced and not stack:
    print("balanced")
else:
    print("not balanced")'''

#code to perform stack empty in a stack
'''class stack:
    def __init__(self):
        self.stack=[]
    def is_empty(self):
        return len(self.stack)==0
    def pop(self):
        if self.is_empty():
            print("stack is empty")
        else:
            print("popped:",self.stack.pop())
s=stack()
s.pop()'''


#code to perform stack overflow
'''class stack:
    def __init__(self,size):
        self.stack=[]
        self.size=size
    def is_full(self):
        return len(self.stack)==self.size
    def push(self,val):
        if self.is_full():
            print("stack is full....")
        else:
            self.stack.append(val)
            print(val,"pushed")
s=stack(3)
s.push(10)
s.push(20)
s.push(30)
s.push(40)'''
