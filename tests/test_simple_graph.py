import unittest
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from graphlib.errors.errors import GraphError
from graphlib.graphs.simple_graph import SimpleGraph

# import logging
# formatter = logging.Formatter('[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s','%m-%d %H:%M:%S')
# c_handler = logging.StreamHandler()
# lgr = logging.getLogger("custom logger")
# lgr.addHandler(c_handler)
# lgr.setLevel(10)

class TestSimpleFullGraph(unittest.TestCase):

    def setUp(self) -> None:
        nodes_num = 20
        sg = SimpleGraph()
        nodes = sg.add_nodes(nodes_num)
        c = nodes.pop()
        while nodes:
            for n in nodes:
                sg.connect_two_nodes(c, n)
            c = nodes.pop()

        self.nodes_num = nodes_num
        self.full_graph = sg

    def test_number_of_edges(self):
        self.assertEqual(len(self.full_graph.E), (self.nodes_num * (self.nodes_num - 1)) / 2,
            "fail if number of edges is different than LOUD predicts")

    def test_number_of_neighbours(self):
        for n in self.full_graph.V:
            self.assertEqual(len(n._neighbours), self.nodes_num - 1,
            f"fail if a node has different number of neighbours than {self.nodes_num-1=}")
    
    def test_disconnect_all_nodes(self):
        for e in self.full_graph.E[:]:
            self.full_graph.remove_edges(e)
        self.assertEqual(len(self.full_graph.E), 0, "should have removed all edges")
        
        for n in self.full_graph.V:
            self.assertEqual(n.num_neighbours, 0, "Node shouldnt have any neighbours left")
            self.assertEqual(len(n.edges), 0, "no edges shoud be left, as all were supposed to be disconnected from the node")

        # check if in Node._neighbours: { Node->int } values are all 0``
        for n in self.full_graph.V:
            neigh_sum = sum(n._neighbours.values())
            self.assertEqual(0, neigh_sum, "The full_graph shuld have been completely disconnected, and all neighbour values should've been 0.")

    def test_cannot_create_two_equal_edges(self):
        n1, n2 = self.full_graph.add_nodes(2)
        self.full_graph.connect_two_nodes(n1, n2)
        try:
            self.full_graph.connect_two_nodes(n2, n1)
        except GraphError:
            return
        self.assertEqual(1, 2, "It should not be possible to create two edges between two same nodes in a SimpleGraph.")

    def test_cannot_create_loop(self):
        [n1] = self.full_graph.add_nodes(1)
        try:
            self.full_graph.connect_two_nodes(n1, n1)
        except GraphError:
            return
        self.assertEqual(1, 2, "It should NOT be possible to create an edge loop (connect n1 to n1).")



if __name__ == "__main__":
    unittest.main()