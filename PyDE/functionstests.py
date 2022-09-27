import numpy as np
import matplotlib as plt
from core import Integrate

#Exponential function integration

x : float = 0.0
current_y: float = 1.0 
step: float = 0.01

while (x < 5):

    exp_real = np.exp(x + step)
    exp_de = Integrate((current_y, ), (x, ), (lambda t,y: y, ), "Euler", step)

    current_y = exp_de
    x += step

    error = exp_real - exp_de[0]

    print(f"Real:{exp_real}   Solver:{exp_de[0]}   Error: {error}")

