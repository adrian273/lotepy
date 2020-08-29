"""
    @ Numeros de la suerte al azar para jugar el kino de Chile
"""

import random
import csv
from datetime import date, datetime
import time
import numpy as np


lotery_num = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    16, 17, 18, 19, 20,
    21, 22, 23, 24, 25
]

j3 = lotery_num
random.shuffle(j3) 

J3 = j3[:14]


today = date.today()

nnow = str(today)+str(time.time()) 


np.savetxt(nnow + ".csv",
           sorted(J3),
           fmt="%d",
           delimiter=",", footer="Fecha: " + str(datetime.now())
        )