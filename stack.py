#stack
stack=[0]*100
print(stack)
top=-1
def push(x):
    global top
    top+=1
    stack[top]=x
def pop():
    global top
    if top==-1:
        print("Stack underflow")
    else:
        top-=1
def peek():
    if top==-1:
        print("Stack underflow")
    else:
        print(stack[top])
def stack_overflow():
    global top
    if top==99:
        print("Stack overflow")
def stack_underflow():
    global top
    if top==-1:
        print("Stack underflow")
push(1)
push(2)
push(3)
print(stack)
pop()
peek()
stack_overflow()
stack_underflow()