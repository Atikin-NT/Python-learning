
class Stack:

    def __init__(self) -> None:
        self.items = []
    
    def is_empty(self) -> bool:
        return self.items == []
    
    def push(self, item) -> None:
        self.items.append(item)
    
    def pop(self) -> any:
        return self.items.pop()
    
    def peek(self) -> any:
        return self.items[len(self.items)-1]
    
    def size(self) -> int:
        return len(self.items)