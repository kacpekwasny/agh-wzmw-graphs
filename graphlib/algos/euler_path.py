import enum

from graphlib.edges.simple_edge import SimpleEdge

from ..nodes.node import Node
from ..edges.edge import Edge
from ..graphs.graph_base import GraphBase
from .algo import Algo
from .is_connected import IsConnected
from graphlib.edges import edge


class FindEulerPath(Algo):
    
    def prepare(self, graph: GraphBase):
        self.original_graph = graph
        self.graph = graph.deepcopy()
        self.edges = self.graph.E[:]
        self.edges_used: list[Edge] = []
        self.path: list[Edge, Node] = []
        self.current_node = self.graph.V[0]
        self.success = None

    def next(self) -> bool:
        """
        Run next cycle of algorithm.
        
        returns:
            bool:  <the algorithm is NOT completed> True for not completed, False for completed.
        """
        if len(self.graph.E) == 0:
            self.path.append(self.original_graph.get_nodes(self.current_node.id)[0])
            self.success = True
            return False

        # There are edges left, but the current node does not have any left <=> it is isolated, and we have no way to get back to the rest of the graph.
        # The graph is NOT an euler graph
        if len(self.current_node.edges) == 0:
            self.success = False
            return False

        edge_to_remove: Edge = None
        for e in self.current_node.edges:
            # check if the edge we will attempt to use is a bridge
            # TODO insted of creating a deep copy, remove the edge, check if is_connected, then <to be thought through, either added back, or not>
            g = self.graph.deepcopy()
            g._remove_edge(g.get_edges(e.id)[0])
            conn = IsConnected()
            if conn.solve(g).return_value():
                edge_to_remove = e
                break
        
        # Only an edge, that is a bridge is left, so we must take it, as there is no other left.
        if edge_to_remove is None:
            edge_to_remove = self.current_node.edges[0]
        self.old_node = self.current_node 
        self.path.append(self.original_graph.get_nodes(self.current_node.id)[0])
        self.path.append(self.original_graph.get_edges(edge_to_remove.id)[0])
        self.current_node = [n for n in edge_to_remove.nodes if n is not self.current_node][0]
        self.graph._remove_edge(edge_to_remove)
        self.edges_used.append(edge_to_remove)
        if len(self.old_node.edges) == 0:
            # this node is isolated, remove it, so it wont interfere with checking whether the graph is_connected
            self.graph._remove_nodes(self.old_node)
        return True

    def return_value(self) -> bool:
        return self.path

    def __str__(self) -> str:
        ret = ""
        for el in self.path:
            #if type(el) is SimpleEdge:
            #    ret += str(el)
            if type(el) is Node:
                ret += str(el.id)
            ret += " "

        return ret + "\b\b"
        