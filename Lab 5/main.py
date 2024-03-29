"""

"""
from graph import UndirectedGraph, GraphEdge
from heap import Heap

city_mapping = {
    'Amsterdam': 0,
    'Den Haag': 1,
    'Den Helder': 2,
    'Utrecht': 3,
    'Eindhoven': 4,
    'Maastricht': 5,
    'Nijmegen': 6,
    'Enschede': 7,
    'Zwolle': 8,
    'Groningen': 9,
    'Leeuwarden': 10,
    'Meppel': 11
}

connections = [
    ('Amsterdam', 'Den Haag', 46),
    ('Amsterdam', 'Den Helder', 77),
    ('Amsterdam', 'Utrecht', 26),
    ('Den Haag', 'Eindhoven', 89),
    ('Eindhoven', 'Maastricht', 63),
    ('Eindhoven', 'Nijmegen', 55),
    ('Eindhoven', 'Utrecht', 47),
    ('Enschede', 'Zwolle', 50),
    ('Groningen', 'Leeuwarden', 34),
    ('Groningen', 'Meppel', 49),
    ('Leeuwarden', 'Meppel', 40),
    ('Maastricht', 'Nijmegen', 111),
    ('Meppel', 'Zwolle', 15),
    ('Nijmegen', 'Zwolle', 77),
    ('Utrecht', 'Zwolle', 51)
]

graph = UndirectedGraph(len(city_mapping))

for connection in connections:
    city1, city2, weight = connection
    node1 = city_mapping[city1]
    node2 = city_mapping[city2]
    graph.add_edge(node1, node2, weight)


def dijkstra(graph: UndirectedGraph, start: int, goal: int) -> (list[int], int):
    key = list(city_mapping.keys())

    s = [i for i in range(len(city_mapping))]
    d = Heap()

    for i in range(len(s)):
        # Probably going to give issues due to float.
        if i != start:
            d.enqueue(float('inf'))
        else:
            d.enqueue(0)

    parent_of = [None] * len(city_mapping)

    while s:
        cd = d.deep_copy()
        pseudo_weight, origin = cd.remove_min()
        while origin not in s:
            pseudo_weight, origin = cd.remove_min()

        del cd

        index = s.index(origin)
        s.pop(index)

        for path in graph.neighbours[origin]:
            node = path.other_node(origin)
            d_weight = d.get_weight_from_key(node)
            if d_weight > pseudo_weight + path.get_weight():
                d.set_weight_from_key(node, pseudo_weight + path.get_weight())
                parent_of[node] = origin

    if parent_of[city_mapping.get('Amsterdam')] is None:
        return None, None

    pathway = [goal]
    parent = parent_of[goal]

    while parent is not None:
        pathway.append(parent)
        parent = parent_of[parent]

    pathway.reverse()

    return pathway, d.get_weight_from_key(goal)


print(dijkstra(graph, city_mapping.get('Maastricht'), city_mapping.get("Amsterdam")))
