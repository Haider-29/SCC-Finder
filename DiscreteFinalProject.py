#Fatima Khan - 21i-0725
#Syed Haider Naqvi - 20i-0816
#Fareeah Naseem - 21i-0500

import GraphModule

def main():

    g = GraphModule.Graph(5)

    GraphModule.fillGraph(g)
    #GraphModule.fillGraphT(g)

    # g.addEdge(1, 0)
    # g.addEdge(0, 2)
    # g.addEdge(2, 1)
    # g.addEdge(0, 3)
    # g.addEdge(3, 4)

    #g.addEdge(0, 1)
    #g.addEdge(1, 2)
    #g.addEdge(2, 3)
    #g.addEdge(2, 4)
    #g.addEdge(3, 0)
    #g.addEdge(4, 5)
    #g.addEdge(5, 6)
    #g.addEdge(6, 4)
    #g.addEdge(7, 20000)

    g.findLargestSCC()


if __name__ == "__main__":
    main()