"""
File: lab5trains.py
Authors: Marcus Persson (m.h.o.persson@student.rug.nl), Marinus van den Ende (m.van.den.ende.1@student.rug.nl)

Description:
    This program uses Dijkstra’s Algorithm to find the fastest connection and output the list of all stations along
    that route, including the starting and ending station, as well as the total time the connection will take.
"""
from graph import UndirectedGraph


def create_network(banned: list[tuple]) -> (UndirectedGraph, list):
    """
    Returns a heap of all connected stations and their distances, in which each node is a dictionary with a
    key tuple (station1, station2) and value distance.
    :param banned: A list of tuples of banned connections.
    :return: A tuple of the network and list of all stations.
    """
    file = open("connections.csv", "r")
    connections = []
    cities = []
    line = file.readline().strip("\n").split(",")

    while line != [""]:
        if (line[0], line[1]) in banned:
            continue
        if line[0] not in cities:
            cities.append(line[0])
        if line[1] not in cities:
            cities.append(line[1])

        connections.append((cities.index(line[0]), cities.index(line[1]), int(line[2])))
        line = file.readline().strip("\n").split(",")

    network = UndirectedGraph(len(cities))

    for item in connections:
        network.add_edge(item[0], item[1], item[2])

    return network, cities


# TODO: Dijkstra's Algorithm
def dijkstra(network: UndirectedGraph, query: tuple) -> None:
    route = []
    distance = 0
    if True:
        print(*route, sep="\n")
        print(distance)
        return
    print("UNREACHABLE")
    return


# Input: n current disruptions.
disruptions = int(input())

# Input: n many disruptions, in which each disruption consists of a tuple regarding a direct connection.
banned_connections = []
for i in range(disruptions):
    connection = (input(), input())
    banned_connections.append(connection)

network, cities = create_network(banned_connections)

# Input: Queries, in which each query consists of a tuple regarding a start and end. Program ends when input == "!".
station = input()
while station != "!":
    query = (cities.index(station), cities.index(input()))
    # Do something here
    dijkstra(network, query)
    station = input()
