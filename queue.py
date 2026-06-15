queue=[0]*100
head=tail=-1

def push(x):
    global tail
    global head
    if queue_overflow():
        return
    elif tail==-1:
        head+=1
        tail+=1
        queue[tail]=x
    else:
        tail+=1
        queue[tail]=x


def queue_overflow():
    global tail
    if tail==99:
        print("Queue overflow")
        return True
    return False


def queue_underflow():
    global head
    if head==-1:
        print("Queue underflow")
        return True
    return False


def pop():
    global head, tail
    if queue_underflow():
        return
    x = queue[head]
    if head==tail:
        head=tail=-1
    else:
        head+=1
    return x


def peek():
    global tail
    global head
    if queue_underflow():
        return
    print(queue[head])


push(10)
push(20)
print(queue)
print(pop())
print(pop())
peek()