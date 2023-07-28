#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

#define INF INT_MAX // Define a macro for infinity

// Graph class
class Graph {
    int V; // Number of vertices
    vector<pair<int, int>> *adj; // Adjacency list

public:
    Graph(int V);
    void addEdge(int u, int v, int w);
    void dijkstra(int src);
};

Graph::Graph(int V) {
    this->V = V;
    adj = new vector<pair<int, int>>[V];
}

void Graph::addEdge(int u, int v, int w) {
    adj[u].push_back(make_pair(v, w));
}

void Graph::dijkstra(int src) {
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq; // Min heap for Dijkstra's algorithm
    vector<int> dist(V, INF); // Initialize distances to infinity
    pq.push(make_pair(0, src)); // Insert source vertex with distance 0
    dist[src] = 0;

    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();

        for (auto i = adj[u].begin(); i != adj[u].end(); i++) {
            int v = i->first;
            int weight = i->second;

            if (dist[v] > dist[u] + weight) { // Relaxation step
                dist[v] = dist[u] + weight;
                pq.push(make_pair(dist[v], v));
            }
        }
    }

    // Print shortest distances
    cout << "Vertex\tDistance from Source\n";
    for (int i = 0; i < V; i++)
        cout << i << "\t" << dist[i] << endl;
}

int main() {
    int V = 6;
    Graph g(V);

    g.addEdge(0, 1, 7);
    g.addEdge(0, 2, 12);
    g.addEdge(1, 2, 2);
    g.addEdge(1, 3, 9);
    g.addEdge(2, 4, 10);
    g.addEdge(4, 3, 4);
    g.addEdge(3, 5, 1);
    g.addEdge(4, 5, 5);

    g.dijkstra(2);

    return 0;
}
