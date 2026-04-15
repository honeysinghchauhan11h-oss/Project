# COMP 251 Final Capstone Project

## Project Title

Network Exploration System

## Student Information

* Student Name: \[Honey Singh]
* Student ID: \[300218302]

## Project Description

This project builds a network exploration system using COMP 251 data structure ideas. The program reads a graph from `data/network.txt`, stores it as an adjacency list, and lets the user explore the network with a menu-driven interface.

## File Structure

```text
comp251\_capstone/
├── src/
│   ├── main.py
│   ├── graph.py
│   ├── heap.py
│   ├── hashmap.py
│   ├── trie.py
│   └── utils.py
├── data/
│   └── network.txt
├── README.md
└── requirements.txt
```

## How to Run

From the project root folder, run:

```bash
python src/main.py
```

## Why These Data Structures Were Chosen

### 1\. Graph as an Adjacency List

The graph is stored using an adjacency list. This is a strong choice when the network is sparse, because the space cost is O(V + E) instead of O(V^2).

### 2\. Hash Map

The custom hash map is used for fast average-case lookup of vertices, visited states, distances, and parent tracking.

### 3\. Min-Heap / Priority Queue

The min-heap supports Dijkstra’s algorithm by always removing the currently smallest-distance node first.

### 4\. Trie

The trie supports prefix search on node names. This allows the user to type the beginning of a node name and find matching nodes efficiently.

## Modules

### `src/main.py`

Runs the menu system, loads the file, builds the trie, and calls the graph operations.

### `src/graph.py`

Contains the graph implementation using an adjacency list. Also includes BFS, DFS, and Dijkstra.

### `src/heap.py`

Contains the custom array-based min-heap.

### `src/hashmap.py`

Contains the custom hash table using separate chaining.

### `src/trie.py`

Contains the trie used for prefix-based search of node names.

### `src/utils.py`

Contains small helper functions for input and formatting.

## Complexity Analysis

### Graph Representation

* Space: `O(V + E)`
* Reason: only the real vertices and edges are stored.

### BFS Shortest Path

* Time: `O(V + E)`
* Reason: each vertex and edge is processed at most once.

### DFS Traversal

* Time: `O(V + E)`
* Reason: DFS visits each reachable vertex once and checks outgoing edges.

### Dijkstra with Min-Heap

* Time: `O((V + E) log V)`
* Reason: heap operations are `O(log V)` and are used during relaxation.

### Min-Heap

* Insert: `O(log n)`
* Extract Min: `O(log n)`
* Peek: `O(1)`

### Hash Map

* Insert / Search / Delete: average `O(1)`
* Worst case: `O(n)` if collisions become extreme

### Trie

* Insert: `O(L)`
* Search: `O(L)`
* Prefix search: `O(L + k)` in practical use, where `L` is the prefix length and `k` is the size of collected output

## Sample Output

C:\\Users\\sarda\\Downloads\\gurpinder1\\comp251\_capstone>python src/main.py

COMP 251 - Network Exploration System

Uses adjacency list, BFS, DFS, hash map, heap, and Dijkstra.

Loaded 7 vertices from data/network.txt

\--------------------------------------------------

1\. Display graph

2\. BFS shortest path (unweighted)

3\. DFS traversal

4\. Dijkstra shortest path (weighted)

5\. Check whether a node exists

6\. Show neighbors of a node

7\. Exit

Enter choice: 1

Adjacency List:

A: B(w=4), C(w=2)

B: D(w=5)

C: D(w=1), E(w=6)

D: E(w=3)

E: A(w=2)

F: G(w=1)

G: no outgoing edges

## 

