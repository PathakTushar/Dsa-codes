#include <iostream>
#include <vector>
#include <set>
#include <limits>
#include <algorithm>
#include <string>
using namespace std;

const int INF = numeric_limits<int>::max();

vector<int> dijkstra(vector<vector<pair<int, int>>> graph, int start) {
    int n = graph.size();
    vector<int> distance(n, INF);
    set<pair<int, int>> unvisited;
    distance[start] = 0;
    unvisited.insert({0, start});
    while (!unvisited.empty()) {
        int u = unvisited.begin()->second;
        unvisited.erase(unvisited.begin());
        for (auto edge : graph[u]) {
            int v = edge.first;
            int weight = edge.second;
            if (distance[u] + weight < distance[v]) {
                unvisited.erase({distance[v], v});
                distance[v] = distance[u] + weight;
                unvisited.insert({distance[v], v});
            }
        }
    }
    return distance;
}
int numfragments;
vector<int> fragmentation(int payload, int mtu) {
     int payload_size = payload-20;
    int Mtu = mtu-20;
    numfragments = payload/Mtu; // round up division
    if(payload % Mtu != 0){
        numfragments++;
    }
    cout<<"Total fragments : "<< numfragments<<endl;
    int j=0;
    vector<int> fragments(numfragments);
    for (int i = 0; i < numfragments; i++){
        int offset = i * mtu;
        while(payload_size > Mtu){
            payload_size = payload_size-Mtu;
            fragments[j]=mtu;
            j++;
        }
        fragments[j] = payload_size+20;
    }
    return fragments;
}

int main() {
   int payload_Size;
    cout << "Enter payload: ";
    cin>>payload_Size;
    int mtu;
    cout << "Enter MTU: ";
    cin >> mtu;
    vector<int> fragment = fragmentation(payload_Size, mtu);
    vector<int> ints;
    for (int i = 0; i < fragment.size(); i++) {
        cout << "Fragment_size " << i << ": " << fragment[i] << endl;
        cout<<"Enter the no of vertices and no of edges :";
        int vertices, edge;
        cin >> vertices >> edge;
        int start,dest;
        cout<<"Enter the start and end points";
        cin>> start >> dest;
        vector<vector<pair<int, int>>> graph(vertices);
        for (int i = 0; i < edge; i++) {
            int x, y, z;
            cin >> x >> y >> z;
            graph[x].push_back({y, z});
            graph[y].push_back({x, z});
        }
        vector<int> dist = dijkstra(graph, start);
        int flag = 0;
        int temp;
        for (temp = 0; temp < vertices; temp++) {
            if (dist[temp] == INF) {
                flag=1;
                break;
            }
            else if(temp == dest) {
                if(temp == 0) continue;
                cout << "Shortest path from " << start << " to " << temp << " is " << dist[temp] << endl;
            }
        }
        if(flag == 1){
                cout << "No path from source to destination" << endl;
            }

    }
     
       
    
    return 0;
}
