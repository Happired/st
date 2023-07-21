from random import randint
import sys

class LLNode():
#node for linked lists
    def __init__(self, value):
        self.pointer = None;
        self.value = value;

    def setPointer(self, node):
        self.pointer = node

    def reveal(self):
        print(self.value)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

class TreeNode():
#node for trees 
    def __init__(self, value):
        self.leftPointer = None
        self.rightPointer = None
        self.value = value
        self.bal = 0
        self.height = 0

    def setLeftPointer(self, node):
        self.leftPointer = node

    def setRightPointer(self, node):
        self.rightPointer = node

    def reveal(self):
        #print function
        print(self.value)

    def updateHeight(self):
        if self.leftPointer and self.rightPointer:
            if self.leftPointer.height > self.rightPointer.height:
                self.height = self.leftPointer.height + 1
            else:
                self.height = self.rightPointer.height + 1
        elif self.leftPointer:
            self.height = self.leftPointer.height + 1
        elif self.rightPointer:
            self.height = self.rightPointer.height + 1
        else:
            self.height = 0

    def updateBalance(self):
        if self.leftPointer and self.rightPointer:
            self.bal = self.rightPointer.height - self.leftPointer.height
        elif self.leftPointer:
            self.bal = -1 - self.leftPointer.height
        elif self.rightPointer:
            self.bal = self.rightPointer.height + 1
        else:
            self.bal = 0
            
    def updateAll(self):
        self.updateHeight()
        self.updateBalance()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

class LL():

    def __init__(self, headNode):
        self.headNode = headNode

    def addNode(self, value):
        newNode = LLNode(value)
        currentNode = self.headNode
        while currentNode.pointer:
            currentNode = currentNode.pointer
        else:
            currentNode.pointer = newNode

    def reveal(self):
        #print function
        currentNode = self.headNode
        while currentNode.pointer:
            currentNode.reveal()
            currentNode = currentNode.pointer
        print(currentNode.value)

    def insertNode(self, value, index):
        newNode = LLNode(value)
        if index == 0:
            #if new node is inserted as headnode
            a = self.headNode
            self.headNode = newNode
            newNode.pointer = a
        else:
            currNode = self.headNode
            for x in range(index-1):
                currNode = currNode.pointer
                #obtain node at index
            afterNode = currNode.pointer
            currNode.pointer = newNode
            newNode.pointer = afterNode

    def getValue(self, index):
        if index == 0:
            return self.headNode.value
        else:
            currentNode = self.headNode
            for x in range(index):
                currentNode = currentNode.pointer
            return(currentNode.value)

    def getSize(self):
        size = 0
        if self.headNode:
            currentNode = self.headNode
            while currentNode.pointer:
                currentNode = currentNode.pointer
                size += 1
            size += 1
        return size

    def delete(self, index):
        if index == 0:
            oldHeadNode = self.headNode
            self.headNode = oldHeadNode.pointer
            oldHeadNode.pointer = None
            return oldHeadNode.value
        else:
            currentNode = self.headNode
            for x in range(index-1):
                currentNode = currentNode.pointer
            returnNode = currentNode.pointer
            currentNode.pointer = currentNode.pointer.pointer
            return returnNode.value

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

