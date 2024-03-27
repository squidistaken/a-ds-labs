"""
File: graph.py
Authors: Marcus Persson (m.h.o.persson@student.rug.nl), Marinus van den Ende (m.van.den.ende.1@student.rug.nl)

Description:
    This program creates an UndirectedGraph class, based off the one taught in the lecture and reader.
"""

class GraphEdge:
    def __init__(self, origin, destination, weight: float = 1.0):
        self._origin = origin
        self._destination = destination
        self._weight = weight

    def is_incident(self, node: int) -> bool:
        return node == self._origin or node == self._destination

    def other_node(self, node: int) -> int:
        if self.is_incident(node):
            return self._origin + self._destination - node - node
        return -1


class UndirectedGraph:
    def __init__(self, node_count: int) -> None:
        self._neighbours = [[] for _ in range(node_count)]

    def __getitem__(self, node: int):
        return self._neighbours[node]

    def add_edge(self, node1: int, node2: int, weight: int = 1):
        new_edge = GraphEdge(node1, node2, weight)
        self._neighbours[node1].append(new_edge)
        self._neighbours[node2].append(new_edge)

    def size(self) -> int:
        return len(self._neighbours)

