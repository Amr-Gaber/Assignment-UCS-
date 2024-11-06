import heapq

def uniform_cost_search(graph, start, goal):
    # Priority queue to store (cost, node, path) tuples
    priority_queue = [(0, start, [])]
    # Visited dictionary to keep track of the lowest cost to reach each node
    visited = {}

    while priority_queue:
        # Pop the element with the lowest cost
        cost, current, path = heapq.heappop(priority_queue)

        # Add the current node to the path
        path = path + [current]

        # Check if we reached the goal
        if current == goal:
            return cost, path

        # If the current node is not visited or found with a lower cost, process its neighbors
        if current not in visited or cost < visited[current]:
            visited[current] = cost

            # Go through all neighbors of the current node
            for neighbor, weight in graph.get(current, []):
                if neighbor not in visited or cost + weight < visited[neighbor]:
                    heapq.heappush(priority_queue, (cost + weight, neighbor, path))

    return float("inf"), []  # If goal is not reachable, return infinity and an empty path

# Example usage:
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

start = 'A'
goal = 'D'
cost, path = uniform_cost_search(graph, start, goal)
print(f"Cost: {cost}, Path: {path}")
