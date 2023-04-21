class Node():
    left: "Node"
    right: "Node"
    
    def __init__(self, l: "Node" = None, r: "Node" = None) -> None:
        self.left = l
        self.right = r
        pass
    
def solve(n: Node) -> int:
    if n.left is None or n.right is None:
        return 1
    
    return min(solve(n.left), solve(n.right)) + 1

print(solve(Node(Node(Node(l=Node(l=Node())), Node()), Node(Node(), Node(r=Node(r=Node()))))))
