from sympy.solvers import solve
from sympy import Symbol
from typing import List

class BetVsOneself:

    def __init__(self, b1: float, b2: float):
        """
        
        """
        assert all([b1 > 1, b2 > 1]), 'all decimal odds must be larger than one'

        solverSolution = self.equallyWeight(b1, b2)
        x1 = solverSolution['x1']
        x2 = solverSolution['x2']
        self.x1, self.x2 = x1, x2

        self.profit        = (b1 * x1 + b2 * x2) / 2
        self.excess_return = self.profit - 1
        self.arbitrage     = self.excess_return > 0
        self.implied_prob  = list(map(self.impliedProbabilities, [b1, b2]))


    def equallyWeight(self, b1: float, b2: float) -> dict:

        x1 = Symbol('x1')
        x2 = Symbol('x2')

        solution = solve((b1 * x1 - b2 * x2, x1 + x2 - 1), x1, x2, dict=True)
        
        return {str(key):val for key, val in solution[0].items()}

    def impliedProbabilities(self, decimal_odds: float):
        """
        https://www.bettingexpert.com/da/academy/avanceret-betting-teori/saadan-konverterer-du-odds-implicit-sandsynlighed#gref
        """
        return 1 / decimal_odds