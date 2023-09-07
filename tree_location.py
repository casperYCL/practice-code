class TreeLocation:
    def __init__(self):
        self.treeDict = {}
        self.floor = 1

    def splitWord(self,word):
        split = word.find(' ')
        front = word[:split]
        back = word[split+1:]
        return front,back

    def buildNodeDict(self):
        nodeNumber = int(input("TREE "))
        for i in range(nodeNumber - 1):
            word = input()
            front, back = self.splitWord(word)
            if self.treeDict == {}:
                rootNode = front
            if front in self.treeDict.keys():
                takeList = self.treeDict[front]
                takeList.append(back)
                self.treeDict[front] = takeList
            else:
                self.treeDict[front] = [back]
        return rootNode

    def findDeep(self,rootNode):
        nodeList = self.treeDict[rootNode]
        for node in nodeList:
            floor = 1
            floor = self.loop(node,floor)
            if floor > self.floor:
                self.floor = floor

    def loop(self,node,floor):
        if node in self.treeDict.keys():
            nodeList = self.treeDict[node]
            floor += 1
            for node in nodeList:
                floor = self.loop(node,floor)
                return floor
        else:
            return floor


treeLocation = TreeLocation()
rootNode = treeLocation.buildNodeDict()
floor = treeLocation.findDeep(rootNode)
print(treeLocation.floor)






