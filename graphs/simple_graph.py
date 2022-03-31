from .graph_base import GraphBase


class SimpleGraph(GraphBase):
    def __init__(self) -> None:
        super().__init__()

    def add_node(self):
        return super().add_node()

    @staticmethod
    def __new_edge(*nodes):

    def connect_nodes(self, n1, n2):

        return super().connect_nodes([n1, n2], new_edge_func=new_edge_func)