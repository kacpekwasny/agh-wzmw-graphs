from __future__ import annotations
from copy import deepcopy

from ..edges import edge
from ..nodes import node
from ..errors.errors import EdgeNotMemberOfGraphError, NodeNotMemberOfGraphError

from ..funcs import inherit_docstring

class GraphBase:
    def __init__(self) -> None:
        self.V: list[node.Node] = [] # vertecies / nodes
        self.E: list[edge.Edge] = [] # edges
        self.__last_inserted_node_id = -1 # increment +1 on every new Node
        self.__last_inserted_edge_id = -1
    
    def __create_node(self) -> node.Node:
        """
        Create a node and append to graphs Vertices
            returns:
                (Node) the created node
        """
        n = node.Node(self, id_=self.__last_inserted_node_id + 1)
        self.__last_inserted_node_id += 1
        self.V.append(n)
        return n

    # Do NOT overwrite _func methods (methods starting with underscore) in child classes
    # in case a grandchild wants to have its own wrapper around the _func
    # overwrite the proxy method named func instead.

    # Add
    def _add_nodes(self, num: int)  -> list[node.Node]:
        """
        Create as many nodes as specified in the `num` argument.
            returns list of newly created node.Node objects, that live in Graph.V.
        """
        return [self.__create_node() for _ in range(num)]

    def _add_edges(self, *edges: edge.Edge):
        """
        append edges to self.E and increment self.last_increment_id
        """
        for edge in edges:
            self.__last_inserted_edge_id += 1
            edge.id = self.__last_inserted_edge_id
            self.E.append(edge)


    # Get
    def _get_nodes(self, *ids: int) -> list[node.Node]:
        """
        get nodes with the mathing id in same order as the ids passed.
            raises:
                NodeError - when at least one id was not found
            retuns:
                list[node.Node]
        """
        ids: list[int] = list(ids)
        ret: list[node.Node] = [] # list of requested nodes
        for id_ in ids[:]:
            for n in self.V:
                if n.id == id_:
                    ret.append(n)
                    ids.remove(n.id)
                    break
        if len(ids) > 0: # not all ids where found
            raise NodeNotFoundNodeError
        return ret        

    def _get_edges(self, *ids: int) -> list[edge.Edge]:
        """
        get edges with the mathing id in same order as the ids passed.
            raises:
                GraphError - when at least one id was not found
            retuns:
                list[node.Node]
        """
        ids: list[int] = list(ids)
        ret: list[edge.Edge] = [] # list of requested nodes
        for id_ in ids[:]:
            for e in self.E:
                if e.id == id_:
                    ret.append(e)
                    ids.remove(e.id)
                    break
        if len(ids) > 0: # not all ids where found
            raise EdgeNotMemberOfGraphError
        return ret        


    # Remove
    def _remove_nodes(self, *nodes: node.Node, remove=True):
        """
        Remove nodes from Graph.V (if remove=True), destroy all of its edges, and remove from other nodes's neighbours.
        If you set remove=False: the node will become an isolated Node (Wierzchołek izolowany, bez żadnej krawędzi).
            params:
                nodes: Nodes - nodes to be disconnected from all of their edges.
            raises:
                GraphError - when at least one node is not a member of the graph.
        """
        if not all(n in self.V for n in nodes):
            raise NodeNotMemberOfGraphError
        for n in nodes:
            n._break_connections()
            if remove:
                self.V.remove(n)

    def _remove_edges(self, *edges: edge.Edge):
        """
        disconnect nodes from edges, and remove edges.
            params:
                e: SimpleEdge - edge to be removed from graph
            raises:
                GraphError:
                    - Edge not a member of this graph
        """
        if not all(e in self.E for e in edges):
            raise EdgeNotMemberOfGraphError
        for e in edges:
            e._disconnect_all_nodes()
            self.E.remove(e)


    # Other
    def _nodes_are_members(self, *nodes: node.Node):
        """
        Raise a GraphError when at least one node is not a member of self.V
            params:
                nodes: Node - nodes to be checked
            raises:
                GraphError:  when nodes are not members of the vertices of the graph
        """
        if all(n.graph is self for n in nodes):
            raise NodeNotMemberOfGraphError


    # PROXY METHODS below:
    # I found it comes in handy, when a grandchild wants to add a wraper to parent.func
    # but the parent.func was overwritten by a child (grandchilds parent).
    # Now the _func is never to be overwritten 

    # Add
    @inherit_docstring(_add_nodes)
    def add_nodes(self, num: int) -> list[node.Node]: return self._add_nodes(num)
    @inherit_docstring(_add_edges)
    def add_edges(self, *edges: edge.Edge): return self._add_edges(*edges)

    # Get
    @inherit_docstring(_get_nodes)
    def get_nodes(self, *id_list: int) -> list[node.Node]: return self._get_nodes(*id_list)
    @inherit_docstring(_get_edges)
    def get_edges(self, *id_list: int) -> list[edge.Edge]: return self._get_edges(*id_list)

    # Remove
    @inherit_docstring(_remove_nodes)
    def remove_nodes(self, *nodes: node.Node, remove=True): return self._remove_nodes(*nodes, remove=remove)
    @inherit_docstring(_remove_edges)
    def remove_edges(self, *edges: node.Node): return self._remove_edges(*edges)

    # Other
    @inherit_docstring(_nodes_are_members)
    def nodes_are_members(self, *nodes: node.Node): return self._nodes_are_members(*nodes)


    ###############
    # Other METHODS
    def deepcopy(self):
        "return deepcopy self"
        return deepcopy(self)

    ############################################
    # METHODS to be implemented by child classes
    def connect_two_nodes(self, n1: node.Node, n2: node.Node) -> edge.Edge:
        "Create an edge between two nodes"
        raise NotImplementedError

    def disconnect_two_nodes(self, n1: node.Node, n2: node.Node):
        "Destroy all edges between two nodes"
        raise NotImplementedError
