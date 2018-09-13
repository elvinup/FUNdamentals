def main():
    graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

    print("Stack: ", dfsStack(graph, 'A'))
    print("Recursion: ", dfsRecursion(graph, 'A'))

def dfsStack(graph, start):
    visited =  []
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend([x for x in graph[vertex] if x not in visited]) #sexy list comp preserves order
            #stack.extend(graph[vertex]-set(visited))
    return visited

def dfsRecursion(graph, start, visited=None):
    if visited is None:
        visited = []

    if start not in visited:
        visited.append(start)
    explore = [x for x in graph[start] if x not in visited]
    for next in explore:
        dfsRecursion(graph, next, visited)
    return visited
main()
