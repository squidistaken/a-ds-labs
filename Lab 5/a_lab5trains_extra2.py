"""
File: a_lab5trains_extra2.py
Authors:
    Marcus Persson (m.h.o.persson@student.rug.nl)
    Marinus van den Ende (m.van.den.ende.1@student.rug.nl)

Description:
    This program is a bonus assignment, regarding going international.
"""
from graph import UndirectedGraph
from minheap import MinHeap


def find_shortest_path(graph: UndirectedGraph, start: int, end: int) -> \
        (list[int], int):
    """
    Returns the shortest path in an undirected graph from a start node and
    end node, using Dijkstra's algorithm.
    :param graph: UndirectedGraph class.
    :param start: Starting node.
    :param end: Ending node.
    :return: Tuple of the shortest possible path, represented as a list of
             points, and the minimum distance.
    """
    # Accounts for if we put in the same two nodes.
    if start == end:
        return [start, end], 0

    # Implements a priority queue as a MinHeap.
    p_queue = MinHeap()
    p_queue.enqueue((0, start))

    # We create a list of (minimum) distances from the start node.
    dist = [float("inf")] * graph.size()
    dist[start] = 0

    # We create a reference list of nodes' parent nodes
    parent_of = [None] * graph.size()

    while p_queue.size():
        min_dist, node = p_queue.remove_min()

        for e in graph._neighbours[node]:
            # In our undirected graph, we do not add two pathways twice, so
            # destination/origin are interchangeable.
            vertex = e._destination if e._destination != node else e._origin
            weight = e._weight
            if dist[vertex] > dist[node] + weight:
                dist[vertex] = dist[node] + weight
                p_queue.enqueue((dist[vertex], vertex))
                parent_of[vertex] = node

    if parent_of[end] is None:
        # If there is no parent, that means there is no possible path.
        return None, None

    pathway = [end]
    parent = parent_of[end]

    while parent is not None:
        pathway.append(parent)
        parent = parent_of[parent]

    pathway.reverse()

    return pathway, dist[end]


class TrainNetwork:
    """
    This class represents a train network, represented as an UndirectedGraph.
    """

    def __init__(self):
        _station_count = int(input())
        self.stations = [None] * _station_count
        for i in range(_station_count):
            pos, item = input().split(" ", 1)
            self.stations[int(pos)] = item

        _connection_count = int(input())
        self._connections = []
        while len(self._connections) < _connection_count:
            self._connections.append(tuple(input().split()))

        _disruption_count = int(input())
        self._disruptions = []
        while len(self._disruptions) < _disruption_count:
            self._disruptions.append((input(), input()))

        self.network = self._create_network(self.stations,
                                            self._connections,
                                            self._disruptions)

    def _create_network(self, stations: list, connections: list,
                        disruptions: list) -> (UndirectedGraph, list):
        network = UndirectedGraph(len(stations))

        for i in range(len(connections)):
            if (stations[int(connections[i][0])],
                stations[int(connections[i][1])]) not in disruptions:
                network.add_edge(int(connections[i][0]),
                                 int(connections[i][1]),
                                 int(connections[i][2]))

        return network


network_count = int(input())
networks = [None] * network_count

for i in range(network_count):
    networks[i] = TrainNetwork()
    start = input()
    while start != "!":
        end = input()
        if start not in networks[i].stations or end not in networks[i].stations:
            print("UNREACHABLE")
        else:
            journey, distance = (
                find_shortest_path(networks[i].network,
                                   networks[i].stations.index(start),
                                   networks[i].stations.index(end)))

            if distance is None:
                print("UNREACHABLE")
            else:
                for j in journey:
                    print(networks[i].stations[j])
                print(distance)
        start = input()
