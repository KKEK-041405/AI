from collections import deque

def bfs(graph, start):
    visited = set()         # Set to keep track of visited nodes
    queue = deque([start])  # Initialize a queue with the start node
    visited.add(start)      # Mark the start node as visited
   
    while queue:
        vertex = queue.popleft()  # Dequeue a vertex from the front of the queue
        print(vertex, end=" ")    # Process the current vertex (e.g., print it)
       
        # Iterate over all the adjacent vertices of the dequeued vertex
        for neighbor in graph[vertex]:
            if neighbor not in visited:     # If the neighbor has not been visited
                visited.add(neighbor)       # Mark it as visited
                queue.append(neighbor)      # Enqueue the neighbor

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
   
    print("\nBFS Traversal Order:")
    bfs(graph, start_node)

if __name__ == "__main__":
    main()
