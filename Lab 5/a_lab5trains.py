"""
File: a_lab5trains.py
Authors:
    Marcus Persson (m.h.o.persson@student.rug.nl)
    Marinus van den Ende (m.van.den.ende.1@student.rug.nl)

Description:
    This program uses Dijkstra’s Algorithm to find the fastest connection
    and output the list of all stations along that route, including the
    starting and ending station, as well as the total time the connection will take.
"""
from graph import UndirectedGraph
from minheap import MinHeap
import csv


def create_network(banned: list[tuple]) -> (UndirectedGraph, list):
    """
    Returns a heap of all connected stations and their distances, in which
    each node is a dictionary with a key tuple (station1, station2) and
    value distance.
    :param banned: A list of tuples of banned connections.
    :return: A tuple of the network and list of all stations.
    """
    connections = []
    cities = []

    with open("connections.csv") as f:
        reader = csv.reader(f)
        for line in reader:
            if (line[0], line[1]) not in banned:
                if line[0] not in cities:
                    cities.append(line[0])
                if line[1] not in cities:
                    cities.append(line[1])

                # (Origin, Destination, Distance)
                connections.append((cities.index(line[0]),
                                    cities.index(line[1]),
                                    int(line[2])))

    network = UndirectedGraph(len(cities))

    for item in connections:
        network.add_edge(item[0], item[1], item[2])

    return network, cities


# Input: n current disruptions.
disruptions = int(input())

# Input: n many disruptions, in which each disruption consists of a tuple
#        regarding a direct connection.
banned_connections = []
for i in range(disruptions):
    connection = (input(), input())
    banned_connections.append(connection)

network, cities = create_network(banned_connections)


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
    # TODO: Create a correct shortest path
    pathway = [end]

    parent_of = [None] * graph.size()
    # We create a list of (minimum) distances from the start node.
    dist = [float("inf")] * graph.size()
    dist[start] = 0

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

    parent = parent_of[end]
    while parent is not None:
        pathway.append(parent)
        parent = parent_of[parent]
    pathway.reverse()
    return pathway, dist[end]


# Input: Queries, in which each query consists of a tuple regarding a start
#        and end.
start = input()

while start != "!":
    end = input()
    if start not in cities or end not in cities:
        print("UNREACHABLE")
    else:
        journey, distance = find_shortest_path(network,
                                               cities.index(start),
                                               cities.index(end))
        if distance is None:
            print("UNREACHABLE")
        else:
            for j in journey:
                print(cities[j])
            print(distance)
    start = input()
