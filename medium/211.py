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
            if c == ".":
                # has a child that is end
                return [child.isEnd() for child in self.children.values()].count(True) > 0
            if c in self.children:
                # has a child that is end and has value c
                return self.children[c].isEnd()
            return False
            
        if c == ".":
            for child in self.children.values():
                if child.search(value[1:]):
                    return True
            return False
        
        if c in self.children:
            return self.children[c].search(value[1:])
        
        return False


class WordDictionary:
    root: TrieNode
    

    def __init__(self):
        self.root = TrieNode(None, False)
        

    def addWord(self, word: str) -> None:
        self.root.insert(word)
        

    def search(self, word: str) -> bool:
        return self.root.search(word)
        

wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad")) 
print(wordDictionary.search("bad")) 
print(wordDictionary.search(".ad")) 
print(wordDictionary.search("b..")) 


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)