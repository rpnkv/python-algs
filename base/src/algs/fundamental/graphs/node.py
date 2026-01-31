# Definition for a Node.
from typing import Tuple, Self


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __eq__(self, value, /):
        return False

    @staticmethod
    def build(vertices: list[int], edges: list[Tuple[int, int]]) -> Self:
        raise NotImplementedfiu
