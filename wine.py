# https://code.google.com/codejam/contest/4214486/dashboard#s=p1

# execute cmd:   python wine.py B-small-practice.in.txt 
# execute cmd:   python wine.py B-large-practice.in.txt
# the output is in wineOutput.txt

import sys

orderSearchTable={}

def layerGlass(L):
    ret=0
    for i in range(1,L+1):
        ret +=i
    return ret


def totalGalass(L):
    sum=0
    for i in range(1,L+1):
        sum += i*(L+1-i)
    return sum

def sumGlassArray(L):
    ret={}
    num=0
    for i in range(1,L+1):
        if i==1:
            num +=1
            ret[num]=1
        else:
            for j in range(i):
                num += 1
                ret[num]=i
    return (ret)
        
        
def searchLevel(glasses, num, s, e):
    mid = (s+e)/2
    if (mid+1<=len(glasses)-1):
        if glasses[mid]<=num and (mid+1<=len(glasses) and glasses[mid+1]>=num):
            return mid
    else:
        if glasses[mid]<=num:
            return mid;
    
    if glasses[mid]>num:
        return searchLevel(glasses, num, s,mid)
    else:
        return searchLevel(glasses, num, mid, e)
    
    
        
def wineML(B, L, N):
    volume= B*750
    #search volume in glassarray
    (glass, sumGlass)=sumGlassArray(3*B)
    level=searchLevel(sumGlass, 3*B, 1, 3*B)
    
    ret=1.0*(volume-sumGlass[level]*250)/(glass[level+1])

    print ret
    
    
    
def wineML2(B, L, N):
    tree = buildTree(L)
    print "tree is built"
    #link=tree.findAncients(L, N)
    #tree.pour(B*750, L, N, link)
    pour2(B*750, L, N, tree)
    node = tree.findNode(L, N)
    
    return node.getVolumn() 
    
            

def buildTree(L):
    nums={}
    global orderSearchTable
    
    (orderSearchTable)=sumGlassArray(L)
    
    for i in range(1,L+1):
        #print "build level ", i, "/", L
        if i==1:
            nums[i]=1
            tree=NODE(1,1)
        else:
            nums[i]=nums[i-1]+i
            for j in range(1,nums[i]+1):
                node = NODE(i,j)
                tree.addChild(i, node)
    return tree
    
    
def pour2(volumn, L, N, tree):
    level=1
    
    if L==4:
        print L
    
    if volumn > 250:
        tree.setVolumn(250)
        tree.setOverflow(volumn-250)
    else:
        tree.setVolumn(volumn)
        return
    
    level+=1
    while level <= L:
        for num in NODE.nodes[level].keys():
            node = NODE.nodes[level][num]
            income=0
            for p in node.getParents():
                income += 1.0*p.getOverflow()/len(p.getChildren())
                 
            if income > 250:
                node.setVolumn(250)
                node.setOverflow(income-250)
            else:
                node.setVolumn(income)
        level+=1
                
    
    
    
class NODE:
    nodes={}
    
    def __init__(self, L, N):
        self.level=L
        self.num = N
        self.parents=[]
        self.children=[]
        self.volumn=0
        if L not in NODE.nodes.keys():
            NODE.nodes[L]={}
            NODE.nodes[L][N]=self
        else:
            NODE.nodes[L][N]=self
        self.overflow=0
        
    def getChildren(self):
        return self.children
        
    def getParents(self):
        return self.parents
    
    def getOverflow(self):
        return self.overflow
    
    def setOverflow(self, overflow):
        self.overflow = overflow
    
    def getVolumn(self):
        return self.volumn
    
    def setVolumn(self, volumn):
        self.volumn = volumn
        
    def findNode(self, L, N):
        return NODE.nodes[L][N]
#         if L>self.level:
#             ret=None
#             for child in self.children:
#                 ret= child.findNode(L,N)
#                 if ret!=None:
#                     return ret
#         else:
#             if self.num == N:
#                 return self
        
    def withinLevel(self):
        global orderSearchTable
        return orderSearchTable[self.num]
        
    def insertChild(self, node):
        self.children.append(node)
        
    def addParent(self, parent):
        self.parents.append(parent)
        
    def addChild(self, L, node):
        
        global orderSearchTable
        layer = orderSearchTable[node.num]
        
        # it's parents
        
        if (layer < node.level):
            parent = NODE.nodes[node.level-1][node.num]
            parent.insertChild(node)
            node.addParent(parent)
            
        if (node.num >layer and orderSearchTable[node.num - layer] ==layer-1):
            parent = NODE.nodes[node.level-1][node.num-layer]
            parent.insertChild(node)
            node.addParent(parent)
        
        if (node.num > layer-1 and orderSearchTable[node.num - layer+1] ==layer-1):
            parent = NODE.nodes[node.level-1][node.num-layer+1]
            parent.insertChild(node)
            node.addParent(parent)
#         
#         if self.level+1<L:
#             for child in self.children:
#                 child.addChild(L, node)
#         if L==self.level + 1 and (self.num==node.num or node.num==self.num + self.withinLevel() or node.num==self.num + self.withinLevel()+1):
#             self.children.append(node)
    
    def findAncients(self, L, N):
        ancient=set()
        
        if L==16:
            print L
        
        node = self.findNode(L,N)
        
        parents=node.getParents()
        while len(parents):
            p=parents[0]
            ancient.add(p)
            for gp in p.getParents():
                if gp not in parents:
                    parents.append(gp)
            parents.remove(p)
        
        ancient.add(node)        
        print L,N, len(ancient)
        return ancient
    
    def DFS(self, L, N):
        if self.level==L and self.num==N:
            link=set()
            link.add(self)
            return link
        else:
            for child in self.children:
                ret=child.DFS(L,N)
                if ret!=None:
                    ret.add(self)
                    return ret
        return None
    
    

    
    
    def pour(self, volumn, L, N, link):
        
        #print "pour", self.level, self.num
        
        if volumn + self.volumn> 250:
            overflow = volumn+self.volumn-250
            self.volumn=250
            for child in self.children:
                if child in link:
                    child.pour(1.0*(overflow)/3, L, N, link)
        else:
            self.volumn += volumn
            

def main(argv):
    
    inputfile = argv[0]
    fi = open(inputfile, "r")
    fo = open("wineOutput.txt","w")
    line=fi.readline()
    casesNum = int(line)
    for i in range(casesNum):
        print i, "/", casesNum
        line=fi.readline()
        inputs=line.split()
        B=int(inputs[0])
        L=int(inputs[1])
        N=int(inputs[2]) 
        volumn = wineML2(B,L,N)
        fo.write("Case #" + str(i+1) + ": " + str(volumn) + "\n")
    fi.close()
    fo.close()

if __name__=="__main__":
    main(sys.argv[1:])
