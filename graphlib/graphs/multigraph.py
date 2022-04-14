from ..graphs.two_nodes_edge_graph import TNEGraph


class Multigraph(TNEGraph):
    def __init__(self, *, allow_multigraph=True, allow_loops=True) -> None:
        super().__init__(allow_multigraph = allow_multigraph,
                         allow_loops = allow_loops) 
    