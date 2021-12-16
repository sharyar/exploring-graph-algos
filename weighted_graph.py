"""This module contains all the class definitions for the graph and nodes 
    """


class Node:
    def __init__(self, val, in_connections=None, out_connections=None):
        self.val = val
        if in_connections is None:
            self.in_connections = {}
        if out_connections is None:
            self.out_connections = {}

    def __repr__(self):
        return f"Node: {self.val}"

    def __str__(self):
        return f"Node: {self.val}"


class Graph:
    def __init__(self, nodes=None, edges=None):
        if nodes is None:
            self.nodes = set()
        else:
            self.nodes = nodes

        if edges is None:
            self.edges = {node: [] for node in self.nodes}
        else:
            self.edges = edges

    def add_edge(self, v, t, weight) -> None:
        """Adds edge between v and t and the weight of the edge. This is a directed edge. 

        :param Node v: starting node 
        :param Node t: destination node 
        :param int w: weight of the edge from v to t. 
        """
        if v in self.nodes and t in self.nodes:
            v.out_connections[t] = weight
            t.in_connections[v] = weight
            self.edges[v].append(t)
        else:
            print("Start or destination node not found in graph. ")

    def remove_edge(self, v, t):
        if v in self.nodes and t in self.nodes:
            v.out_connections.pop(t)
            t.in_connections.pop(v)
        else:
            print("Start or destination node not found in graph.")

    def check_connected_nodes(self, s, d) -> bool:
        # conduct bfs
        if s in self.nodes and d in self.nodes:
            explored_dict = {node: False for node in self.nodes}
            explored_dict[s] = True

            q = [s]

            while q:  # while not empty
                v = q.pop(0)  # the first element in the que
                for w in v.out_connections:
                    if not explored_dict[w]:
                        q.append(w)
                        explored_dict[w] = True

            # only retuns true if we reach d from s in the graph
            return explored_dict[d]

        else:
            print("Start or destination node not found in graph")

    def dijkstra_algo(self, s, d) -> bool:

        x = {s}
        length = {node: float('inf') for node in self.nodes}
        length[s] = 0

        edges_s = [w for w in s.out_connections.keys()]


if __name__ == "__main__":
    nodes = [Node(x) for x in range(6)]
    graph = Graph(nodes)

    graph.add_edge(nodes[1], nodes[2], 1)
    graph.add_edge(nodes[1], nodes[5], 4)
    graph.add_edge(nodes[2], nodes[3], 5)
    graph.add_edge(nodes[3], nodes[5], 10)

    print(graph.check_connected_nodes(nodes[1], nodes[5]))
    print(graph.check_connected_nodes(nodes[1], nodes[4]))
    graph.dijkstra_algo(nodes[1], nodes[5])
