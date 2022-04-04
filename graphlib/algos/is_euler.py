from ..graphs.graph_base import GraphBase
from .algo import Algo
from .is_connected import IsConnected


class IsEuler(Algo):
    
    def prepare(self, graph: GraphBase):
        self.done = False
        self.nodes_have_even_edges = False
        self.nodes_are_connected = False
        self.visualization_state = {}
        self.graph = graph
        self.is_connected = IsConnected()
        self.is_connected.prepare(self.graph)
        self.visualization_state["is_connected"] = self.is_connected.visualization_state
        # dict is mutable, so this is a refernce, and there is no need to update it any more, as it will
        # be done automatically 
        
        self.nodes_check_edges = self.graph.V[:]
        """ nodes to be checked if they have an even number of edges """
        self.checked_even_num_edges = False
        """ set to True when next is supposed to switch from checking if all nodes have even number of nodes """

    def next(self) -> bool:
        """
        Run next cycle of algorithm.
        
        returns:
            bool:  <the algorithm is NOT completed> True for not ready, False for ready.
        """
        if not self.checked_even_num_edges:
            n = self.nodes_check_edges.pop(0)
            if len(n.edges) % 2 != 0:
                self.done = True
                self.nodes_have_even_edges = False
                # a node has an uneven number of edges
                return False
            self.checked_even_num_edges = len(self.nodes_check_edges) == 0
            return True
        self.nodes_are_connected = True
        
        # All nodes have an even number of edges.
        # so now check if all nodes are connected.
        self.done = not self.is_connected.next()
        return not self.done

    def return_value(self) -> bool:
        return self.nodes_are_connected and self.is_connected.return_value()


