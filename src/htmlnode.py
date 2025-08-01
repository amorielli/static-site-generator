from functools import reduce


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not Implemented")

    def props_to_html(self):
        return reduce(
            lambda s, s2: f' {s}="{self.props.get(s)}" {s2}="{self.props.get(s2)}"',
            list(self.props.keys()),
        )

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
