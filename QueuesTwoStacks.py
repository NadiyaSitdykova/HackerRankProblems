def is_empty(stack):
    return len(stack) == 0

class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []

    def update_stack2(self):
        while len(self.first) > 0:
            self.second.append(self.first.pop())
    
    def peek(self):
        if is_empty(self.second):
            self.update_stack2()
        if not is_empty(self.second):
            return self.second[-1]
        return None
        
    def pop(self):
        if is_empty(self.second):
            self.update_stack2()
        if not is_empty(self.second):
            self.second.pop()
        
    def put(self, value):
        self.first.append(value)
        

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
