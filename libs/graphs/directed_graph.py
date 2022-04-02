
from ..nodes.node import Node
from ..errors.errors import EdgeAllreadyExistsinGraphError, EdgeNotMemberOfGraphError, NodesNotConnectedGraphError
from ..edges.directed_edge import DirectedEdge
from .graph_base import GraphBase

class DirectedGraph(GraphBase):
    def __init__(self, *, multigraph=True) -> None:
        self.multigraph = multigraph
        super().__init__()

    def connect_nodes(self, from_, to):
        """
        connect two nodes of this graph with a directed edge
        """
        new_e = DirectedEdge(from_, to)
        if not self.multigraph: # check if an edge like this allready exists
            for e in self.E:
                if new_e.equal_to(e):
                    raise EdgeAllreadyExistsinGraphError
        self.add_edge(new_e)
    
    def remove_edge(self, e: DirectedEdge):
        if e in self.E:    
            e.from_.neighbours.remove(e.to)
            e.to.neighbours.remove(e.from_)
            self.E.remove(e)
            return
        
        raise EdgeNotMemberOfGraphError
    
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
        if not to in from_.neighbours:
            return []
        return []
        

