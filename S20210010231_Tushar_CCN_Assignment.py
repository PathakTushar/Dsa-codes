
import heapq
import math
import sys

INT_MAX = sys.maxsize


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def enqueue(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def dequeue(self):
        return heapq.heappop(self.elements)[1]


class Fragmentation:
    def __init__(self, mtu, payload):
        self.mtu = mtu
        self.payload = payload
        self.header = 20

    def no_of_packets(self):
        n = ((self.payload - self.header) / (self.mtu - self.header))
        return int(math.ceil(n))


class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second


def dijkstra(graph, src, dest):
    n = len(graph)
    dist = [INT_MAX] * n
    parent = [-1] * n
    visited = [False] * n
    dist[src] = 0
    pq = PriorityQueue()
    pq.enqueue(src, 0)
    while not pq.is_empty():
        u = pq.dequeue()
        if u == dest:
            print(f"\nShortest Distance is {dist[dest]}\n")
            break
        if visited[u]:
            continue
        visited[u] = True
        for v in range(n):
            if graph[u][v] == INT_MAX:
                continue
            ans = dist[u] + graph[u][v]
            if ans < dist[v]:
                dist[v] = ans
                parent[v] = u
                pq.enqueue(v, dist[v])
    path = []
    u = dest
    while u != -1:
        path.append(u)
        u = parent[u]
    path = path[::-1]
    for z in range(len(path)):
        print(path[z], end=" ")
        if z < len(path) - 1:
            print("-> ", end="")
    print("")


def create_graph():
    n = int(input("Enter the number of Vertices ->> "))
    # Initialize adjacency matrix with all values set to infinity
    graph = [[INT_MAX for _ in range(n)] for _ in range(n)]
    # Set diagonal values to 0
    for i in range(n):
        graph[i][i] = 0
    e = int(input("Enter the number of Edges ->> "))
    # Read edges and update adjacency matrix
    for i in range(e):
        source, destination, weight = map(int, input(
            f"Enter Source, Destination and Weight of Edge {i + 1} ->> ").split())
        graph[source][destination] = weight
    print("Adjacency Matrix of the Graph ->> ")
    for i in range(n):
        for j in range(n):
            if graph[i][j] == INT_MAX:
                print(f"{INT_MAX} ", end="")
            else:
                print(f"{graph[i][j]} ", end="")
        print()
    return graph


if __name__ == '__main__':
    mtu = int(input("Enter the value of MTU ->> "))
    payload = int(
        input("Enter the value of payload(including header size) ->> "))
    packet_size = Fragmentation(mtu, payload).no_of_packets()
    print(f"Packet Size ->> {packet_size}\n")
    graph = create_graph()
    for j in range(packet_size):
        choice = int(
            input("Do you to create a new topology?\n(0 ->> NO\n1 ->> YES)\n"))
        if choice == 0:
            src, dest = map(int, input(
                f"Enter Source and Destination of Packet {j + 1} ->> ").split())
            dijkstra(graph, src, dest)
        else:
            graph = create_graph()
            src, dest = map(int, input(
                f"Enter Source and Destination of Packet {j + 1} ->> ").split())
            dijkstra(graph, src, dest)

    
    

