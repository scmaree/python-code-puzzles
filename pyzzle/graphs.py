from tqdm import tqdm
from collections import defaultdict


def find_cliques_of_size_plus_one(cliques: dict, nodes: list, edges: dict) -> dict:
    """Clique finder: finds all cliques of size +1 by brute force searching for one additional node

    cliques: dict
        Initial dict can be a list of edges, see description below.
    nodes: list
        All nodes in the graph to iterate over. Perhaps an update is to extract this from
        the cliques' dict.
    edges: dict
        edges = {(n1, n2): True, (n1, n3): True, ...}
         sorted such that n1 > n2

    Call this in an iterative manner until you have the desired clique size or no cliques are left.

        edges = {(n1, n2): True, (n1, n3): True, ...} sorted such that n1 > n2
        nodes = list(set(n for edge in edges.keys() for n in edge))
        triplets = find_cliques(edges, nodes)
        quadruplets = find_cliques(triplets, nodes)
        ...
    """
    larger_cliques = {}
    for edge in tqdm(cliques.keys()):
        for p_next in nodes:
            if p_next in edge:
                continue
            fail = False
            for p in edge:
                edge_next = (p, p_next) if p > p_next else (p_next, p)
                if edge_next not in edges:
                    fail = True
                    break
            if fail:
                continue
            larger_cliques[tuple(sorted([p_next, *edge]))] = True
    return larger_cliques


class Graph:
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight=1, bidirectional=False):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.weights[(from_node, to_node)] = weight

        if bidirectional:
            self.edges[to_node].append(from_node)
            self.weights[(to_node, from_node)] = weight


def dijkstra(graph: Graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path
