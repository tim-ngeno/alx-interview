#!/usr/bin/python3
"""
Solving the lockboxes algorithm challenge
"""


# def canUnlockAll(boxes):
#     """
#     Determines if all boxes in a list can be opened

#     Args:
#         boxes (list): a multidimensional list of boxes
#     """
#     visited_boxes = set()

#     def explore_boxes(box_index):
#         """
#         Traverses all the boxes by index
#         """
#         if box_index in visited_boxes:
#             return
#         visited_boxes.add(box_index)

#         for key in boxes[box_index]:
#             explore_boxes(key)

#     explore_boxes(0)
#     return len(visited_boxes) == len(boxes)


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Parameters:
    - boxes (List[List[int]]): A list of lists where each inner list represents a box and contains keys to other boxes.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True  # The first box is always unlocked.

    stack = [0]  # Start with the first box.

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
