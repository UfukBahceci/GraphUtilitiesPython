import numpy as np
from numpy import linalg as LA
import math

def create_completesimplegraph(vertices, nodepos, distancetype):
    listofvertices = []
    listofedges = []
    nodeposset = {}
    distancetypes = ['Rectilinear', 'Euclidian', 'Chebyshev', 'Cosine', 'binaryJaccard', 'binarySorensenDice', 'discreteHellinger', 'discreteKL', 'binaryHamming', 'Levenshtein']
    enumerate_distancetypes = enumerate(distancetypes)
    selectedindex = -1
    for index, dtype in enumerate_distancetypes:
        if(distancetype == dtype):
            selectedindex = index
    if(selectedindex == -1):
        print('Please select a valid distance type!\n')
    else:
        try:
            assert (np.size(vertices,0) > 0 and np.size(vertices,0) == np.size(nodepos,0) and np.size(nodepos,1) == 2), "Please check the input format!"
            numberofvertices = np.size(vertices,0)
            for v in range(numberofvertices):
                listofvertices.append((v, {'color': 'black'}))
                nodeposset[v] = nodepos[v]
            if(selectedindex == 0):
                print('Rectilinear distance selected..\n')
                for v1 in range(numberofvertices):
                    for v2 in range(numberofvertices):
                        if(v1<v2):
                            distance = 0
                            for j in range(np.size(vertices,1)):
                                distance += abs(vertices[v1][j]-vertices[v2][j])
                            distance = float(distance)
                            distance = round(distance, 2)
                            newedge = (v1,v2,distance)
                            listofedges.append(newedge)
            elif(selectedindex == 1):
                print('Euclidian distance selected..\n')
                for v1 in range(numberofvertices):
                    for v2 in range(numberofvertices):
                        if(v1<v2):
                            distance = 0
                            for j in range(np.size(vertices,1)):
                                distance += (vertices[v1][j]-vertices[v2][j])**2
                            distance = math.sqrt(distance)
                            distance = float(distance)
                            distance = round(distance, 2)
                            newedge = (v1,v2,distance)
                            listofedges.append(newedge)
            elif(selectedindex == 2):
                print('Chebyshev distance selected..\n')
                for v1 in range(numberofvertices):
                    for v2 in range(numberofvertices):
                        if(v1<v2):
                            distance = 0
                            for j in range(np.size(vertices,1)):
                                distance = max(distance,abs(vertices[v1][j]-vertices[v2][j]))
                            distance = float(distance)
                            distance = round(distance, 2)
                            newedge = (v1,v2,distance)
                            listofedges.append(newedge)
            elif(selectedindex == 3):
                print('Cosine distance selected..\n')
                for v1 in range(numberofvertices):
                    for v2 in range(numberofvertices):
                        if(v1<v2):
                            distance = np.dot(vertices[v1],vertices[v2].T)
                            distance = float(distance)
                            distance = distance / (LA.norm(vertices[v1],2)*LA.norm(vertices[v2],2))
                            distance = 1 - distance
                            distance = round(distance, 2)
                            newedge = (v1,v2,distance)
                            listofedges.append(newedge)
            elif(selectedindex == 4):
                print('binary Jaccard distance selected..\n')
                for v1 in range(numberofvertices):
                    for v2 in range(numberofvertices):
                        if(v1<v2):
                            distance = LA.norm(np.logical_and(vertices[v1],vertices[v2]),1)
                            distance = float(distance)
                            distance = distance / (np.size(vertices,1) - LA.norm(np.logical_and(1-vertices[v1],1-vertices[v2]),1))
                            distance = 1 - distance
                            distance = round(distance, 2)
                            newedge = (v1,v2,distance)
                            listofedges.append(newedge)
            elif(selectedindex == 5):
                print('binary Sorensen-Dice distance selected..\n')
                for v1 in range(numberofvertices):
                    for v2 in range(numberofvertices):
                        if(v1<v2):
                            distance = 2*LA.norm(np.logical_and(vertices[v1],vertices[v2]),1)
                            distance = float(distance)
                            distance = distance / (LA.norm(vertices[v1],1) + LA.norm(vertices[v2],1))
                            distance = 1 - distance
                            distance = round(distance, 2)
                            newedge = (v1,v2,distance)
                            listofedges.append(newedge)
            elif(selectedindex == 6):
                print('discrete Hellinger distance selected..\n')
                for v1 in range(numberofvertices):
                    for v2 in range(numberofvertices):
                        if(v1<v2):
                            distance = 0
                            for j in range(np.size(vertices,1)):
                                distance += (math.sqrt(vertices[v1][j])-math.sqrt(vertices[v2][j]))**2                          
                            distance = (1/math.sqrt(2))*math.sqrt(distance)           
                            distance = float(distance)
                            distance = round(distance, 2)
                            newedge = (v1,v2,distance)
                            listofedges.append(newedge)
            elif(selectedindex == 7):
                print('discrete Kullback–Leibler divergence selected..\n')
                for v1 in range(numberofvertices):
                    for v2 in range(numberofvertices):
                        if(v1<v2):
                            distance = 0
                            for j in range(np.size(vertices,1)):
                                distance += vertices[v2][j]*math.log(vertices[v2][j]/vertices[v1][j])
                            distance = float(distance)
                            distance = round(distance, 2)
                            newedge = (v1,v2,distance)
                            listofedges.append(newedge)
            elif(selectedindex == 8):
                print('binary Hamming distance selected..\n')
                for v1 in range(numberofvertices):
                    for v2 in range(numberofvertices):
                        if(v1<v2):
                            distance = LA.norm(np.logical_xor(vertices[v1],vertices[v2]),1)
                            distance = float(distance)
                            distance = round(distance, 2)
                            newedge = (v1,v2,distance)
                            listofedges.append(newedge)
        except AssertionError as msg:
            print(msg)
    return [listofvertices, listofedges, nodeposset]

