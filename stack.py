# data-structures
def createStack():
    stack=[]
    return stack
def checkEmpty(stack):
    return len(stack)==0
def push(stack,item):
    stack.append(item)
    print("push item:"+item)
def pop(stack):
    if checkEmpty(stack):
        return "stack is empty"
    return stack.pop()  
stack=createStack()
push(stack,str(1))
push(stack,str(2))
push(stack,str(3))
push(stack,str(4))
print("pop item:"+pop(stack))
print("stack after popping an element:"+str(stack))  
def reverseString(string):
    n=len(string)
    stack=createStack()
    for i in range(0,n,1):
        push(stack,string[i])
    string=" "    
    for i in range(0,n,1):
        string+=pop(stack)
    return string 
string="HANEEFA"
string=reverseString(string)
print("Reversed string is:"+string)
