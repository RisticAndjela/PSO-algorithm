from mojeOpcije import *
from PSO import *
from ann_criterion import optimality_criterion

import time

start_time = time.time()

opcija1 = mojeOpcije()
PSO(60,opcije=opcija1)


end_time = time.time()
elapsed_time = end_time - start_time
print(f"Minimum je pronadjen za {elapsed_time} sekundi.")
