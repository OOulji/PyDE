from .solvers import *
import numpy as np

Integrators = {

    "Euler": EulerSolver,
    "MidPoint" : MidPointSolver

}

def Integrate(initial_conditions: tuple, inital_time: float, functions: tuple, solver: str, time_step: float) -> np.ndarray:

    solverFunction: function = Integrators[solver]

    results: np.ndarray = solverFunction(initial_conditions, inital_time, functions, time_step)
    
    return results
