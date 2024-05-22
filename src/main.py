import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
import os
import valores_alternativos as va
from function import Function as Fx
from Euler import Euler_Method
from Euler_Melhorado import Improved_Method

inicial = (0, 1)
intervalo = (0, 5)
Funx = Fx(inicial, intervalo, 30)

Funx.Euler.make.graph()