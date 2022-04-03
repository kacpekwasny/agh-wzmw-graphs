
class NodeError(Exception):pass
NodeNotFoundNodeError = NodeError(f"At least one Node was not found in graph's vertices.")
NodeMissingIdNodeError = NodeError("No id was passed")
WrongGraphParentNodeError = NodeError("Cannot add a node with different graph parent as neighbour")
EdgeNotFoundNodeError = NodeError("Edge has not been found in edges of this node")

class GraphError(Exception):pass
EdgeAllreadyExistsinGraphError = GraphError("Edge allready exists in graph.")
NodesAllreadyConnectedGraphError = GraphError("Those two nodes are allready connected")
EdgeNotMemberOfGraphError = GraphError("Edge not a member of this graph")
NodesNotConnectedGraphError = GraphError("Nodes are not connected")
CannotCreateLoopGraphError = GraphError("It is not allowed to create an edge from N1 to N1.")
NoNodesGraphError = GraphError("This graph has no nodes.")

class EdgeError(Exception):pass
NodeNotMemberOfEdgeError = EdgeError("Node is not a member of edge")


