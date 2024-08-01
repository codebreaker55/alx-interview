#!/usr/bin/python3
"""method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """
    function that determine if all the boxes can be opened
    boxes is a list of lists
    assume all keys will be positive integers
    There can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
    """
    if not boxes or type(boxes) is not list:
        return False

    else:
        box_unlocked = [0]
        for n in box_unlocked:
            for key in boxes[n]:
                if key not in box_unlocked and key < len(boxes):
                    box_unlocked.append(key)
        if len(box_unlocked) == len(boxes):
            return True
        return False
