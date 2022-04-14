
from ..graphs.two_nodes_edge_graph import TNEGraph
from ..nodes.node import Node
from ..errors.errors import CannotCreateLoopGraphError, EdgeAllreadyExistsinGraphError, EdgeNotMemberOfGraphError
from ..edges.directed_edge import DirectedEdge
from .graph_base import GraphBase

class DirectedGraph(TNEGraph):
    def __init__(self, *, multigraph=True, loops=False) -> None:
        self.multigraph = multigraph
        super().__init__(allow_multigraph=multigraph, allow_loops=loops)

    def connect_two_nodes(self, from_, to):
        """
        connect two nodes of this graph with a directed edge
        """
        return super().connect_two_nodes(from_, to, edge_cls=DirectedEdge)
    
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


        

