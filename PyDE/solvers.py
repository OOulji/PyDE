from time import time
import numpy as np

def EulerSolver(initial_conditions: tuple, inital_time: tuple, functions: tuple, time_step: float):

        result = np.zeros(len(initial_conditions))

        for idx, dimension in enumerate(initial_conditions):
            fun = functions[idx]
            value = fun(inital_time, dimension)
            result[idx] = dimension + time_step * value

        return result

def MidPointSolver(initial_conditions: tuple, inital_time: tuple, functions: tuple, time_step: float):

        result = np.zeros(len(initial_conditions))

        for idx, dimension in enumerate(initial_conditions):
            fun = functions[idx]
            midPointValue = (time_step/2)*fun(inital_time[idx], dimension)
            value = fun(inital_time[idx] + time_step/2, dimension + midPointValue)
            result[idx] = dimension + time_step * value

        return result