class Stack():
    def __init__(self, value):
        self.headNode = LLNode(value)

    def push(self,value):
        newNode = LLNode(value)
        currNode = self.headNode
        while currNode.pointer:
            currNode = currNode.pointer
        currNode.setPointer(newNode)

    def pop(self):
        currNode = self.headNode
        if not self.headNode.pointer:
            print(self.headNode.value)
            self.headNode = None
            return
        if not self.headNode.pointer.pointer:
            print(self.headNode.pointer.value)
            self.headNode.pointer = None
            return
        while self.headNode.pointer.pointer:
            currNode = currNode.pointer
        print(currNode.pointer.value)
        currNode.pointer = None
        
    def getLast(self):
        currNode = self.headNode
        if not self.headNode.pointer:
            return self.headNode.value
        if not self.headNode.pointer.pointer:
            return self.headNode.pointer.value
        while self.headNode.pointer.pointer:
            currNode = currNode.pointer
        return currNode.pointer.value

    def reveal(self):
        #print function
        currentNode = self.headNode
        while currentNode.pointer:
            currentNode.reveal()
            currentNode = currentNode.pointer
        print(currentNode.value)

    def insertNode(self, value, index):
        newNode = LLNode(value)
        if index == 0:
            #if new node is inserted as headnode
            a = self.headNode
            self.headNode = newNode
            newNode.pointer = a
        else:
            currNode = self.headNode
            for x in range(index-1):
                currNode = currNode.pointer
                #obtain node at index
            afterNode = currNode.pointer
            currNode.pointer = newNode
            newNode.pointer = afterNode

    def getValue(self, index):
        if index == 0:
            return self.headNode.value
        else:
            currentNode = self.headNode
            for x in range(index):
                currentNode = currentNode.pointer
            return(currentNode.value)

    def getSize(self):
        size = 0
        if self.headNode:
            currentNode = self.headNode
            while currentNode.pointer:
                currentNode = currentNode.pointer
                size += 1
            size += 1
        return size

    def delete(self, index):
        if index == 0:
            oldHeadNode = self.headNode
            self.headNode = oldHeadNode.pointer
            oldHeadNode.pointer = None
            return oldHeadNode.value
        else:
            currentNode = self.headNode
            for x in range(index-1):
                currentNode = currentNode.pointer
            returnNode = currentNode.pointer
            currentNode.pointer = currentNode.pointer.pointer
            return returnNode.value
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

class Queue:
#fifo
    def __init__(self, value):
        self.headNode = LLNode(value)

    def enQueue(self, value):
        newNode = LLNode(value)
        currNode = self.headNode
        while currNode.pointer:
            currNode = currNode.pointer
        currNode.setPointer(newNode)

    def deQueue(self):
        newHeadNode = self.headNode.pointer
        self.headNode = newHeadNode

    def getValue(self, index):
        if index == 0:
            return self.headNode.value
        else:
            currentNode = self.headNode
            for x in range(index):
                currentNode = currentNode.pointer
            return(currentNode.value)

    def insertNode(self, value, index):
        newNode = LLNode(value)
        if index == 0:
            #if new node is inserted as headnode
            a = self.headNode
            self.headNode = newNode
            newNode.pointer = a
        else:
            currNode = self.headNode
            for x in range(index-1):
                currNode = currNode.pointer
                #obtain node at index
            afterNode = currNode.pointer
            currNode.pointer = newNode
            newNode.pointer = afterNode

    def reveal(self):
        #print function
        currentNode = self.headNode
        while currentNode.pointer:
            currentNode.reveal()
            currentNode = currentNode.pointer
        print(currentNode.value)

    def getSize(self):
        size = 0
        if self.headNode:
            currentNode = self.headNode
            while currentNode.pointer:
                currentNode = currentNode.pointer
                size += 1
            size += 1
        return size

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------


