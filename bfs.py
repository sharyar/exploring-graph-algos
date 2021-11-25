from graph import Node, Graph

node_s = Node("s")
node_u = Node("u")
node_v = Node("v")
node_w = Node("w")

node_s.add_edge(node_u)
node_u.add_edge(node_v)
node_v.add_edge(node_w)

graph = Graph([node_s, node_u, node_v, node_w])
# print(graph.ucc())
# print(graph.shortest_paths(node_s, node_v))
# print(graph.dfs(node_s, node_u))
# print(graph.dfs_recursive(node_s, node_w))
print(graph.topological_sort())
