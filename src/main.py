import os
import sys

from graph import Graph
from trie import Trie
from utils import print_separator, prompt_user


def load_network(file_path):
    """
    File format:
    source destination weight
    or
    source destination
    If weight is missing, default to 1.
    """
    graph = Graph()

    if not os.path.exists(file_path):
        print(f"Error: file not found -> {file_path}")
        return None

    with open(file_path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            if len(parts) == 2:
                source, dest = parts
                weight = 1
            elif len(parts) == 3:
                source, dest, weight_text = parts
                try:
                    weight = float(weight_text)
                    if weight.is_integer():
                        weight = int(weight)
                except ValueError:
                    print(f"Skipping invalid weight on line {line_number}: {line}")
                    continue
            else:
                print(f"Skipping malformed line {line_number}: {line}")
                continue

            graph.add_edge(source, dest, weight)

    return graph


def build_trie_from_graph(graph):
    trie = Trie()
    for vertex in graph.get_vertices():
        trie.insert(vertex)
    return trie


def display_graph(graph):
    vertices = graph.get_vertices()
    if not vertices:
        print("The graph is empty.")
        return

    print("Adjacency List:")
    for vertex in vertices:
        neighbors = graph.get_neighbors(vertex)
        if neighbors:
            formatted = ", ".join([f"{neighbor}(w={weight})" for neighbor, weight in neighbors])
            print(f"{vertex}: {formatted}")
        else:
            print(f"{vertex}: no outgoing edges")


def main():
    print("COMP 251 - Network Exploration System")
    print("Uses adjacency list, BFS, DFS, hash map, heap, trie, and Dijkstra.")

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "data", "network.txt")
    graph = load_network(file_path)

    if graph is None:
        sys.exit(1)

    trie = build_trie_from_graph(graph)

    print(f"Loaded {len(graph.get_vertices())} vertices from data/network.txt")

    while True:
        print_separator()
        print("1. Display graph")
        print("2. BFS shortest path (unweighted)")
        print("3. DFS traversal")
        print("4. Dijkstra shortest path (weighted)")
        print("5. Check whether a node exists")
        print("6. Show neighbors of a node")
        print("7. Search nodes by prefix (Trie)")
        print("8. Exit")

        choice = prompt_user("Enter choice:")

        if choice == "1":
            display_graph(graph)

        elif choice == "2":
            start = prompt_user("Start node:")
            end = prompt_user("End node:")
            path = graph.bfs_shortest_path(start, end)
            if path is None:
                print("No path found, or one of the nodes does not exist.")
            else:
                print("BFS shortest path:", " -> ".join(path))

        elif choice == "3":
            start = prompt_user("Start node:")
            traversal = graph.dfs_traversal(start)
            if not traversal:
                print("Start node does not exist.")
            else:
                print("DFS traversal:", " -> ".join(traversal))

        elif choice == "4":
            start = prompt_user("Start node:")
            end = prompt_user("End node:")
            result = graph.dijkstra_shortest_path(start, end)
            if result is None:
                print("No weighted path found, or one of the nodes does not exist.")
            else:
                path, distance = result
                print("Dijkstra path:", " -> ".join(path))
                print("Total distance:", distance)

        elif choice == "5":
            node = prompt_user("Node name:")
            if graph.adj_list.contains(node):
                print(f"Node '{node}' exists in the graph.")
            else:
                print(f"Node '{node}' does not exist in the graph.")

        elif choice == "6":
            node = prompt_user("Node name:")
            if not graph.adj_list.contains(node):
                print(f"Node '{node}' does not exist in the graph.")
            else:
                neighbors = graph.get_neighbors(node)
                if not neighbors:
                    print(f"Node '{node}' has no outgoing edges.")
                else:
                    print(f"Neighbors of {node}:")
                    for neighbor, weight in neighbors:
                        print(f"- {neighbor} (weight = {weight})")

        elif choice == "7":
            prefix = prompt_user("Enter prefix:")
            matches = trie.words_with_prefix(prefix)
            if not matches:
                print("No nodes found with that prefix.")
            else:
                print("Matching nodes:", ", ".join(matches))

        elif choice == "8":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
