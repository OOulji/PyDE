import numpy as np
import time

import PyDE as pyde

#Exponential function integration

x : float = 0.0
current_y: float = 1.0 
step: float = 0.001
eval_points = 0

start = time.perf_counter()

while (x < 5):

    exp_real = np.exp(x + step)
    exp_de = pyde.Integrate((current_y, ), (x, ), (lambda t,y: y, ), "Euler", step)

    current_y = exp_de
    x += step

    error = exp_real - exp_de[0]

    print(f"Point x = {x+step: .5f} | Real:{exp_real: .5f} | Solver:{exp_de[0]: .5f} | Error: {error: .5f}")
    eval_points += 1

end = time.perf_counter()

print("\n")

print(f" Evaluated points: {eval_points} | Time: {end - start: .3f}")