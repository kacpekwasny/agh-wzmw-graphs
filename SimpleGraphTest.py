import unittest
from libs.edges.simple_edge import SimpleEdge
from libs.errors.errors import EdgeAllreadyExistsinGraphError, GraphError

from libs.graphs.simple_graph import SimpleGraph

class TestSimpleFullGraph(unittest.TestCase):

    def setUp(self) -> None:
        nodes_num = 20
        sg = SimpleGraph()
        nodes = [sg.add_node() for _ in range(nodes_num)]
        c = nodes.pop()
        while nodes:
            for n in nodes:
                sg.connect_nodes(c, n)
            c = nodes.pop()

        self.nodes_num = nodes_num
        self.full_graph = sg

    def test_number_of_edges(self):
        self.assertEqual(len(self.full_graph.E), (self.nodes_num * (self.nodes_num - 1)) / 2,
            "fail if number of edges is different than LOUD predicts")

    def test_number_of_neighbours(self):
        for n in self.full_graph.V:
            self.assertEqual(len(n.neighbours), self.nodes_num - 1,
            f"fail if a node has different number of neighbours than {self.nodes_num-1=}")
    
    def test_disconnect_all_nodes(self):
        for e in self.full_graph.E[:]:
            self.full_graph.remove_edge(e)
        self.assertEqual(len(self.full_graph.E), 0, "should have removed all edges")
        
        for n in self.full_graph.V:
            self.assertEqual(n.num_neighbours, 0, "Node shouldnt have any neighbours left")

    def test_cannot_create_two_equal_edges(self):
        n1 = self.full_graph.add_node()
        n2 = self.full_graph.add_node()
        self.full_graph.connect_nodes(n1, n2)
        try:
            self.full_graph.connect_nodes(n2, n1)
        except GraphError:
            return
        self.assertEqual(1, 2, "It should not be possible to create two edges between two same nodes in a SimpleGraph.")

if __name__ == "__main__":
    unittest.main()