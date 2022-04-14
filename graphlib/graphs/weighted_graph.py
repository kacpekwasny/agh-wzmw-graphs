from graphlib.errors.errors import CannotCreateLoopGraphError, NodesAllreadyConnectedGraphError
from .two_nodes_edge_graph import TNEGraph
from ..nodes import node
from ..edges.weighted_edge import WeightedEdge

class WeightedGraph(TNEGraph):
    def __init__(self, *, allow_multigraph=True,
                          allow_loops=True,
                          default_weight=0,
                          default_flow=1,
                          default_capacity=1) -> None:

        self.E: list[WeightedEdge]
        super().__init__(allow_multigraph=allow_multigraph, allow_loops=allow_loops)

        self.default_weight = default_weight
        self.default_flow = default_flow
        self.default_capacity = default_capacity

    def connect_two_nodes(self, n1: node.Node, n2: node.Node, *,
                         weight=None, flow=None, capacity=None):
        if not self.allow_loops and n1 is n2:
            raise CannotCreateLoopGraphError

        weight = weight if weight is not None else self.default_weight
        flow = flow if flow is not None else self.default_flow
        capacity = capacity if capacity is not None else self.default_capacity
        
        new_e = WeightedEdge(self, n1, n2, weight=weight, flow=flow, capacity=capacity) 
        # Important, this type of graph, as edges uses WeightedEdge not the Edge class.
        
        for e in self.E:
            if not self.allow_multigraph and new_e.equal_to(e):
                new_e._disconnect_all_nodes()
                raise NodesAllreadyConnectedGraphError
        super().add_edges(new_e)
    

    