from ..edges import Edge
from ..errors import NodeError
from ..nodes import Node

class GraphBase:
    def __init__(self) -> None:
        self.V = [] # vertecies / nodes
        self.E = [] # edges
        self.__last_inserted_node_id = 0 # increment +1 on every new Node


    """
    Create a node and append to graphs Vertices
        returns:
            (Node) the created node
    """
    def add_node(self):
        n = Node(id=self.__last_inserted_node_id+1)
        self.last_inserted_node_id += 1
        self.V.append(n)
        return n

    """
    Remove node from Graph.V, destroy all of its edges, and remove from other nodes's neighbours.
    """    
    def remove_node(self):
        raise NotImplemented

    def nodes_are_members(self, *nodes):
        for n in nodes:
            if n not in self.V:
                raise NodeError(f"At least one Node was not found in vertices {n1=}; {n2=}")

    """
    Create an edge, that connects any number of nodes.
        params:
            nodes:          List[Node]                  - any number of nodes, depending on the child class is supposed to implement restrictions for its specific graph type
            new_edge_func:  lambda List[Node]: [Edge]   - function that will take nodes and return an Child of Edge type, it allows for the child class to implement using specific Edge subclass or smthing

        raises:
            NotImplementedError:    when new_edge_func is not passed
            NodeError:              when nodes are not members of the vertices of the graph

        returns:
            [Edge] the created edge
    """
    def connect_nodes(self, *nodes, new_edge_func=None):
        if new_edge_func is None:
            raise NotImplementedError("new_edge_func is None.")
        self.nodes_are_members(*nodes)
        e = Edge(*nodes)
        self.E.append(e)
        return e

