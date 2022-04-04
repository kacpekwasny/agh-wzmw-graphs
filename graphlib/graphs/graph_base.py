from __future__ import annotations
from copy import deepcopy

from ..edges import edge
from ..nodes import node
from ..errors.errors import EdgeNotMemberOfGraphError, NodeNotFoundNodeError, NodeNotFoundNodeError
    

class GraphBase:
    def __init__(self) -> None:
        self.V: list[node.Node] = [] # vertecies / nodes
        self.E: list[edge.Edge] = [] # edges
        self.__last_inserted_node_id = -1 # increment +1 on every new Node
        self.__last_inserted_edge_id = -1

    def _add_node(self):
        """
        Create a node and append to graphs Vertices
            returns:
                (Node) the created node
        """
        n = node.Node(id_=self.__last_inserted_node_id + 1)
        self.__last_inserted_node_id += 1
        self.V.append(n)
        return n
    
    def _add_nodes(self, num):
        return [self._add_node() for _ in range(num)]

    def _remove_node(self, n: node.Node):
        """
        Remove node from Graph.V, destroy all of its edges, and remove from other nodes's neighbours.
        """
        if n not in self.V:
            raise NodeNotFoundNodeError
        self.V.remove(n)
        # for e in self.E:
        for e in n.edges:
            e._disconnect_node(n)

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
        edge.id = self.__last_inserted_edge_id + 1
        self.__last_inserted_edge_id += 1
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

    def get_nodes(self, *id_list: int) -> list[node.Node]:
        """
        Get node by id:
            params:
                id_: int - id of node
            
            returns:
                Node - node with specified id
            
            raises:
                IndexError when a node with specified id was not found
        """
        return [n for n in self.V if n.id in id_list]

    def get_edges(self, *id_list: int) -> list[edge.Edge]:
        """
        Get edge by id:
            params:
                id_: int - id of edge
            
            returns:
                Node - node with specified id
            
            raises:
                IndexError when a node with specified id was not found
        """
        return [e for e in self.E if e.id in id_list]

    def deepcopy(self):
        return deepcopy(self)

