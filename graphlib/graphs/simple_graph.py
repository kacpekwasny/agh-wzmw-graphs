from ..errors.errors import CannotCreateLoopGraphError, NodesAllreadyConnectedGraphError, NodesNotConnectedGraphError
from ..nodes import node
from ..edges import simple_edge as se
from .two_nodes_edge_graph import TNEGraph


class SimpleGraph(TNEGraph):

    def __init__(self) -> None:
        super().__init__(allow_multigraph=False, allow_loops=False)
