from graph import UndirectedGraph
from heapGPT import MinHeap
from heap import Heap

city_mapping = {
    'Amsterdam': 0,
    'Den Haag': 1,
    'Den Helder': 2,
    'Eindhoven': 3,
    'Enschede': 4,
    'Groningen': 5,
    'Leeuwarden': 6,
    'Maastricht': 7,
    'Meppel': 8,
    'Nijmegen': 9,
    'Utrecht': 10,
    'Zwolle': 11
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

graph.print_graph()

pos_heap = Heap()
pos_heap.enqueue(5)
pos_heap.enqueue(9)
pos_heap.enqueue(10)
pos_heap.enqueue(6)
pos_heap.enqueue(4)
pos_heap.enqueue(7)
pos_heap.enqueue(3)

pos_heap.print_heap()

print("Popping items from the heap:")
while pos_heap.size() > 0:
    print(pos_heap.remove_min())
    print(pos_heap.print_heap())
    print()
