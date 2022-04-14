
from ..errors.errors import CannotCreateLoopGraphError, GraphError, NodesAllreadyConnectedGraphError, NodesNotConnectedGraphError
from ..nodes import node
from ..edges import simple_edge as se
from .graph_base import GraphBase


class TNEGraph(GraphBase):
    """
    This graph has edges that connect exactly two nodes.
    """

    def __init__(self, *, allow_multigraph=True, allow_loops=True) -> None:
        super().__init__()

        self.E: list[se.SimpleEdge] = []
        "Just to typehint better, because this type of Graph has for an edge a connection between exactly two nodes"
        self.allow_multigraph = allow_multigraph
        "When creating a new connection, check, does a connection like this allready exist?"
        self.allow_loops = allow_loops
        "When creatin a new connection, check, if the new edge will be a loop"

    def disconnect_nodes_from_edges(self, *nodes: node.Node):
        """
        Take nodes, and for every one, disconnect it from its edges.
        """
        for n in nodes:
            for e in n.edges:
                e._disconnect_all_nodes()

    def connect_two_nodes(self, n1: node.Node, n2: node.Node, *, edge_cls=se.SimpleEdge):
        """
        Create an edge between two nodes according to rules set by:
        self.allow_multigraph and self.allow_loops.
            raise:
                GraphError - when cannot create loop or when an edge allready exists
        """
        if not self.allow_loops and n1 is n2:
            raise CannotCreateLoopGraphError

        new_e = edge_cls(self, n1, n2) # Important, this type of graph, as edges uses SimpleEdge not the Edge class.
        for e in self.E:
            if not self.allow_multigraph and new_e.equal_to(e):
                new_e._disconnect_all_nodes()
                raise NodesAllreadyConnectedGraphError
        super().add_edges(new_e)

    def disconnect_nodes(self, n1: node.Node, n2: node.Node):
        """
        remove all edges that connect these two nodes.
        If nodes are not connected, nothing happens.
            params:
                n1, n2: Node
            raises:
                GraphError
                    - At least one node is not a memeber of graph
        """
        self._nodes_are_members(n1, n2)
        e: se.SimpleEdge
        for e in n1.edges:
            if (e.n1 == n1 and e.n2 == n2
             or e.n1 == n2 or e.n2 == n1):
                self.remove_edges(e)

    def create_path(self, *nodes: node.Node) -> None:
        """
        Create connections between subsequent nodes and thus create a path.
        If an edge between two nodes cannot be created, because it allready exists and an error was thrown
        It will be skipped and next
        """
        for i, n in enumerate(nodes[:-1]):
            try:
                self.connect_two_nodes(n, nodes[i+1])
            except GraphError:
                continue
