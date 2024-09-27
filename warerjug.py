from collections import deque

def water_jug_solver(capacity1, capacity2, initial_amount1, initial_amount2, goal_amount1, goal_amount2):
    def get_neighbors(state):
        a, b = state
        neighbors = []
        
        # Fill Jug 1
        neighbors.append((capacity1, b))
        
        # Fill Jug 2
        neighbors.append((a, capacity2))
        
        # Empty Jug 1
        neighbors.append((0, b))
        
        # Empty Jug 2
        neighbors.append((a, 0))
        
        # Pour Jug 1 into Jug 2
        pour1_to_2 = min(a, capacity2 - b)
        neighbors.append((a - pour1_to_2, b + pour1_to_2))
        
        # Pour Jug 2 into Jug 1
        pour2_to_1 = min(b, capacity1 - a)
        neighbors.append((a + pour2_to_1, b - pour2_to_1))
        
        return neighbors

    def bfs():
        queue = deque([((initial_amount1, initial_amount2), [])])  # (state, path)
        visited = set()
        visited.add((initial_amount1, initial_amount2))
        solutions = []

        while queue:
            (current_state, path) = queue.popleft()
            a, b = current_state
            
            # Check if either jug has the goal amount
            if a == goal_amount1 and b == goal_amount2:
                solutions.append(path + [current_state])
            
            # Explore all possible next states
            for neighbor in get_neighbors(current_state):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [current_state]))

        return solutions

    # Run BFS to find all possible solutions
    solutions = bfs()
    if solutions:
        print("Possible ways to reach the goal:")
        for i, solution in enumerate(solutions):
            print(f"Solution {i+1}:")
            for step in solution:
                print(f"({step[0]}, {step[1]})")
            print()
    else:
        print("No possible way to reach the goal.")

# User Input
def main():
    # Collect user input for jug capacities, initial amounts, and goal amounts
    capacity1 = int(input("Enter the capacity of jug 1: "))
    capacity2 = int(input("Enter the capacity of jug 2: "))
    initial_amount1 = int(input("Enter the initial amount of water in jug 1: "))
    initial_amount2 = int(input("Enter the initial amount of water in jug 2: "))
    goal_amount1 = int(input("Enter the goal amount of water in jug 1: "))
    goal_amount2 = int(input("Enter the goal amount of water in jug 2: "))

    # Validate input
    if (initial_amount1 > capacity1 or initial_amount2 > capacity2 or 
        goal_amount1 > capacity1 or goal_amount2 > capacity2):
        print("Invalid input: Amounts exceed jug capacities.")
        return

    # Solve the problem and output the results
    water_jug_solver(capacity1, capacity2, initial_amount1, initial_amount2, goal_amount1, goal_amount2)

if __name__ == "__main__":
    main()

