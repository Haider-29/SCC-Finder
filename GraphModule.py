import StackModule
from collections import defaultdict
import sys
#import resource
#resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
sys.setrecursionlimit(1000000000)
print(sys.getrecursionlimit())

currLength = 0

class Graph:

    def __init__(self, n = 0):

        self.numVertices = n
        self.adjacentVertices = defaultdict(list)

    def addEdge(self, v1, v2):

        self.adjacentVertices[v1].append(v2)


    def setVertices(self, n):

        self.numVertices = n
     

    def getTranspose(self):
        
        transpose = Graph()
 
        for i in self.adjacentVertices:

            for j in self.adjacentVertices[i]:

                transpose.addEdge(j,i)

        return transpose

    def firstDFS(self, node, visited, stack):

        visited[node] = True

        for i in self.adjacentVertices[node]:
            if not visited[i]:
                self.firstDFS(i, visited, stack)

        stack.push(node)


    def secondDFS(self, node, visited):

        global currLength

        visited[node] = True
        currLength += 1

        for i in self.adjacentVertices[node]:
            if not visited[i]:
                self.secondDFS(i, visited)
        

    def findLargestSCC(self):

        print("Scc started")

        visited = [False] * (self.numVertices)

        dfsStack = StackModule.Stack()

        for i in list(self.adjacentVertices):
            if not visited[i]:
                self.firstDFS(i, visited, dfsStack)

        transpose = self.getTranspose()

        print("First dfs done")

        visited = [False] * (self.numVertices)

        numSCCs = 0
        maxLength = 0

        global currLength

        while not dfsStack.isEmpty():
            node = dfsStack.pop()
            currLength = 0
            if not visited[node]:
                transpose.secondDFS(node, visited)
                numSCCs += 1

                if(currLength > maxLength):
                    maxLength = currLength

        print("Second dfs done")
        print("Number of SCCs are: ", end = '')
        print(numSCCs)
        print("Biggest SCC has length: ", end = '')
        print(maxLength)



    def print(self):

        for i in self.adjacentVertices:
            print(i)
            print(self.adjacentVertices[i])


def fillGraph(g):

    f = open('web-Google.txt', 'r')

    wholeText = f.read()
    linesArray = wholeText.split('\n')
    node1 = ""
    node2 = ""
    maxNode = 0

    print("Filling Graph")
    
    for i in range(0, len(linesArray) - 1):

        node1, node2 = (int(val) for val in linesArray[i].split())

        if(node1 > maxNode):
            maxNode = node1
        if(node2 > maxNode):
            maxNode = node2

        g.addEdge(int(node1), int(node2))

    g.setVertices(maxNode + 1)

def fillGraphT(g):

    f = open('web-Google.txt', 'r')

    wholeText = f.read()
    linesArray = wholeText.split('\n')
    node1 = ""
    node2 = ""
    maxNode = 0

    print("Filling Graph")
    
    for i in range(0, len(linesArray) - 1):

        node1, node2 = (int(val) for val in linesArray[i].split())

        if(node1 > maxNode):
            maxNode = node1
        if(node2 > maxNode):
            maxNode = node2

        g.addEdge(int(node1), int(node2))

    g.setVertices(maxNode + 1)
