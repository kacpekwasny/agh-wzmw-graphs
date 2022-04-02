import unittest
from graphlib.edges.directed_edge import DirectedEdge
from graphlib.errors.errors import EdgeAllreadyExistsinGraphError, GraphError
import inspect

from graphlib.graphs.directed_graph import DirectedGraph

class TestDirectGraph(unittest.TestCase):

    def setUp(self) -> None:
        nodes_num = 20
        multigraph=False
        dg = DirectedGraph(multigraph=multigraph)
        nodes = [dg.add_node() for _ in range(nodes_num)]
        c = nodes.pop()
        while nodes:
            for n in nodes:
                dg.connect_nodes(c, n)
                dg.connect_nodes(n, c)
            c = nodes.pop()

        self.multigraph = multigraph
        self.nodes_num = nodes_num
        self.digraph = dg

    def test_number_of_edges(self):
        self.assertEqual(len(self.digraph.E), (self.nodes_num * (self.nodes_num - 1)),
            "fail if number of edges is different than LOUD predicts")

    def test_number_of_neighbours(self):
        for n in self.digraph.V:
            self.assertEqual(len(n.neighbours), self.nodes_num - 1,
            f"fail if a node has different number of neighbours than {self.nodes_num-1=}")

    def test_disconnect_all_nodes(self):
        for e in self.digraph.E[:]:
            self.digraph.remove_edge(e)
        self.assertEqual(len(self.digraph.E), 0, "should have removed all edges")

        
        for n in self.digraph.V:
            self.assertEqual(n.num_neighbours, 0, "Node shouldnt have any neighbours left")
            self.assertEqual(len(n.edges), 0, "no edges shoud be left, as all were supposed to be disconnected from the node")

        # check if in Node.neighbours: { Node->int } values are all 0``
        for n in self.digraph.V:
            neigh_sum = sum(n.neighbours.values())
            self.assertEqual(0, neigh_sum, "The digraph shuld have been completely disconnected, and all neighbour values should've been 0.")

    def test_flow(self):
        for n1 in self.digraph.V:
            for n2 in self.digraph.V:
                if n1 is n2:
                    continue
                self.assertEqual(len(self.digraph.get_directed_edges(n1, n2)), 1, "Should be only one directional edge connecting these two nodes.")



    def test_cannot_create_two_equal_edges(self):
        n1 = self.digraph.add_node()
        n2 = self.digraph.add_node()
        try:
            self.digraph.connect_nodes(n2, n1)
            self.digraph.connect_nodes(n2, n1)
        except GraphError:
            if self.multigraph:
                self.assertEqual(1, 2, "It should BE possible to create as many equal edges as one wants.")
            return
        if not self.multigraph:
            self.assertEqual(1, 2, "It should NOT BE possible to create two edges between two same nodes with same direction.")



if __name__ == "__main__":
    unittest.main()