class BinaryTree():

    def __init__(self, value):
        self.headNode = TreeNode(value)

    def addNode(self, value):
        addingNode = TreeNode(value)
        if not self.headNode:
            self.headNode = addingNode
        else:
            self.recursiveAddNode(addingNode, self.headNode)
    def recursiveAddNode(self, addingNode, currNode):
        if addingNode.value >= currNode.value:
            if currNode.rightPointer:
                self.recursiveAddNode(addingNode, currNode.rightPointer)
            else:
                currNode.setRightPointer(addingNode)
        else:
            if currNode.leftPointer:
                self.recursiveAddNode(addingNode, currNode.leftPointer)
            else:
                currNode.setLeftPointer(addingNode)
    def contains(self, number):
        #return bool
        currNode = self.headNode
        while currNode:
            if currNode.value == number:
                return True
            elif number > currNode.value:
                if currNode.rightPointer:
                    currNode = currNode.rightPointer
                else:
                    return False
            elif number < currNode.value:
                if currNode.leftPointer:
                    currNode = currNode.leftPointer
                else:
                    return False
    def reveal(self):
        self.revealTwo(self.headNode)
        print()
        
    def revealTwo(self, node):
        if node:
            print(str(node.value) + ", ", end="")
            self.revealTwo(node.leftPointer)
            self.revealTwo(node.rightPointer)

    def delete(self, number):

        if self.contains(number):
            if self.headNode.value == number:
                if self.headNode.rightPointer == None and self.headNode.leftPointer == None:
                    self.headNode = None
                elif self.headNode.leftPointer == None and self.headNode.rightPointer:
                    self.headNode = self.headNode.rightPointer
                elif self.headNode.rightPointer == None and self.headNode.leftPointer:
                    self.headNode = self.headNode.leftPointer
                else:
                    theValue = self.findLargestSmall(self.headNode).value
                    self.delete(theValue)
                    self.headNode.value = theValue
            else:
                currParent = None
                currNode = self.headNode
                while currNode.value != number:
                    if number > currNode.value:
                        currParent = currNode
                        currNode = currNode.rightPointer
                        
                    elif number < currNode.value:
                        currParent = currNode
                        currNode = currNode.leftPointer
                #at this point, the current Node should be the one getting deleted
                if currNode.leftPointer == None and currNode.rightPointer == None:
                    if currParent.value > number:
                        currParent.leftPointer = None
                    else:
                        currParent.rightPointer = None
                elif (currNode.leftPointer) and (currNode.rightPointer == None):
                    if currParent.value > number:
                        currParent.setLeftPointer(currNode.leftPointer)
                    else:
                        currParent.setRightPointer(currNode.leftPointer)
                elif (currNode.leftPointer == None) and (currNode.rightPointer):
                    if currParent.value > number:
                        currParent.setLeftPointer(currNode.rightPointer)
                    else:
                        currParent.setRightPointer(currNode.rightPointer)
                else:
                    if currParent.value > number:
                        theValue = self.findLargestSmall(currNode).value
                        self.delete(theValue)
                        currNode.value = theValue

            
    def findLargestSmall(self, node):
        #for delete function
        currNode = node.leftPointer
        while currNode:
            if currNode.rightPointer:
                currNode = currNode.rightPointer
            else:
                return currNode


#----------------------------------------------------------------------------------------------------------------------------------------------------------------


