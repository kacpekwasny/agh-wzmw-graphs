import unittest
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from graphlib.errors.errors import GraphError
from graphlib.graphs.multigraph import Multigraph

class TestMultiGraph(unittest.TestCase):

    def setUp(self) -> None:
        nodes_num = 20
        multigraph=False
        mg = Multigraph()
        nodes = mg.add_nodes(nodes_num)
        c = nodes.pop()
        while nodes:
            for n in nodes:
                mg.connect_two_nodes(c, n)
                mg.connect_two_nodes(n, c)
            c = nodes.pop()

        self.multigraph = multigraph
        self.nodes_num = nodes_num
        self.multigraph = mg

    def test_number_of_edges(self):
        self.assertEqual(len(self.multigraph.E), (self.nodes_num * (self.nodes_num - 1)),
            "fail if number of edges is different than LOUD predicts")

    def test_number_of_neighbours(self):
        for n in self.multigraph.V:
            self.assertEqual(len(n._neighbours), self.nodes_num - 1,
            f"fail if a node has different number of neighbours than {self.nodes_num-1=}")

    def test_disconnect_all_nodes(self):
        for e in self.multigraph.E[:]:
            self.multigraph.remove_edges(e)
        self.assertEqual(len(self.multigraph.E), 0, "should have removed all edges")

        for n in self.multigraph.V:
            self.assertEqual(n.num_neighbours, 0, "Node shouldnt have any neighbours left")
            self.assertEqual(len(n.edges), 0, "no edges shoud be left, as all were supposed to be disconnected from the node")

        # check if in Node._neighbours: { Node->int } values are all 0``
        for n in self.multigraph.V:
            neigh_sum = sum(n._neighbours.values())
            self.assertEqual(0, neigh_sum, "The multigraph shuld have been completely disconnected, and all neighbour values should've been 0.")

    def test_can_create_two_equal_edges(self):
        n1, n2 = self.multigraph.add_nodes(2)
        try:
            self.multigraph.connect_two_nodes(n2, n1)
            self.multigraph.connect_two_nodes(n2, n1)
        except GraphError:
            self.assertEqual(1, 2, "It should BE possible to create as many equal edges as one wants.")



if __name__ == "__main__":
    unittest.main()