from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # frontier
        frontier = PriorityQueueFrontier()
        frontier.add(root, root.cost + grid.manhattan(root.state))

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        if grid.objective_test(root.state):
                return Solution(root, reached)

        while True:

            if frontier.is_empty():
                return NoSolution(reached)
            
            current_node = frontier.pop()  # take node out from the frontier for further expansion

            # check if new node contains objective state
            if grid.objective_test(current_node.state):
                return Solution(current_node, reached)

            for action in grid.actions(current_node.state):  # iterate over current_node's possible actions
                 # get a new state for every action
                 new_state = grid.result(current_node.state, action)
                 new_cost = current_node.cost + grid.individual_cost(current_node.state, action)
                 
                 if new_state not in reached or new_cost < reached[new_state]:
                    # create a new node with the new state
                    new_node = Node(
                         "",
                         state=new_state,
                         cost=new_cost,
                         parent=current_node,
                         action=action
                    )

                    
                    
                    # instert new state in reached dict
                    reached[new_node.state] = new_cost

                    # instert new node in frontier
                    frontier.add(new_node, new_node.cost + grid.manhattan(new_node.state))

        return NoSolution(reached)

