import unittest
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from graphlib.graphs.two_nodes_edge_graph import TNEGraph
from graphlib.visualization.visualize import VisualizeGraph
from graphlib.graphs.weighted_graph import WeightedGraph

from graphlib.algos.euler_path import FindEulerPath


class TestSimpleFullGraph(unittest.TestCase):

    def setUp(self, *, nodes_num = 20) -> None:
        wg = WeightedGraph(default_weight=5, default_flow=7, default_capacity=10)
        nodes = wg.add_nodes(nodes_num)
        c = nodes.pop()
        while nodes:
            for n in nodes:
                wg.connect_two_nodes(c, n)
            c = nodes.pop()

        self.nodes_num = nodes_num
        self.full_graph = wg

    @unittest.skip
    def test_1(self):
        v = VisualizeGraph(self.full_graph)
        v.pygame_init()
        v.recalculate()
        v.clear()
        v.draw_graph()

    @unittest.skip
    def test_2(self):
        g = TNEGraph()
        n0, n1, n2, n3 = g.add_nodes(4)
        g.add_nodes(1)
        for n in g.V:
            n.to_visualize = f"n{n.id}"

    
        g.create_path(n0, n1, n2, n3)
        g.connect_two_nodes(n1, n3)
        v = VisualizeGraph(g)\
            .corrds_calc_ofset(reverse=True, angle_offset=1.25)

        v.pygame_init(font_size=15)
        v.recalculate()
        v.draw_graph()
        v.update()

        while True: v.poll_events()

    #@unittest.skip
    def test_euler_path_visualization(self):
        self.setUp(nodes_num=5)
        fep = FindEulerPath()
        fep.prepare(self.full_graph)
        fep.visualize()


if __name__ == "__main__":
    unittest.main()