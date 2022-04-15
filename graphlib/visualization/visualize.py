from __future__ import annotations

import pygame
from math import sin, cos, pi

from ..edges.simple_edge import SimpleEdge

from ..nodes.node import Node

from ..graphs.two_nodes_edge_graph import TNEGraph


class VisualizeGraph:
    def __init__(self, graph: TNEGraph) -> None:
        self.graph = graph
        self.x = 800
        self.y = 600
        self.window_size = (self.x, self.y)
        self.window_middle = (self.x/2, self.y/2)
        
        self.screen = None
        self.bg_color = (100, 100, 100)
        self.nc_radius = 200 # Node circle radius - nodes will be displayed on the perimeter of a circle with this radius
        self.angle_offest = 0
        self.reverse=False


        self.node_color = (0, 0, 200)
        self.node_radius = 10
        self.node_font_color = (250, 250, 0)

        self.edge_color = (0, 0, 0)
        self.edge_width = 1
        self.edge_font_color = (250, 250, 0)

    def pygame_init(self, *, font="Comic Sans MS", font_size=10):
        """
        Start pygame, window
        """
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont(font, font_size)
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.update()

    def update(self):
        pygame.display.update()

    def poll_events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit(0)

    def recalculate(self): 
        """
        Calculate coords for Nodes and set them: Node.xy = calculated_coord
        """
        num = len(self.graph.V)
        # going counter-clockwise from 3 o'clock
        rev = -1 if self.reverse else 1

        for i, n in enumerate(self.graph.V):
            if n.user_defined_cords:
                # the n.xy was set by user. Do not change it.
                continue
            new_x = int(cos(rev * (self.angle_offest + i * 2*pi/num)) * self.nc_radius)
            new_y = int(sin(rev * (self.angle_offest + i * 2*pi/num)) * self.nc_radius)
            n.xy = new_x, new_y


    def clear(self):
        """
        clear the window by overwriting everything with bg_color
        """
        self.screen.fill(self.bg_color)

    def draw_graph(self):
        """
        for every node and edge in graph draw them
        """
        self.clear()
        self.draw_edges()
        self.draw_nodes()
        self.update()

    def test_circle(self, xy):
        pygame.draw.circle(self.screen, (255, 255, 255), addcords(self.window_middle, xy), 20)

    def draw_edges(self):
        # TODO at least display nr of edges if not going to immplement isplaying multiple edeges between two nodes.
        for e in self.graph.E:
            xy1 = addcords(self.window_middle, e.n1.xy),
            xy2 = addcords(self.window_middle, e.n2.xy),
            pygame.draw.line(self.screen,
                            (e.color or self.edge_color),
                            xy1,
                            xy2,
                            (e.width or self.edge_width))
            if e.to_visualize != "":
                self.screen.blit(self.font.render(e.to_visualize, True, self.edge_font_color),
                                middlecords(xy1, xy2))

    def draw_nodes(self):
        for n in self.graph.V:
            xy = addcords(self.window_middle, n.xy)
            pygame.draw.circle(self.screen,
                            (n.color or self.node_color),
                            xy,
                            (n.radius or self.node_radius))
            if n.to_visualize != "":
                self.screen.blit(self.font.render(n.to_visualize, True, self.node_font_color), subtractcords(xy, self.node_radius))


    ### Methods for overwriting default CONFIG by chaining ###
    def set_size(self, x: int, y: int) -> VisualizeGraph:
        self.window_size = self.x, self.y = x, y
        self.window_middle = (self.x/2, self.y/2)
        return self

    def set_bg_color(self, rgb: tuple[int]) -> VisualizeGraph:
        self.bg_color = rgb
        return self
    
    def corrds_calc_ofset(self, *, reverse=False, angle_offset=0.0) -> VisualizeGraph:
        self.angle_offest = pi * angle_offset
        self.reverse = reverse
        return self

    ############
    ### Node ###
    def set_node_color(self, rgb: tuple[int]) -> VisualizeGraph:
        self.node_color = rgb
        return self

    def set_node_radius(self, r: int) -> VisualizeGraph:
        self.node_radius = r
        return self

    def set_node_font_color(self, rgb: tuple[int]) -> VisualizeGraph:
        self.node_font_color = rgb
        return self

    ############
    ### Edge ###
    def set_edge_color(self, rgb: tuple[int]) -> VisualizeGraph:
        self.edge_color = rgb
        return self

    def set_edge_width(self, w: int) -> VisualizeGraph:
        self.edge_width = w
        return self
    
    def set_edge_font_color(self, rgb: tuple[int]) -> VisualizeGraph:
        self.edge_font_color = rgb
        return self


    # def set_node_cords_generator_mode(self, mode: str | None) -> VisualizeGraph:
    #     """
    #     Automated generating coordinates for nodes.
    #         Nodes can be displayed in a circle
    #                             or in a square??
    #     """

def addcords(xy1, xy2):
    return xy1[0] + xy2[0], xy1[1] + xy2[1]

def middlecords(xy1, xy2):
    return (xy1[0] + xy2[0])/2, (xy1[1] + xy2[1])/2

def subtractcords(xy, val):
    return xy[0]-val, xy[1]-val