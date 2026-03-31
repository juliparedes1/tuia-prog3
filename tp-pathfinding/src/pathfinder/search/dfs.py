from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        frontier = StackFrontier()
        frontier.add(root)

        # Initialize expanded with the empty dictionary
        expanded = dict()

        if grid.objective_test(root.state):
                return Solution(root, expanded)

        # Initialize frontier with the root node
        # TODO Complete the rest!!
        # ...

        while True:
            if frontier.is_empty():
               return NoSolution(expanded)
             
            current_node = frontier.remove()

            if current_node.state in expanded:
                continue
            expanded[current_node.state] = True

            for action in grid.actions(current_node.state):  # iterate over current_node's possible actions
                 # get a new state for every action
                 new_state = grid.result(current_node.state, action)

                 if new_state not in expanded:
                    # create a new node with the new state
                    new_node = Node(
                         "",
                         state=new_state,
                         cost=current_node.cost + grid.individual_cost(current_node.state, action),
                         parent=current_node,
                         action=action
                    )

                    # check if new node contains objective state
                    if grid.objective_test(new_node.state):
                        return Solution(new_node, expanded)

                    # instert new node in frontier
                    frontier.add(new_node)
             
        return NoSolution(expanded)
