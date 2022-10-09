class UnionFind:
  def __init__(self, nodes = []):
    self.parent = {}
    for node in nodes:
      self.add(node)
  
  # add node
  def add(self, node):
    # initially each node is parent of itself
    if node not in self.parent:
      self.parent[node] = node
  
  # group 2 nodes A and B
  def union(self, A, B):
    p1 = self.find(A)
    p2 = self.find(B)
    if (p1 == p2): return 0 # they alrady are in the same group
    self.parent[p2] = p1

  # find the parent of a node x
  def find(self, x):
    res = x
    while (res != self.parent[res]):
      res = self.parent[res]
    return res

# Example
# let's say we have a undirected graph represented in the form of adjacency list like so
# [[1, 2], [4, 2], [3], [1], [0]]
# here the nodes are -> 0, 1, 2, 3, 4
graph = [[1, 2], [4, 2], [3], [1], [0]]
nodes = [0, 1, 2, 3, 4]

uf = UnionFind(nodes)
# lets group the nodes
for node in nodes:
  connection_nodes = graph[node]
  for connection_node in connection_nodes:
    uf.union(node, connection_node)

# In this example all nodes are connected so all the nodes belong to same group and have same parent
parents = []
for node in nodes:
  parents.append(uf.find(node))
print('parent of each node = ' ,parents)
# To get the total no of connected components or groups in the graph do the following
parents_set = set(parents)
no_of_connected_components = len(parents_set)
print('number of connected components in the graph = ', no_of_connected_components) # in this ex it's 1
