def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
   
    visited.add(start)
    print(start, end=" ")  # Process the current vertex (e.g., print it)
   
    # Recursively visit all the adjacent vertices
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def create_graph():
    graph = {}
   
    num_nodes = int(input("Enter the number of nodes: "))
   
    # Adding nodes and their connections
    for _ in range(num_nodes):
        node = input("Enter the node name: ")
        neighbors = input(f"Enter the neighbors of {node} (space-separated): ").split()
        graph[node] = neighbors
   
    return graph

def main():
    graph = create_graph()
    start_node = input("Enter the starting node: ")
   
    print("\nDFS Traversal Order:")
    dfs(graph, start_node)

if __name__ == "__main__":
    main()
