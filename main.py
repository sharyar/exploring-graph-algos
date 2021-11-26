from graph import Node, Graph

nodes = [Node(x) for x in range(0, 12)]

nodes[1].add_edge(nodes[3])
nodes[3].add_edge(nodes[5])
nodes[5].add_edge(nodes[1])

nodes[3].add_edge(nodes[11])

nodes[11].add_edge(nodes[6])
nodes[11].add_edge(nodes[8])

nodes[6].add_edge(nodes[10])
nodes[10].add_edge(nodes[8])
nodes[8].add_edge(nodes[6])

nodes[5].add_edge(nodes[9])
nodes[5].add_edge(nodes[7])

nodes[9].add_edge(nodes[2])
nodes[9].add_edge(nodes[4])
nodes[7].add_edge(nodes[9])
nodes[4].add_edge(nodes[7])
nodes[2].add_edge(nodes[4])

nodes[2].add_edge(nodes[10])
nodes[9].add_edge(nodes[8])

nodes.pop(0)

graph = Graph(nodes)
# print(graph.ucc())
# print(graph.shortest_paths(node_s, node_v))
# print(graph.dfs(node_s, node_u))
# print(graph.dfs_recursive(node_s, node_w))
# print(graph.topological_sort())
print(graph.rev_topological_sort())
print(graph.scc())
