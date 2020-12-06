from __future__ import print_function
from ortools.linear_solver import pywraplp
import matplotlib.pyplot as plt
import numpy as np
import math


def distance(point1, point2):
    distance = math.sqrt(((point1[0]-point2[0])**2)+((point1[1]-point2[1])**2))
    print(distance)
    return distance

def TPS_solver(locations, distanceArray, Ref_point):
    solver = pywraplp.Solver.CreateSolver('SCPI')
    for i in locations:
        plt.plot(i[0], i[1], 'bo-')
        distanceArray.append(distance(Ref_point, i))
    plt.show()




locations = np.array([
   [ 11003.611100, 42102.500000],
   [ 11108.611100, 42373.888900],
   [ 11133.333300, 42885.833300],
   [ 11155.833300, 42712.500000],
   [ 11183.333300, 42933.333300],
   [ 11297.500000, 42853.333300],
   [ 11310.277800, 42929.444400],
   [ 11416.666700, 42983.333300],
   [ 11423.888900, 43000.277800]
])

#distance( [ 2, 3],  [ -2, -2])

distanceArray = []
Ref_point = locations[0]

TPS_solver(locations, distanceArray, Ref_point)