"""
    V = {a,b,c,d,e}
    E = {ab,ac,cd,bd,de}
"""
class graph:
    def __init__ (self, gdict = None):
        if gdict is None:
            gdict = []
        self.gdict = gdict
    
    def edges(self):
        return self.findEdges()

    # Get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys())
    
    def addVertex(self, vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx] = []

    def findEdges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename
    
    def addEdges(self, edge):
        # Make it unordered and immutable
        edge = set(edge)
        # Turn it into a tuple
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            # Add vrtx2 to the new edge of vrtx1
            self.gdict[vrtx1].append(vrtx2)
        else:
            # A whole new edge, with a whole new vertices
            self.gdict[vrtx1] = [vrtx2]

# Create the dictionary w/ graph elements
graph_elements = {   "a" : ["b","c"],
            "b" : ["a","d"],
            "c" : ["a","d"],
            "d" : ["b","c","e"],
            "e" : ["d"]
        }

g = graph(graph_elements)

print(g.getVertices())
print (g.findEdges())

g.addVertex("f")
print(g.getVertices())

g.addEdges({'a','e'})
g.addEdges({'f','c'})
print(g.edges())