class AVLTree():

    def __init__(self, value):
        self.headNode = TreeNode(value)

    def addNode(self, value):
        #creates node
        addingNode = TreeNode(value)
        #creates headnode
        if self.headNode == None:
            self.headNode = addingNode
            #if there's no headnode, then the adding node is headnode
        else:
            self.headNode = self.recursiveAdd(addingNode, self.headNode) 

        self.update()

    def recursiveAdd(self, nodeToAdd, currNode):
        #finds the proper place
        if currNode:

            if nodeToAdd.value >= currNode.value:
                currNode.rightPointer = (self.recursiveAdd(nodeToAdd, currNode.rightPointer))
            elif nodeToAdd.value < currNode.value:
                currNode.leftPointer = (self.recursiveAdd(nodeToAdd, currNode.leftPointer))

            currNode.updateAll()
            b = self.balance(currNode)
            return b

        else:
            return nodeToAdd
                
    def contains(self, number):
        
        if self.headNode.value == number:
            return True
            #takes care of headnode case

        currentNode = self.headNode

        while currentNode:
            #goes through the rest of the tree
            if currentNode.value == number:
                return True
                #if found, return true

            elif number > currentNode.value:
                #if a number SHOULD be on right
                if currentNode.rightPointer:
                    currentNode = currentNode.rightPointer
                else:
                    return False

            elif number < currentNode.value:
                #if a number SHOULD be on left
                if currentNode.leftPointer:
                    currentNode = currentNode.leftPointer
                else:
                    return False
                
    def findLargestSmall(self, node):
        #for deletion & balancing function
        currentNode = node.leftPointer

        while currentNode:

            if currentNode.rightPointer:
                currentNode = currentNode.rightPointer

            else:
                return currentNode
   

    def reveal(self):
        #print function,, uses recursion (instead of queue)
        self.recursivePrintTwo(self.headNode)
        
    def recursivePrintTwo(self, node):

        if node:
            print(str(node.value) + ", ", end="")
            self.recursivePrintTwo(node.leftPointer)
            self.recursivePrintTwo(node.rightPointer)
            
    
        
    def delete(self, number):

        self.recursive_delete(number)
        
        print("deleting:", number, "balance:", self.headNode.bal, "height:", self.headNode.height, "\n")
        
        self.update()
        b = self.balance(self.headNode)
        self.headNode = b

        self.update()
        b = self.balance(self.headNode)
        self.headNode = b
    
    def recursive_delete(self, number):
        
        if self.contains(number):   
            currentParent = None

            if number == self.headNode.value:
            #deleting the headnode
                if self.headNode.rightPointer == None and self.headNode.leftPointer == None:
                    self.headNode = None
                    #if no children, just get rid of headnode lol
                elif self.headNode.rightPointer != None and self.headNode.leftPointer == None:
                    self.headNode = self.headNode.rightPointer
                    #if there's only a right child, make the right child the head
                elif self.headNode.rightPointer == None and self.headNode.leftPointer != None:
                    self.headNode = self.headNode.leftPointer
                    #if there's only a left child, make the left child the head
                else:
                    #if there are two children :(
                    theValue = self.findLargestSmall(self.headNode).value
                    self.recursive_delete(theValue)
                    self.headNode.value = theValue
                    #largest small is now headnode
                    
                self.update()
                    
                
            else:
                #deleting a regular node
                currentParent = None
                currentNode = self.headNode

                while not currentNode.value == number:
                #getting the node to be deleted,,,

                    if number > currentNode.value:
                        currentParent = currentNode
                        currentNode = currentNode.rightPointer
                    elif number < currentNode.value:
                        currentParent = currentNode
                        currentNode = currentNode.leftPointer

                if currentNode.rightPointer == None and currentNode.leftPointer == None:
                    #if the node has no children, then set the parent's applicable pointer to none
                    if currentNode.value > currentParent.value:
                        currentParent.rightPointer = None 
                    else:
                        currentParent.leftPointer = None
                        
                elif (currentNode.rightPointer == None) and (currentNode.leftPointer != None):
                    #if node has a left child, set largest small to be new node
                    theValue = self.findLargestSmall(currentNode).value
                    self.recursive_delete(theValue)
                    currentNode.value = theValue

                elif (currentNode.rightPointer != None) and (currentNode.leftPointer == None):
                    #if node has a right pointer, node parents takes on child
                    if currentNode.value > currentParent.value:
                        currentParent.rightPointer = currentNode.rightPointer
                    else:
                        currentParent.leftPointer = currentNode.rightPointer

                else:
                    #if node has two children, act as deleting headnode with two children
                    theValue = self.findLargestSmall(currentNode).value
                    self.recursive_delete(theValue)
                    currentNode.value = theValue
                    
                self.update()
                
                return currentParent
        else:
            return None
        
    def leftRotation(self, a):

        b = a.rightPointer
        a.setRightPointer(b.leftPointer)
        b.setLeftPointer(a)
        a.updateAll()
        b.updateAll()
        return b

    def rightRotation(self, a):

        b = a.leftPointer
        a.setLeftPointer(b.rightPointer)
        b.setRightPointer(a)
        a.updateAll()
        b.updateAll()
        return b
        
    def update(self):
        self.recursiveUpdate(self.headNode)
        
    def recursiveUpdate(self, node):
        if node:
            self.recursiveUpdate(node.leftPointer)
            self.recursiveUpdate(node.rightPointer)
            node.updateAll()
            #updates from ground up     
    

    def balance(self, node):
        #function controls rotations 
        if node:
            self.balance(node.leftPointer)
            self.balance(node.rightPointer)
            #rotates from ground up

            if node.bal > 1:
                #if unbalanced on right

                if node.rightPointer.bal >= 1:

                    b =  self.leftRotation(node)
                    return b
                    #left rotation

                else:

                    #if node child is balanced/unbalanced on left

                    node.rightPointer = self.rightRotation(node.rightPointer)
                    return self.leftRotation(node)
                    #right left rotation
                    
                    
            elif node.bal < -1:
                #if unbalanced on left

                if node.leftPointer.bal <= -1:
                    #if node's child is left unbalanced
                    b = self.rightRotation(node)
                    return b
                    #right rotation

                else:
                    #if node's child is balanced/right unbalanced
                    node.leftPointer = self.leftRotation(node.leftPointer)
                    return self.rightRotation(node)
                    #left right rotation
                    
                    
            else:
                #if node is balanced, return
                return node





