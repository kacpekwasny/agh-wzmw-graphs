
class GraphError(Exception):pass
NodeNotMemberOfGraphError = GraphError("Node is not a member of this graph / id was not found")
EdgeNotMemberOfGraphError = GraphError("Edge is not a member of this graph / id was not found")

EdgeAllreadyExistsinGraphError = GraphError("Edge allready exists in graph")
NodesNotConnectedGraphError = GraphError("Nodes are not connected")
NodesAllreadyConnectedGraphError = GraphError("Those two nodes are allready connected")

CannotCreateLoopGraphError = GraphError("It is not allowed to create an edge from N1 to N1")
NotMultigraphGraphError = GraphError("This graph is not a multigraph, and thus doesn't allow this type of edge")
NoNodesGraphError = GraphError("This graph has no nodes")


class NodeError(Exception):pass
NodeMissingIdNodeError = NodeError("No id was passed")
WrongGraphParentNodeError = NodeError("Cannot add a node with different graph parent as neighbour")
EdgeNotFoundNodeError = NodeError("Edge has not been found in edges of this node")


class EdgeError(Exception):pass
NodeNotMemberOfEdgeError = EdgeError("Node is not a member of edge")


