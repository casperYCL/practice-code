class Kruskal:
    def __init__(self,vertex):
        self.n = vertex
        self.graph = []

    #新增邊數
    def addEdge(self,f,l,w):
        self.graph.append([f,l,w])

    def bubbleSort(self):
        n = len(self.graph)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.graph[j][2] > self.graph[j+1][2]:
                    self.graph[j][2], self.graph[j+1][2] = self.graph[j+1][2], self.graph[j][2]

    def KruskalMSL(self):
        answer = []
        t = 0 #answer內數量
        self.bubbleSort() #依邊的權重大小排序
        answer.append(self.graph[0]) #加數最小的
        answer.append(self.graph[1]) #加數第二小的(兩個不會形成迴圈)
        num = 2 #決定第三大位數
        while t<self.n-(1+2): #邊數為頂點數-1 已醒做完第一二條所以-2
            if self.graph[num][0] != self.graph[1][1] and self.graph[num][1] != self.graph[0][0]:
                answer.append(self.graph[num])  # 加數第三小的(兩個不會形成迴圈)
                t+=1
                num+=1
                break
            else:
                num+=1

        #三個未迴圈的圖加一條線也不會形成迴圈 直接加入第四大位數
        answer.append(self.graph[num])
        t += 1
        num += 1

        #加入第五大位數
        while t<self.n-(1+2): #邊數為頂點數-1 已醒做完第一二條所以-2
            if (self.graph[num][0] != self.graph[1][0] or self.graph[num][1] != self.graph[2][0]) and (self.graph[num][0] != self.graph[3][1] or self.graph[num][1] != self.graph[0][1]) and (self.graph[num][0] != self.graph[2][0] or self.graph[num][1] != self.graph[0][1]):
                answer.append(self.graph[num])  # 加數第三小的(兩個不會形成迴圈)
                t += 1
                num += 1
                break
            else:
                num+=1

        for i in range(len(answer)):
            print(answer[i][0],"--",answer[i][1],"=",answer[i][2])

k=Kruskal(6)
k.addEdge("bar","castle",1)
k.addEdge("home","store",2)
k.addEdge("shop","store",3)
k.addEdge("bar","store",4)
k.addEdge("home","shop",5)
k.addEdge("home","bank",6)
k.addEdge("bank","store",7)
k.addEdge("bar","bank",9)
k.addEdge("store","castle",10)
k.addEdge("shop","castle",12)
k.KruskalMSL()
