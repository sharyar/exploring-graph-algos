from __future__ import annotations  # for type hinting within an enclosing class
from typing import Dict, List, Tuple, Any


class Node():
    def __init__(self, val, connections=None):
        self.val = val
        self.connections = []
        if connections:
            self.connections = connections

    def __str__(self):
        return f"Node: {self.val}"

    def __repr__(self):
        return f"Node: {self.val}"

    def add_nodes_cnxs(self, nodes: List[Any]) -> None:
        self.connections.extend(nodes)

    def add_edge(self, node: Node) -> None:
        self.connections.append(node)

# For a directed graph, we don't need two way edges, only way edges in the connectiosn of each node


class Graph():
    def __init__(self, nodes: List[Node]):
        self.nodes = nodes

    def bfs(self, start, destination):
        if (start in self.nodes) and (destination in self.nodes):
            # create a dictionary and set all nodes as false for explored
            explored_dict = {node: False for node in self.nodes}

            explored_dict[start] = True

            # intialize queue
            queue = [start]
            while queue:
                v = queue.pop(0)
                for w in v.connections:
                    if not explored_dict[w]:
                        explored_dict[w] = True
                        queue.append(w)
            return explored_dict[destination]

        else:
            print("Start and/or destination not found in current node list")

    def dfs(self, start, destination):
        if (start in self.nodes) and (destination in self.nodes):
            explored_dict = {node: False for node in self.nodes}

            stack = [start]
            while stack:
                v = stack.pop()  # instead of pull from front, pull from back, lifo
                if not explored_dict[v]:
                    explored_dict[v] = True
                    for w in v.connections:
                        stack.append(w)

            # will only be explored if on the same graph and reachable from start
            return explored_dict[destination]

    def ucc(self) -> Dict[Node, int]:
        explored_dict = {node: False for node in self.nodes}
        cc = {}
        numCC = 0
        for node in self.nodes:
            if not explored_dict[node]:
                numCC += 1
                q = [node]
                while len(q) > 0:
                    v = q.pop(0)
                    cc[v] = numCC
                    for w in v.connections:
                        if not explored_dict[w]:
                            explored_dict[w] = True
                            q.append(w)

        return cc

    def shortest_paths(self, start: Node, destination: Node) -> int:
        explored_dict = {node: False for node in self.nodes}
        explored_dict[start] = True
        distances = {node: float("inf") for node in self.nodes}
        distances[start] = 0

        q = [start]
        while len(q) > 0:
            v = q.pop(0)
            for w in v.connections:
                if not explored_dict[w]:
                    explored_dict[w] = True
                    distances[w] = distances[v] + 1
                    q.append(w)

        return distances[destination]

    def dfs_recursive(self, start: Node, destination: Node) -> bool:
        explored_dict = {node: False for node in self.nodes}

        def dfs(g, s):
            nonlocal explored_dict
            explored_dict[s] = True
            for w in s.connections:
                if not explored_dict[w]:
                    dfs(g, w)

        dfs(self.nodes, start)
        return explored_dict[destination]

    def topological_sort(self) -> List[Node]:
        """Will sort nodes of a DAG (Directed Acyclic Graph) in a toplogical order depending on their order of 
        dependencies

        :List[Node]: list of nodes in their toplogical order
        """

        # outer loop over the entire graph:
        explored_dict = {node: False for node in self.nodes}

        # depicts the dependency order or sorting position
        curr_label = len(self.nodes)

        dependency_order = {}

        def dfs_top(s: Node) -> None:
            """Inner function that does the actual sorting and explores each node provided by the outer function. 

            :param Node s: node to conduct bfs over.
            """
            nonlocal explored_dict
            nonlocal curr_label
            nonlocal dependency_order
            explored_dict[s] = True
            for w in s.connections:
                if not explored_dict[w]:
                    dfs_top(w)
            dependency_order[s] = curr_label
            curr_label -= 1

        for v in self.nodes:
            if not explored_dict[v]:
                dfs_top(v)

        return dependency_order
