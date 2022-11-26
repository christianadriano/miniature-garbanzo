from sympy.stats import DiscreteMarkovChain, P
from sympy import Gt, Le, Rational
from sympy import Matrix, MatrixSymbol, Eq, symbols

T = Matrix([[Rational(5, 10), Rational(3, 10), Rational(2, 10)], [Rational(2, 10), Rational(7, 10), Rational(1, 10)], [Rational(3, 10), Rational(3, 10), Rational(4, 10)]])
Y = DiscreteMarkovChain("Y", [0, 1, 2], T)
print(P(Eq(Y[3], Y[1]), Eq(Y[0], 0)).round(3))
print(P(Gt(Y[3], Y[1]), Eq(Y[0], 0)).round(2))
print(P(Le(Y[15], Y[10]), Eq(Y[8], 2)).round(7))