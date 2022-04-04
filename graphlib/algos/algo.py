from __future__ import annotations
# from ..graphs.graph_base import GraphBase

from typing import Any


class Algo:
    def __init__(self) -> None:
        self.visualization_state = {}
        """Keep here data that is important for visualization."""
        self.done = False
        
    def prepare(self):
        """
        Prepare eveything
        """
        raise NotImplementedError

    def next(self) -> bool:
        """
        Make move in algorithm
            returns:
                Algorithm has ended.
        """
        raise NotImplementedError


    def return_value(self) -> Any:
        raise NotImplementedError

    def solve(self, *args, **kwargs) -> Algo:
        """
        Run the algorithm from begging to end. Without stops for visualization.
        """
        self.prepare(*args, **kwargs)
        while self.next(): pass
        return self

    def visualize_data(self) -> dict:
        """
        Return dict of variables, that visualize the current state of the algorithm.
        One could simply access values by Object.field, but if we return all values that we consider meaningfull,
        it might be easier for somone to understand the algorithm and implement their own visualization. 
        self.visualization_state = {}
        """
        raise NotImplementedError

    def visualize(self):
        """
        Draw in pygame or turtle the current state.
        """
        raise NotImplementedError




    