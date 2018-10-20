from collections import deque

def main():
    graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

    print("BFS: ", bfs(graph, 'A'))

def bfs(graph, start):
    visited =  []
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        visited.append(vertex)
        #queue.extend([x for x in graph[vertex] if x not in visited])
        for x in graph[vertex]:
            if x not in visited and x not in queue:
                queue.extend(x)

    return visited
main()
