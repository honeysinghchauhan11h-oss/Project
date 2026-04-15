from hashmap import HashMap
from heap import MinHeap


class Graph:
    """
    Graph implemented with an adjacency list.
    Space complexity: O(V + E)
    """

    def __init__(self):
        self.adj_list = HashMap()

    def add_vertex(self, vertex):
        if not self.adj_list.contains(vertex):
            self.adj_list.put(vertex, [])

    def add_edge(self, source, dest, weight=1):
        self.add_vertex(source)
        self.add_vertex(dest)

        neighbors = self.adj_list.get(source)
        for i, (neighbor, _) in enumerate(neighbors):
            if neighbor == dest:
                neighbors[i] = (dest, weight)
                return
        neighbors.append((dest, weight))

    def get_neighbors(self, vertex):
        neighbors = self.adj_list.get(vertex)
        return neighbors if neighbors is not None else []

    def get_vertices(self):
        return self.adj_list.keys()

    def bfs_shortest_path(self, start, end):
        """
        Breadth-First Search shortest path for unweighted graphs.
        Time complexity: O(V + E)
        """
        if not self.adj_list.contains(start) or not self.adj_list.contains(end):
            return None

        visited = HashMap()
        queue = [(start, [start])]
        front = 0
        visited.put(start, True)

        while front < len(queue):
            current, path = queue[front]
            front += 1

            if current == end:
                return path

            for neighbor, _ in self.get_neighbors(current):
                if not visited.contains(neighbor):
                    visited.put(neighbor, True)
                    queue.append((neighbor, path + [neighbor]))

        return None

    def dfs_traversal(self, start):
        """
        Depth-First Search traversal.
        Time complexity: O(V + E)
        """
        if not self.adj_list.contains(start):
            return []

        visited = HashMap()
        order = []

        def dfs(vertex):
            visited.put(vertex, True)
            order.append(vertex)
            for neighbor, _ in self.get_neighbors(vertex):
                if not visited.contains(neighbor):
                    dfs(neighbor)

        dfs(start)
        return order

    def is_connected(self, start, target):
        return self.bfs_shortest_path(start, target) is not None

    def dijkstra_shortest_path(self, start, end):
        """
        Dijkstra's algorithm for weighted shortest path.
        Time complexity: O((V + E) log V) with a min-heap.
        """
        if not self.adj_list.contains(start) or not self.adj_list.contains(end):
            return None

        distances = HashMap()
        previous = HashMap()
        visited = HashMap()
        heap = MinHeap()

        for vertex in self.get_vertices():
            distances.put(vertex, float("inf"))
            previous.put(vertex, None)

        distances.put(start, 0)
        heap.insert(0, start)

        while not heap.is_empty():
            current_distance, current_vertex = heap.extract_min()

            if visited.contains(current_vertex):
                continue
            visited.put(current_vertex, True)

            if current_vertex == end:
                break

            for neighbor, weight in self.get_neighbors(current_vertex):
                if visited.contains(neighbor):
                    continue

                new_distance = current_distance + weight
                old_distance = distances.get(neighbor)

                if new_distance < old_distance:
                    distances.put(neighbor, new_distance)
                    previous.put(neighbor, current_vertex)
                    heap.insert(new_distance, neighbor)

        if distances.get(end) == float("inf"):
            return None

        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous.get(current)
        path.reverse()

        return path, distances.get(end)
