from sympy.stats import DiscreteMarkovChain, TransitionMatrixOf, P, E
from sympy import Matrix, MatrixSymbol, Eq, symbols
import matplotlib.pyplot as plt
import numpy as np

#DiscreteMarkovChain, TransitionMatrixOf, P, E
#from sympy import Matrix, MatrixSymbol, Eq, symbols
T = Matrix([[0.5, 0.2, 0.3],[0.2, 0.5, 0.3],[0.2, 0.3, 0.5]])
Y = DiscreteMarkovChain("Y", [0, 1, 2], T)
YS = DiscreteMarkovChain("Y")
TS = MatrixSymbol('T', 3, 3)
P(Eq(YS[1], 1), Eq(YS[1], 1) & TransitionMatrixOf(YS, TS))
#T[0, 2]*T[1, 0] + T[1, 1]*T[1, 2] + T[1, 2]*T[2, 2]
#P(Eq(Y[3], 2), Eq(Y[1], 1)).round(2)

#print(P(Eq(Y[3], 2), Eq(Y[1], 2),Eq(Y[1], 2)).round(2))

