from sympy import *
#DiscreteMarkovChain, TransitionMatrixOf, P, E
#from sympy import Matrix, MatrixSymbol, Eq, symbols
T = Matrix([[0.5, 0.2, 0.3],[0.2, 0.5, 0.3],[0.2, 0.3, 0.5]])
Y = DiscreteMarkovChain("Y", [0, 1, 2], T)
YS = DiscreteMarkovChain("Y")