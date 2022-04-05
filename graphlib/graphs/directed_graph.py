
from ..nodes.node import Node
from ..errors.errors import CannotCreateLoopGraphError, EdgeAllreadyExistsinGraphError, EdgeNotMemberOfGraphError
from ..edges.directed_edge import DirectedEdge
from .graph_base import GraphBase

class DirectedGraph(GraphBase):
    def __init__(self, *, multigraph=True) -> None:
        self.multigraph = multigraph
        super().__init__()

    def add_node(self):
        return super()._add_node()

    def add_nodes(self, num):
        return super()._add_nodes(num)

    def remove_node(self, n):
        super()._remove_node(n)

    def connect_nodes(self, from_, to):
        """
        connect two nodes of this graph with a directed edge
        """
        if from_ is to:
            raise CannotCreateLoopGraphError
        new_e = DirectedEdge(from_, to)
        if not self.multigraph: # check if an edge like this allready exists
            for e in self.E:
                if new_e.equal_to(e):
                    raise EdgeAllreadyExistsinGraphError
        self._add_edge(new_e)
    
    def remove_edge(self, e: DirectedEdge):
        if e not in self.E:    
            raise EdgeNotMemberOfGraphError
        e._disconnect_all_nodes()
        self.E.remove(e)
    
    def get_directed_edges(self, from_: Node, to: Node) -> list[DirectedEdge]:
        """
        get directed edges in direction from_ -> to
        between specified nodes

        params:
            from_:  Node
            to:     Node
        
        returns:
            list[DirectedEdge] - empty if none where found
        """
        if to not in from_._neighbours:
            return []
        e: DirectedEdge
        return [e for e in from_.edges if e.flow_possible(from_, to)]


        

