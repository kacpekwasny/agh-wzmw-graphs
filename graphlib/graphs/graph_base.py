from ..edges import edge
from ..nodes import node
from ..errors.errors import EdgeNotMemberOfGraphError, NodeNotFoundNodeError, NodeNotFoundNodeError
    

class GraphBase:
    def __init__(self) -> None:
        self.V: list[node.Node] = [] # vertecies / nodes
        self.E: list[edge.Edge] = [] # edges
        self.__last_inserted_node_id = 0 # increment +1 on every new Node


    def _add_node(self):
        """
        Create a node and append to graphs Vertices
            returns:
                (Node) the created node
        """
        n = node.Node(id_=self.__last_inserted_node_id+1)
        self.__last_inserted_node_id += 1
        self.V.append(n)
        return n

    def _remove_node(self, n: node.Node):
        """
        Remove node from Graph.V, destroy all of its edges, and remove from other nodes's neighbours.
        """
        if n not in self.V:
            raise NodeNotFoundNodeError
        self.V.remove(n)
        for e in self.E:
            e.disconnect_node(n)
        raise NotImplemented

    def _nodes_are_members(self, *nodes):
        """
        Raise a NodeNotFoundError when nodes are not members of the vertices of the graph.
            raises:
                NodeNotFoundError:  when nodes are not members of the vertices of the graph
        """
        for n in nodes:
            if n not in self.V:
                raise NodeNotFoundNodeError

    def _add_edge(self, edge: edge.Edge):
        self.E.append(edge)

    def _remove_edge(self, e: edge.Edge):
        """
        remove edge, and disconnect nodes
            params:
                e: SimpleEdege - edge to be removed from graph

            raises:
                GraphError:
                    - Edge not a member of this graph
        """
        if e in self.E:
            e._disconnect_all_nodes()
            self.E.remove(e)
            return
        
        raise EdgeNotMemberOfGraphError