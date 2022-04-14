from __future__ import annotations
import pygame

from ..graphs.two_nodes_edge_graph import TNEGraph


class VisualizeGraph:
    def __init__(self, graph) -> None:
        self.graph = graph
        self.x = 800
        self.y = 600
        self.window_size = (self.x, self.y)
        self.bg_color = (200, 200, 200)
        self.screen = None


    def pygame_init(self):
        """
        Start pygame, window
        """
        pygame.init()
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.update()

    def clear(self):
        """
        clear the window by overwriting everything with bg_color
        """
        self.screen.fill(self.bg_color)

    def draw_graph(self):
        """
        for every node and edge in graph draw them
        """




    ### Methods for overwriting default CONFIG by chaining ###
    def set_size(self, x: int, y: int) -> VisualizeGraph:
        self.window_size = self.x, self.y = x, y
        return self

    def set_bg_color(self, rgb: tuple[int]) -> VisualizeGraph:
        self.bg_color = rgb
        return self

