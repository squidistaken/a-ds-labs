"""
File: lab5trains.py
Authors: Marcus Persson (m.h.o.persson@student.rug.nl), Marinus van den Ende (m.van.den.ende.1@student.rug.nl)

Description:
    This program uses Dijkstra’s Algorithm to find the fastest connection and output the list of all stations along
    that route, including the starting and ending station, as well as the total time the connection will take.
"""

# Input: n current disruptions.
disruptions = int(input())

# Input: n many disruptions, in which each disruption consists of a tuple
#        regarding a direct connection.
banned_connections = []
for i in range(disruptions):
    connection = (input(), input())
    banned_connections.append(connection)

# Input: Queries, in which each query consists of a tuple regarding a
#        start and end. Program ends when input == "!".
station = input()
while station != "!":
    query = (station, input())
    # Do something here

    station = input()
