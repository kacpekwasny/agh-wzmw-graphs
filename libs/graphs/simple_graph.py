from ..errors.errors import EdgeNotMemberOfGraphError, NodesAllreadyConnectedGraphError, NodesNotConnectedGraphError
from ..nodes import node
from ..edges import simple_edge as se
from .graph_base import GraphBase


class SimpleGraph(GraphBase):
    def __init__(self) -> None:
        super().__init__()

    def add_node(self):
        return super().add_node()

    def connect_nodes(self, n1: node.Node, n2: node.Node):
        new_e = se.SimpleEdge(n1, n2)
        for e in self.E:
            if new_e.equal_to(e):
                raise NodesAllreadyConnectedGraphError
        super().add_edge(new_e)
    
    def remove_edge(self, e: se.SimpleEdge):
        """
        remove edge, and disconnect nodes
            params:
                e: SimpleEdege - edge to be removed from graph

            raises:
                GraphError:
                    - Edge not a member of this graph
        """
        if e in self.E:    
            e.destroy()
            self.E.remove(e)
            return
        
        raise EdgeNotMemberOfGraphError

    def disconnect_nodes(self, n1: node.Node, n2: node.Node):
        """
        remove edge if nodes connected
            params:
                n1, n2: Node

            raises:
                GraphError
                    - At least one node is not a memeber of graph
                    - Nodes are not connected
        """
        self.nodes_are_members(n1, n2)
        e: se.SimpleEdge
        for e in self.E:
            if (e.n1 == n1 and e.n2 == n2
             or e.n1 == n2 or e.n2 == n1):
                self.remove_edge(e)
                return
        raise NodesNotConnectedGraphError
