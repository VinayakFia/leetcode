#include <utility>
#include <vector>
#include <map>
#include <set>

using namespace std;

class Solution {
public:
    int minReorder(int n, vector<vector<int>>& connections) {
        // edges going out from map.at(0)
        map<int, vector<int>> edges;

        for (vector<int> connection : connections) {
            edges.insert({connection[0], {}});
        }
            
        for (vector<int> connection : connections) {
            edges.at(connection[0]).push_back(connection[1]);
        }
        
        set<int> valid = 
        for (pair<int, vector<int>> p : edges) {
            dfs(edges, p.first);
        }
    }

    int dfs(map<int, vector<int>>& edges, set<int> valid, int c) {
        if (edges[c][])
    }
};