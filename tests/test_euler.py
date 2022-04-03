import unittest
import sys, os

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from graphlib.nodes.node import Node
from graphlib.edges.simple_edge import SimpleEdge
from graphlib.graphs.multigraph import Multigraph
from graphlib.algos import IsConnected

class TestMultiGraph(unittest.TestCase):

    def setUp(self) -> None:
        self.is_connected = IsConnected()
        return super().setUp()

    def create_cycle(self) -> None:
        nodes_num = 20
        G = Multigraph()
        nodes = [G.add_node() for _ in range(nodes_num)]
        
        for i, n in enumerate(nodes[:-1]):
            G.connect_nodes(n, G.V[i+1])
        G.connect_nodes(G.V[0], G.V[-1])

        self.nodes_num = nodes_num
        self.graph = G

    def create_double_cycle(self) -> None:
        nodes_num = 20
        G = Multigraph()
        nodes = [G.add_node() for _ in range(nodes_num)]
        
        for i, n in enumerate(nodes[:-1]):
            G.connect_nodes(n, G.V[i+1])
        G.connect_nodes(G.V[0], G.V[-1])

        self.nodes_num = nodes_num
        self.graph = G

    def create_path(self) -> None:
        nodes_num = 20
        G = Multigraph()
        nodes = [G.add_node() for _ in range(nodes_num)]
        
        for i, n in enumerate(nodes[:-1]):
            G.connect_nodes(n, G.V[i+1])
        self.nodes_num = nodes_num
        self.graph = G

    def create_unconnected_graph(self) -> None:
        self.graph = Multigraph()
        self.graph.add_node()
        self.graph.add_node()

    def create_unconnected_graph_big(self) -> None:
        self.graph = Multigraph()
        nodes = self.graph.add_nodes(100)
        self.graph.create_path(nodes[:50])
        self.graph.create_path(nodes[50:])

        

    def test_is_fully_connected(self):
        self.create_cycle()
        self.assertTrue(self.is_connected.solve(self.graph).return_value(), "Cycle graph should be determined as fully connected.")
        self.assertTrue(self.is_connected.solve(self.graph).return_value(), "Path graph should NOT be determined as fully connected.")

    def test_not_fully_connected(self):
        self.create_unconnected_graph()
        self.assertFalse(self.is_connected.solve(self.graph).return_value(), "Two separate nodes should be determined as unconnected.")
        self.create_unconnected_graph_big()
        self.assertFalse(self.is_connected.solve(self.graph).return_value(), "Two long chains but split in the middle should be determined as unconnected.")

    @unittest.skip
    def test_is_an_euler_graph(self):
        for f in [self.create_cycle, self.create_double_cycle]:
            f()
            self.assertEqual(is_euler(self.graph), True, f"{f.__name__=} So the graph should be determined as an euler graph.")
        
        self.create_path()
        self.assertEqual(is_euler(self.graph), False, "A path is not an euler graph.")            

    @unittest.skip
    def test_find_euler_path(self):
        self.create_cycle()
        found_path = find_euler_path(self.graph)
        edges = self.graph.E[:]
        prev_nodes = self.graph.V[:]
        for el in found_path:
            if type(el) is SimpleEdge:
                # check if previous edge and this one have a common neighbour
                found = False
                for n in el.nodes:
                    if n in prev_nodes:
                        found = True
                        break
                self.assertTrue(found, "This and previous edge have no common nodes.")
                prev_nodes = el.nodes[:]
                edges.remove(el)

            elif type(el) is not Node:
                raise TypeError(f"{type(el) = }")
        self.assertEqual(len(edges), 0, "All edges should have been used up.")
        

if __name__ == "__main__":
    unittest.main()


