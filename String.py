try:
    class Stack(object):
        def __init__(self):
            self.stk = []

        def stack_return(self):
            return self.stk
        
        def push(self, data):
            self.stk.append(data)
        
        def pop(self):
            self.stk.pop()

        def peek(self):
            if not self.is_empty():
                return self.stk[-1]
        
        def is_empty(self):
            if self.stk:
                return False
            else:
                return True

    string = input()
    stack = Stack()
    for element in string:
        if not stack.is_empty():
            if stack.peek() == element:
                stack.pop()
            else:
                stack.push(element)
        else:
            stack.push(element)
    if stack.stack_return():
        for element in stack.stack_return():
            print(element, end='')
    else:
        print('Empty String')

except EOFError:
    pass