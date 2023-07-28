#include <iostream>
#include <vector>
#include <set>
#include <limits>
#include <algorithm>
#include <string>
#include <queue>
#include <climits>
using namespace std;

const int infinity = numeric_limits<int>::max();

#define INF INT_MAX // Define a macro for infinity

// Graph class
class Graph {
    int V; // Number of vertices
    vector<pair<int, int>> *adj; // Adjacency list

public:
    Graph(int V);
    void addEdge(int u, int v, int w);
    vector<int> dijkstra(int src);
};

Graph::Graph(int V) {
    this->V = V;
    adj = new vector<pair<int, int>>[V];
}

void Graph::addEdge(int u, int v, int w) {
    adj[u].push_back(make_pair(v, w));
}

vector<int> Graph::dijkstra(int src) {
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
    return dist;
}
int findingNumFragments;
vector<int> creatingSetOfFragments(int input_payload, int input_mtu) {
     int payloadAfterRemovingHeaderSize = input_payload-20;
    int mtuAfterRemovingHeaderSize = input_mtu-20;
    findingNumFragments = input_payload/mtuAfterRemovingHeaderSize;
    if(input_payload % mtuAfterRemovingHeaderSize != 0){
        findingNumFragments++;
    }
    cout<<"Total number of fragments : "<< findingNumFragments<<endl;
    int j=0;
    vector<int> vectorOfFragments(findingNumFragments);
    for (int i = 0; i < findingNumFragments; i++){
        while(payloadAfterRemovingHeaderSize > mtuAfterRemovingHeaderSize){
            payloadAfterRemovingHeaderSize = payloadAfterRemovingHeaderSize-mtuAfterRemovingHeaderSize;
            vectorOfFragments[j]=input_mtu;
            j++;
        }
        vectorOfFragments[j] = payloadAfterRemovingHeaderSize+20;
    }
    return vectorOfFragments;
}

int main() {
   int payload_Size;
    cout << "Note: The IP_HEADER_SIZE of 20 has been included in the Payload and MTU. \n";
    cout << "Enter the initial payload size : ";
    cin>>payload_Size;
    int input_mtu;
    cout << "Enter maximum transmitting unit(MTU) : ";
    cin >> input_mtu;
    vector<int> fragment = creatingSetOfFragments(payload_Size, input_mtu);
    vector<int> ints;
    for (int i = 0; i < fragment.size(); i++) {
        cout << "Fragment " << i+1 << ": " << fragment[i] << endl;
        cout<<"Enter the number of vertices and no of edges in the graph. For example (6 8):";
        int vertices, numOfEdge;
        cin >> vertices >> numOfEdge;
        int start_point,destination_point;
        cout<<"Enter the starting and end points. For example (0 5): ";
        cin>> start_point >> destination_point;
        Graph input_graph(vertices);
        cout<<"Enter source,destination,weight. For example (0 1 7)"<<endl;
        for (int i = 0; i < numOfEdge; i++) {
            int x, y, z;
            cin >> x >> y >> z;
            input_graph.addEdge(x,y,z);
        }
        vector<int> dist = input_graph.dijkstra(start_point);
        for (int i = 0; i < dist.size(); i++)
            cout << i << "\t" << dist[i] << endl;
        // int flag = 0;
        // int temp;
        // for (temp = 0; temp < vertices; temp++) {
        //     if (dist[temp] == infinity) {
        //         flag=1;
        //         break;
        //     }
        //     else if(temp == destination_point) {
        //         cout << "Shortest path from " << start_point << " to " << temp << " is " << dist[temp] << endl;
        //     }
        // }
        // if(flag == 1){
        //         cout << "No path from source to destination exists" << endl;
        //     }

    }
     
       
    
    return 0;
}
