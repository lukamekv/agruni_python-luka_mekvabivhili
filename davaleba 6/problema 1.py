from collections import deque


def has_path(graph, start, end):
    if start not in graph or end not in graph:
        return False
    if start == end:
        return True

    visited = set()
    queue = deque([start])

    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)

        for neighbor in graph.get(current, []):
            if neighbor == end:
                return True
            if neighbor not in visited:
                queue.append(neighbor)

    return False

large_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'F'],
    'C': ['E'],
    'D': ['G'],
    'E': ['H'],
    'F': ['G'],
    'G': [],
    'H': ['I'],
    'I': [],
    'J': ['K'],
    'K': []
}

print(has_path(large_graph, 'A', 'G'))
print(has_path(large_graph, 'C', 'H'))
print(has_path(large_graph, 'A', 'I'))
print(has_path(large_graph, 'B', 'E'))
print(has_path(large_graph, 'J', 'K'))
print(has_path(large_graph, 'A', 'J'))
print(has_path(large_graph, 'G', 'A'))
print(has_path(large_graph, 'A', 'A'))  