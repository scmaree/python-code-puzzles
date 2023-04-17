from tqdm import tqdm


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
