from dataclasses import dataclass

@dataclass
class NumberNode(): # Represents a factor
    value: any

    def __repr__(self):
        return f'{self.value}'

@dataclass
class AddNode(): # Represents a add expression
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}+{self.node_b})"

@dataclass
class SubtractNode(): # Represents a subtract expression
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}-{self.node_b})"

@dataclass
class MultiplyNode(): # Represents a multiply term
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}*{self.node_b})"


@dataclass
class DivideNode(): # Represents a division term
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}/{self.node_b})"


@dataclass
class PlusNode(): # Represents a positive number
    node: any

    def __repr__(self): 
        return f"(+{self.node})"

@dataclass
class MinusNode():
    node: any

    def __repr__(self):
        return f"(-{self.node})"