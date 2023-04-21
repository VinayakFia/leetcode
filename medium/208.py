class TrieNode:
    value: str
    children: dict[str, "TrieNode"]
    end: bool
    
    
    def __init__(self, value: str ,end: bool) -> None:
        self.value = value
        self.end = end    
        self.children = {}


    def setEnd(self, end: bool) -> None:
        self.end = end
        
        
    def isEnd(self) -> bool:
        return self.end


    def insert(self, value: str) -> None:
        c = value[0]
        
        if c in self.children:
            if len(value) == 1:
                self.children[c].setEnd(True)
            else:
                self.children[c].insert(value[1:])
        else:
            if len(value) == 1:
                self.children[c] = TrieNode(c, True)
            else:
                self.children[c] = TrieNode(c, False)
                self.children[c].insert(value[1:])
            

    def search(self, value: str) -> bool:
        c = value[0]
        
        if len(value) == 1:
            if c in self.children:
                return self.children[c].isEnd()
            return False
        
        if c in self.children:
            return self.children[c].search(value[1:])
        
        return False
    
    
    def startsWith(self, value: str) -> bool:
        c = value[0]
        
        if len(value) == 1:
            return c in self.children
        
        if c not in self.children:
            return False
        
        return self.children[c].startsWith(value[1:])


class Trie:
    root: TrieNode

    def __init__(self):
        self.root = TrieNode(None, False)
        

    def insert(self, word: str) -> None:
        self.root.insert(word)
        

    def search(self, word: str) -> bool:
        return self.root.search(word)
        

    def startsWith(self, prefix: str) -> bool:
        return self.root.startsWith(prefix)
        
    
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)