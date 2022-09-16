# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 17:13:55 2022

@author: User
"""

import pandas as pd
import numpy as np
import time
import random as rand
    

def createRelationsMatrix():
    #create relationship matrix through console inputs
    seaterNameList = []
    matrix = []
    
    print("enter amount people to seat")
    seatQty = int(input(">>> "))
    if (seatQty < 2):
        print("invalid input, value should be 2 or more. Closing program")
        exit()
    
    for i in range(0, seatQty):
        print(f"enter name of person {i + 1}")
        seaterName = input(">>> ")
        seaterNameList.insert(i, seaterName)
       
    matrix = np.zeros((seatQty, seatQty), dtype = int)

    for i in range(0, seatQty - 1):
        for j in range(i + 1, seatQty):
            print(f"enter relationship value (0 - 100) between {seaterNameList[i]} and {seaterNameList[j]}")
            val = int(input(">>> "))
            if (val not in range(0, 101)):
                print("value should be between 0 to 100. Closing program")
                exit()
            matrix[i][j] = val
            matrix[j][i] = val
            
    df = pd.DataFrame(matrix, index = seaterNameList, columns = seaterNameList)
    outputDict = {
        'matrix' : df,
        'names' : seaterNameList
    }
            
    return outputDict


def createRandomRelationsMatrix(n):
    #create random relationship matrix of size n
    seaterNameList = []
    matrix = []

    seatQty = n
    if (seatQty < 2):
        print("invalid input, value should be 2 or more. Closing program")
        exit()
    
    for i in range(0, seatQty):
        seaterNameList.insert(i, f'person {i}')
       
    matrix = np.zeros((seatQty, seatQty), dtype = int)

    for i in range(0, seatQty - 1):
        for j in range(i + 1, seatQty):
            val = rand.randint(0, 100)
            matrix[i][j] = val
            matrix[j][i] = val
            
    df = pd.DataFrame(matrix, index = seaterNameList, columns = seaterNameList)
    outputDict = {
        'matrix' : df,
        'names' : seaterNameList
    }
            
    return outputDict


def verifyRelationsMatrix(matrix, seaterNameList):
    #verify validity of relationship matrix
    
    if (matrix.shape != (len(seaterNameList), len(seaterNameList))):
        print("Matrix size and amount of names given mismatch. Closing program")
        exit()
    
    for i in range(0, len(seaterNameList) - 1):
        for j in range(i + 1, len(seaterNameList)):
            if (matrix[i][j] != matrix[j][i]):
                print("Value error in matrix. Closing program")
                exit()
          
    df = pd.DataFrame(matrix, index = seaterNameList, columns = seaterNameList)
    outputDict = {
        'matrix' : df,
        'names' : seaterNameList
    }
    
    return outputDict


def nearestNeigbour(matrix, origin):
    global st
    m = matrix['matrix'].to_numpy()
    
    #list of node which forms a route
    route = [origin]
    cost = 0
    
    #condition check to determine if node is evaluated using boolean mask
    shape = m.shape[0]
    mask = np.ones(shape, dtype = bool)
    mask[origin] = False
    
    for i in range(shape - 1):
        evaluatingNode = route[-1]
        maxNextNode = np.argmax(m[evaluatingNode][mask])
        nextNode = np.arange(shape)[mask][maxNextNode]
        route.append(nextNode)
        mask[nextNode] = False
        cost += m[evaluatingNode, nextNode]
    cost +=m[nextNode, origin]
        
    outputDict = {
        'route': route,
        'cost': cost,
        'matrix': matrix['matrix']
    }
        
    elapsed_time = time.process_time() - st
    print('CPU Execution time of NN:', time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
    
    return outputDict


def twoOpt(route):
    def edgeCost(node1, node2, matrix):
        node1 = int(node1)
        node2 = int(node2)
        output = matrix[node1][node2]
        return output
    
    
    def routeCost(route, matrix):
        cost = 0
        for i in range(0, len(route) - 1):
            cost += edgeCost(route[i], route[i + 1], matrix)
        cost += edgeCost(route[i + 1], route[0], matrix)
        return cost
    
    
    #reverse order of list in swap1 to swap 2, then combine reversed list to form someRoute
    def twoOptSwap(route, index1, index2):
        li = route[index1:index2+1]
        li.reverse()
        someRoute = np.concatenate((route[0:index1], li, route[index2+1:len(route)]))
        return someRoute
    
    global st
    
    r = route['route']
    c = route['cost']
    m = route['matrix'].to_numpy()
    improving = True
    
    bestCost = c
    while (improving):
        improving = False
        for swap1 in range(1, len(r) - 1): # From each node except the origin,
            for swap2 in range(swap1 + 1, len(r)): # to each following node
                newRoute = list(twoOptSwap(r, swap1, swap2)) 
                newCost = routeCost(newRoute, m)
                
                if newCost > bestCost:
                    r = newRoute
                    bestCost = newCost
                    improving = True
    
    outputDict = {
        'route': r,
        'cost': bestCost,
        'matrix': route['matrix']
    }
    
    elapsed_time = time.process_time() - st
    print('CPU Execution time of 2-opt:', time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
        
    return outputDict


def drawSeats(route):
    
    r = route['route']
    c = route['cost']
    m = route['matrix']
  
    #assign index to seater's name
    nameDict = {}
    index = 0
    for name in m.columns:
        nameDict.update({index: name})
        index += 1
        
    #converts route of index to route of seater name
    seating = ''
    for i in range(len(r)):
        seating += nameDict.get(r[i])
        if i < len(r) - 1:
            seating += ' -->  '


    print(f"\nrelationship matrix is:\n{m}\n\nideal seating is:\n{seating}\nat a total relationship value of {c}\n")
    return(nameDict)
            

isUserInput = True
if isUserInput == True:
    relMatrixDict = createRelationsMatrix()
else:
    #Matrix creation
    seaterName = list('ABCDE')
    relMatrix = np.array(
            [
            [0, 45, 45, 55, 60],
            [45, 0, 30, 45, 65],
            [45, 30, 0, 10, 30],
            [55, 45, 10, 0, 90],
            [60, 65, 30, 90, 0]
            ]
            )
    
    relMatrixDict = verifyRelationsMatrix(relMatrix, seaterName)
    
    #random matrix generator
    #relMatrixDict = createRandomRelationsMatrix(200)
  
st = time.process_time()
    
#a list as a route
nnRoute = nearestNeigbour(relMatrixDict, 0)
drawSeats(nnRoute)

finalRoute = twoOpt(nnRoute)
drawSeats(finalRoute)