def create_bipartitesimplegraph(vertices, nodepos, distancetype, sizeoffirstvertexset):
    listofvertices = []
    listofedges = []
    nodeposset = {}
    distancetypes = ['Rectilinear', 'Euclidian', 'Chebyshev', 'Cosine', 'binaryJaccard', 'binarySorensenDice', 'discreteHellinger', 'discreteKL', 'binaryHamming', 'Levenshtein']
    enumerate_distancetypes = enumerate(distancetypes)
    selectedindex = -1
    for index, dtype in enumerate_distancetypes:
        if(distancetype == dtype):
            selectedindex = index
    if(selectedindex == -1):
        print('Please select a valid distance type!\n')
    else:
        try:
            assert (np.size(vertices,0) > 0 and np.size(vertices,0) == np.size(nodepos,0) and np.size(nodepos,1) == 2), "Please check the input format!"
            numberofvertices = np.size(vertices,0)
            for v in range(numberofvertices):
                listofvertices.append((v, {'color': 'black'}))
                nodeposset[v] = nodepos[v]
            if(selectedindex == 0):
                print('Rectilinear distance selected..\n')
                for v1 in range(numberofvertices):
                    for v2 in range(numberofvertices):
                        if(v1<sizeoffirstvertexset and v2>=sizeoffirstvertexset):
                            distance = 0
                            for j in range(np.size(vertices,1)):
                                distance += abs(vertices[v1][j]-vertices[v2][j])
                            distance = float(distance)
                            distance = round(distance, 2)
                            newedge = (v1,v2,distance)
                            listofedges.append(newedge)
            elif(selectedindex == 1):
                print('Euclidian distance selected..\n')
                for v1 in range(numberofvertices):
                    for v2 in range(numberofvertices):
                        if(v1<sizeoffirstvertexset and v2>=sizeoffirstvertexset):
                            distance = 0
                            for j in range(np.size(vertices,1)):
                                distance += (vertices[v1][j]-vertices[v2][j])**2
                            distance = math.sqrt(distance)
                            distance = float(distance)
                            distance = round(distance, 2)
                            newedge = (v1,v2,distance)
                            listofedges.append(newedge)
            elif(selectedindex == 2):
                print('Chebyshev distance selected..\n')
                for v1 in range(numberofvertices):
                    for v2 in range(numberofvertices):
                        if(v1<sizeoffirstvertexset and v2>=sizeoffirstvertexset):
                            distance = 0
                            for j in range(np.size(vertices,1)):
                                distance = max(distance,abs(vertices[v1][j]-vertices[v2][j]))
                            distance = float(distance)
                            distance = round(distance, 2)
                            newedge = (v1,v2,distance)
                            listofedges.append(newedge)
            elif(selectedindex == 3):
                print('Cosine distance selected..\n')
                for v1 in range(numberofvertices):
                    for v2 in range(numberofvertices):
                        if(v1<sizeoffirstvertexset and v2>=sizeoffirstvertexset):
                            distance = np.dot(vertices[v1],vertices[v2].T)
                            distance = float(distance)
                            distance = distance / (LA.norm(vertices[v1],2)*LA.norm(vertices[v2],2))
                            distance = 1 - distance
                            distance = round(distance, 2)
                            newedge = (v1,v2,distance)
                            listofedges.append(newedge)
            elif(selectedindex == 4):
                print('binary Jaccard distance selected..\n')
                for v1 in range(numberofvertices):
                    for v2 in range(numberofvertices):
                        if(v1<sizeoffirstvertexset and v2>=sizeoffirstvertexset):
                            distance = LA.norm(np.logical_and(vertices[v1],vertices[v2]),1)
                            distance = float(distance)
                            distance = distance / (np.size(vertices,1) - LA.norm(np.logical_and(1-vertices[v1],1-vertices[v2]),1))
                            distance = 1 - distance
                            distance = round(distance, 2)
                            newedge = (v1,v2,distance)
                            listofedges.append(newedge)
            elif(selectedindex == 5):
                print('binary Sorensen-Dice distance selected..\n')
                for v1 in range(numberofvertices):
                    for v2 in range(numberofvertices):
                        if(v1<sizeoffirstvertexset and v2>=sizeoffirstvertexset):
                            distance = 2*LA.norm(np.logical_and(vertices[v1],vertices[v2]),1)
                            distance = float(distance)
                            distance = distance / (LA.norm(vertices[v1],1) + LA.norm(vertices[v2],1))
                            distance = 1 - distance
                            distance = round(distance, 2)
                            newedge = (v1,v2,distance)
                            listofedges.append(newedge)
            elif(selectedindex == 6):
                print('discrete Hellinger distance selected..\n')
                for v1 in range(numberofvertices):
                    for v2 in range(numberofvertices):
                        if(v1<sizeoffirstvertexset and v2>=sizeoffirstvertexset):
                            distance = 0
                            for j in range(np.size(vertices,1)):
                                distance += (math.sqrt(vertices[v1][j])-math.sqrt(vertices[v2][j]))**2                          
                            distance = (1/math.sqrt(2))*math.sqrt(distance)           
                            distance = float(distance)
                            distance = round(distance, 2)
                            newedge = (v1,v2,distance)
                            listofedges.append(newedge)
            elif(selectedindex == 7):
                print('discrete Kullback–Leibler divergence selected..\n')
                for v1 in range(numberofvertices):
                    for v2 in range(numberofvertices):
                        if(v1<sizeoffirstvertexset and v2>=sizeoffirstvertexset):
                            distance = 0
                            for j in range(np.size(vertices,1)):
                                distance += vertices[v2][j]*math.log(vertices[v2][j]/vertices[v1][j])
                            distance = float(distance)
                            distance = round(distance, 2)
                            newedge = (v1,v2,distance)
                            listofedges.append(newedge)
            elif(selectedindex == 8):
                print('binary Hamming distance selected..\n')
                for v1 in range(numberofvertices):
                    for v2 in range(numberofvertices):
                        if(v1<sizeoffirstvertexset and v2>=sizeoffirstvertexset):
                            distance = LA.norm(np.logical_xor(vertices[v1],vertices[v2]),1)
                            distance = float(distance)
                            distance = round(distance, 2)
                            newedge = (v1,v2,distance)
                            listofedges.append(newedge)
        except AssertionError as msg:
            print(msg)
    return [listofvertices, listofedges, nodeposset]