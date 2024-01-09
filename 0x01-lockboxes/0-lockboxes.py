#!/usr/bin/python3
"""
Solving the lockboxes algorithm challenge
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes in a list can be opened

    Args:
        boxes (list): a multidimensional list of boxes
    """
    visited_boxes = set()

    def explore_boxes(box_index):
        """
        Traverses all the boxes by index
        """
        if box_index in visited_boxes:
            return
        visited_boxes.add(box_index)

        for key in boxes[box_index]:
            explore_boxes(key)

    explore_boxes(0)
    return len(visited_boxes) == len(boxes)
