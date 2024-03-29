class GraphEdge:
    def __init__(self, origin, destination, weight: float = 1.0):
        self._origin = origin
        self._destination = destination
        self._weight = weight

    def is_incident(self, node: int) -> bool:
        return node == self._origin or node == self._destination

    def other_node(self, node: int):
        if self.is_incident(node):
            return self._origin + self._destination - node
        return -1

    def get_origin(self) -> int:
        return self._origin

    def get_destination(self) -> int:
        return self._destination

    def get_weight(self) -> float:
        return self._weight


class UndirectedGraph:
    def __init__(self, node_count: int):
        self.neighbours = [[] for _ in range(node_count)]

    def add_edge(self, node1: int, node2: int, weight: int = 1):
        new_edge = GraphEdge(node1, node2, weight)
        self.neighbours[node1].append(new_edge)
        self.neighbours[node2].append(new_edge)

    def destinations(self, node: int) -> list[int]:
        return self.neighbours[node]

    def print_graph(self):
        for node, edges in enumerate(self.neighbours):
            print(f"Node {node}:")
            for edge in edges:
                print(f"\t-> Connected to node {edge.other_node(node)} with weight {edge.get_weight()}")