#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# firstNode = LLNode(3)
# linkedListTest = LL(firstNode)
# linkedListTest.addNode(7)
# linkedListTest.addNode(9)
# linkedListTest.addNode(6)
# linkedListTest.delete(2)
# linkedListTest.reveal()

# bt = BinaryTree(11)

# for x in range(10):
#     bt.addNode(randint(0, 20))
# bt.reveal()
# bt.delete(10)
# bt.reveal()

# #=== AVL Tree Testing

# print()
# avltree = AVLTree(0)

# for x in range(1,20):
#     avltree.addNode(x)
    

# avltree.reveal()
# avltree.delete(14)
# avltree.reveal()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

class adjacencyMatrix():

    def __init__(self):
        self.matrixTable = []
        self.dictionary = {}

    def addNode(self, letter):
        #to add a new node: add -1 to each row, 
        for x in range(len(self.matrixTable)):
            self.matrixTable[x].append(-1)
        self.matrixTable.append([-1])
        #create new column, 
        for x in range(len(self.matrixTable)):
            self.matrixTable[-1].append(-1)
        #and fill new column with -1's
        self.dictionary[letter] = len(self.matrixTable) -1
        #letter is assigned to index in matrixtable
    
    def reveal(self):
        #print function
        print(self.matrixTable)
        
    def createEdge(self, first, second, cost):
        self.matrixTable[self.dictionary[second]][self.dictionary[first]] = cost
        self.matrixTable[self.dictionary[first]][self.dictionary[second]] = cost
        #updates cost in intersecting spot in matrix table
    
    def getEdges(self, nodeValue):
        #get ion (= index of node in matrix table)
        ion = self.dictionary[nodeValue]
        # ^ finds index in matrix table
        tempTable = []
        # ^ table for returning edges

        for x in range(len(self.matrixTable[ion])):
            #for every cost in the nested table
                if not self.matrixTable[ion][x] == -1:
                    tempTable.append(self.getKey(x))
                    #if the cost exists, add to the table the letter of the edge
        return tempTable

    def findEdge(self, first, second):
        if second in self.getEdges(first):
            return self.matrixTable[self.dictionary[first]][self.dictionary[second]]
        else:
            return False

    def getKey(self, value):
        #get the key for a value
        for x in self.dictionary:
            if self.dictionary[x] == value:
                return x

    def bfs(self, node):
        #breadth first search; uses queue
        tempQueue = Queue(node)
        thingsAlreadyPrinted = []
        thingsAlreadyPrinted.append(node)
        while tempQueue.getSize() != 0:
            
            for x in self.getEdges(tempQueue.headNode.value):
                if not x in thingsAlreadyPrinted:

                    tempQueue.enQueue(x)
                    thingsAlreadyPrinted.append(x)
            print(tempQueue.headNode.value)
            tempQueue.deQueue()

    def dfs(self, node):
        #depth first search,, uses recursion
        tempTable = []
        #temptable: things already printed
        self.dfs_recursive(node, tempTable)
        return tempTable

    def dfs_recursive(self, node, tempTable):
        tempTable.append(node)
        for x in self.getEdges(node):
            if x not in tempTable:
                self.dfs_recursive(x, tempTable)


    def checkOuts(self, costs, outs, index):
        #for djisktras
        #checks if the letter that corresponds to the index is in outs
        if self.getKey(costs[index]) in outs:
            return True
        return False
    
    def findShortestPath(self, first, second):
        #LOCF = List of Connections from First (Node)
        LOCF = self.dfs(first)
        #if the second node is not connected, stop
        if not second in LOCF:
            return False
        # outs = already explored
        # costs = list of total costs for each node path
        # backNodeList = for each node, the previous node to reach current
        outs = []
        costs = []
        backNodeList = []
        for x in self.matrixTable:
            costs.append(999)
            backNodeList.append("")
        costs[self.dictionary[first]] = 0
        #set the cost of first node to 0, every other to max integer
        print(costs)
        path = Stack(first)
        print("initial costs:", costs)
        
        currNode = first

        while currNode != second:
            #until optimal path has not been found
            outs.append(currNode)
            #cross off current node
            print('Exploring node', currNode, ",,,")
            tempList = []
            #tempList = a list of the nodes to explore from currNode 
            for x in self.getEdges(currNode):
                if not x in outs:
                    print("to", x)
                    tempList.append(x)

            if tempList != []:
                #if new nodes were explored
                for x in self.getEdges(currNode):
                    if not x in outs:
                        overridingCost = costs[self.dictionary[currNode]] + self.matrixTable[self.dictionary[currNode]][self.dictionary[x]]
                        #for each node not yet explored, calculate whether the new cost (combined edges of currentNode to newNode) is greater than already calculated newNode cost
                        if costs[self.dictionary[x]] > overridingCost:
                            #if so, override previous cost and add currentNode to the backNode list
                            costs[self.dictionary[x]] = overridingCost
                            backNodeList[self.dictionary[x]] = currNode
                        # overrides the node's cost 
                    print("outs: ", outs)
                    print("costs: ", costs)
            tempList2 = []
            for j in range(len(costs)):
                if self.getKey(j) not in outs:
                    #for each unvisited letter, print its cost and it to tempList2
                    print(costs[j])
                    tempList2.append(costs[j])
                else:
                    tempList2.append(1000)
            
            lowestCost = min(tempList2)
            
            if tempList == []:
                path.pop()
            #if no new nodes were visited, remove node from path
                
            currNode = self.getKey(tempList2.index(lowestCost))
            #new currentNode is assigned to the node with the lowest cost
            
            if currNode != first:
                path.push(currNode)
        
        forwardPath = []
        currNode = second
        forwardPath.append(second)

        while (first not in forwardPath):
            forwardPath.append(backNodeList[self.dictionary[currNode]])
            currNode = backNodeList[self.dictionary[currNode]]
        #find path back to first
        
        print("path:", end="")
        forwardPath.reverse()
        print(forwardPath)

 
#=== Adjacency Matrix Testing

a = adjacencyMatrix()
a.addNode('b')
a.addNode('c')
a.addNode('d')
a.addNode('e')
a.addNode('f')
a.addNode('g')
a.addNode('h')
a.addNode('i')
a.addNode('j')

a.createEdge('b', 'c', 3)
a.createEdge('i', 'b', 2)
a.createEdge('j', 'f', 5)
a.createEdge('h', 'e', 1)
a.createEdge('h', 'f', 1)
a.createEdge('i', 'd', 20)
a.createEdge('b', 'g', 2)
a.createEdge('g', 'f', 8)
a.createEdge('f', 'd', 1)
a.createEdge('d', 'c', 9)
a.createEdge('e', 'c', 4)

print(a.matrixTable)
print(a.dictionary)
# a.bfs('b')
# print()
# print(a.dfs('b'))

a.findShortestPath('b', 'f')
