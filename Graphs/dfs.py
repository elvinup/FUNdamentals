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
        visited.append(vertex)
        #stack.extend([x for x in graph[vertex] if x not in visited and x not in stack]) #sexy list comp preserves order
        for x in graph[vertex]:
                    if x not in visited and x not in stack:
                        stack.append(x)
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
