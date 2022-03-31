from ..errors import NodeError

class Node:
    def __init__(self, *, name=None, id=None) -> None:
        self.neighbours = []
        if id is None:
            raise NodeError("No id was passed when creating a Node(id=???).")
        self.id = id
        self.name = name if name is not None else f"Node id={id}"
    