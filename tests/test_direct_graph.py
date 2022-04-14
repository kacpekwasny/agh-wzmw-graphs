import unittest
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from graphlib.errors.errors import GraphError
from graphlib.graphs.directed_graph import DirectedGraph

class TestDirectGraph(unittest.TestCase):

    def setUp(self) -> None:
        nodes_num = 20
        multigraph=False
        dg = DirectedGraph(multigraph=multigraph)
        nodes = dg.add_nodes(nodes_num)

        # fully connected graph
        for n in nodes:
            for n1 in nodes:
                if n is n1: continue
                dg.connect_two_nodes(n, n1)

        self.multigraph = multigraph
        self.nodes_num = nodes_num
        self.digraph = dg

    def test_number_of_edges(self):
        # expecting a double full graph: there are two edges between any two nodes
        self.assertEqual(len(self.digraph.E), (self.nodes_num * (self.nodes_num - 1)),
            "fail if number of edges is different than LOUD predicts")

    def test_number_of_neighbours(self):
        for n in self.digraph.V:
            self.assertEqual(len(n._neighbours), self.nodes_num - 1,
            f"fail if a node has different number of neighbours than {self.nodes_num-1=}")

    def test_disconnect_all_nodes(self):
        for e in self.digraph.E[:]:
            self.digraph.remove_edges(e)
        self.assertEqual(len(self.digraph.E), 0, "should have removed all edges")

        
        for n in self.digraph.V:
            self.assertEqual(n.num_neighbours, 0, "Node shouldnt have any neighbours left")
            self.assertEqual(len(n.edges), 0, "no edges shoud be left, as all were supposed to be disconnected from the node")

        # check if in Node._neighbours: { Node->int } values are all 0``
        for n in self.digraph.V:
            neigh_sum = sum(n._neighbours.values())
            self.assertEqual(0, neigh_sum, "The digraph shuld have been completely disconnected, and all neighbour values should've been 0.")

    def test_flow(self):
        for n1 in self.digraph.V:
            for n2 in self.digraph.V:
                if n1 is n2:
                    continue
                self.assertEqual(len(self.digraph.get_directed_edges(n1, n2)),
                                 1,
                                 "Should be only one directional edge connecting these two nodes.")

    def test_cannot_create_two_equal_edges(self):
        n1, n2 = self.digraph.add_nodes(2)
        try:
            self.digraph.connect_two_nodes(n2, n1)
            self.digraph.connect_two_nodes(n2, n1)
        except GraphError:
            self.assertFalse(self.multigraph, "It should BE possible to create as many equal edges as one wants.")
            return
        self.assertTrue(self.multigraph, "It should NOT BE possible to create two edges between two same nodes with same direction.")

    def test_cannot_create_loop(self):
        [n1] = self.digraph.add_nodes(1)
        try:
            self.digraph.connect_two_nodes(n1, n1)
        except GraphError:
            self.assertFalse(self.multigraph, "It should BE possible to create an edge loop (connect n1 to n1).")
            return
        self.assertTrue(self.multigraph, "It should NOT be possible to create an edge loop (connect n1 to n1).")


if __name__ == "__main__":
    unittest.main()