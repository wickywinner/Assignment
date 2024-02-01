from typing import List

class Node:
    def __init__(self, val=None, children=None):
        """
        Initializes a Node for an N-ary tree.

        Args:
        - val (optional): The value of the node.
        - children (optional): A list of child nodes.
        """
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def createTree(self, serialization: List) -> Node:
        """
        Creates an N-ary tree from its level order traversal serialization.

        Args:
        - serialization: A list representing the level order traversal serialization.

        Returns:
        - Node: The root node of the created N-ary tree.
        """
        if not serialization:
            return None

        root = Node(val=serialization[0])
        stack = [root]
        i = 1

        while i < len(serialization) and stack:
            current = stack[-1]

            while i < len(serialization) and serialization[i] is not None:
                child = Node(val=serialization[i])
                current.children.append(child)
                stack.append(child)
                i += 1

            # Skip None values
            i += 1

            if i < len(serialization) and serialization[i] is None:
                stack.pop()

        return root

    def traverseTree(self, root: Node) -> List[int]:
        """
        Traverses an N-ary tree and returns the postorder traversal.

        Args:
        - root: The root node of the N-ary tree.

        Returns:
        - List[int]: The postorder traversal of the N-ary tree.
        """
        result = []

        def dfs(node):
            if node:
                for child in node.children:
                    dfs(child)
                result.append(node.val)

        dfs(root)
        return result

# Example usage
input_example_1 = [1, None, 3, 2, 4, None, 5, 6]
input_example_2 = [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14]

solution = Solution()

root_node_1 = solution.createTree(input_example_1)
traversal_result_1 = solution.traverseTree(root_node_1)
print("Traversal Output (Example 1):", traversal_result_1)

root_node_2 = solution.createTree(input_example_2)
traversal_result_2 = solution.traverseTree(root_node_2)
print("Traversal Output (Example 2):", traversal_result_2)
