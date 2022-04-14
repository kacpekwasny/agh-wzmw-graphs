import unittest
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from graphlib.graphs.weighted_graph import WeightedGraph


class TestSimpleFullGraph(unittest.TestCase):

    def setUp(self) -> None:
        nodes_num = 20
        wg = WeightedGraph(default_weight=5, default_flow=7, default_capacity=10)
        nodes = wg.add_nodes(nodes_num)
        c = nodes.pop()
        while nodes:
            for n in nodes:
                wg.connect_two_nodes(c, n)
            c = nodes.pop()

        self.nodes_num = nodes_num
        self.full_graph = wg

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

    def test_default_params(self):
        for e in self.full_graph.E:
            self.assertEqual(self.full_graph.default_capacity, e.capacity, "Capacity is not as the default one")
            self.assertEqual(self.full_graph.default_flow, e.flow, "Flow is not as the default one")
            self.assertEqual(self.full_graph.default_weight, e.weight, "Weight is not as the default one")


if __name__ == "__main__":
    unittest.main()