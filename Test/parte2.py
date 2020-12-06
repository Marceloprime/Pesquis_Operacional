from ortools . linear_solver import pywraplp
import numpy as np


def get_costs ( points ):
    N = points . shape [0]
    costs = np . array ([[ dist ( points [i ,:] , points [j ,:]) for i in
    range (N ) ] for j in range ( N ) ])
    return costs


def tsp_solver ( points ):
    solver = pywraplp . Solver . CreateSolver ('SCIP')
    costs = get_costs ( points )
    N = points . shape [0]

    x = [[ None for i in range (N ) ] for j in range ( N )]
    for i in range ( N ):
        for j in range ( N ):
            x[ i ][ j] = solver . IntVar (0.0 , 1.0 , f"x [{ i } ,{ j }] ")

    y = [ None for i in range ( N ) ]
    for i in range ( N ):
        y[ i ] = solver . IntVar (0.0 , solver . infinity () , f"y [{ i }] ")

    for k in range ( N ):
        row_constraint = solver . RowConstraint (1 , 1)
        col_constraint = solver . RowConstraint (1 , 1)
        for i in range ( N ):
            for j in range ( N ):
                row_constraint . SetCoefficient (x [ i ][ j ], int (k == i and i != j) )
                col_constraint . SetCoefficient (x [ i ][ j ], int (k == j and i != j) )

    for i in range (1 , N ) :
        for j in range (1 , N ):
            if j == i: continue
            solver . Add (y [i] - ( N) * x [ i ][ j ] - y [ j] + (N - 1) >= 0)

    solver . SetTimeLimit (300000)

    objective = solver . Objective ()
    for i in range ( N ):
        for j in range ( N ):
            objective . SetCoefficient (x [i ][ j] , costs [ i ][ j ])
    objective . SetMinimization ()

    solver . Solve ()
    adj_matrix = [ [ int (x [i ][ j ]. solution_value () ) for i in range (N
    ) ] for j in range ( N ) ]
    return adj_matrix

locations = [
    11003.611100, 42102.500000,
    11108.611100, 42373.888900,
    11133.333300, 42885.833300,
    11155.833300, 42712.500000,
    11183.333300, 42933.333300,
    11297.500000, 42853.333300,
    11310.277800, 42929.444400,
    11416.666700, 42983.333300,
    11423.888900, 43000.277800,
    11438.333300, 42057.222200,
    11461.111100, 43252.777800,
    11485.555600, 43187.222200,
    11503.055600, 42855.277800,
    11511.388900, 42106.388900,
    11522.222200, 42841.944400,
    11569.444400, 43136.666700,
    11583.333300, 43150.000000,
    11595.000000, 43148.055600,
    11600.000000, 43150.000000,
    11690.555600, 42686.666700,
    11715.833300, 41836.111100,
    11751.111100, 42814.444400,
    11770.277800, 42651.944400,
    11785.277800, 42884.444400,
    11822.777800, 42673.611100,
    11846.944400, 42660.555600,
    11963.055600, 43290.555600,
    11973.055600, 43026.111100,
    12058.333300, 42195.555600,
    12149.444400, 42477.500000,
    12286.944400, 43355.555600,
    12300.000000, 42433.333300,
    12355.833300, 43156.388900,
    12363.333300, 43189.166700,
    12372.777800, 42711.388900,
    12386.666700, 43334.722200,
]