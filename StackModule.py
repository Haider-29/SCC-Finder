class Stack:

    def __init__(self):

        self.stackList = []

    def push(self, value):

        self.stackList.append(value)

    def pop(self):

        return self.stackList.pop()

    def isEmpty(self):

        if(len(self.stackList) == 0):
            return True
        return False

    def getSize(self):

        return len(self.stackList)

    def peek(self):

        return self.stackList[-1]

    def print(self):

        for i in self.stackList:
            print(i)

    def reverse(self):

        reverseStack = Stack()

        while not self.isEmpty():

            reverseStack.push(self.pop())

        return reverseStack

