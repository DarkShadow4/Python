# Regla de Scott

import pandas as pd
import numpy as np
import math

crabs = pd.read_table("../../../../r-basic/data/datacrab.txt", sep = " ")
cw = crabs.width
n = len(cw)
precision = 0.1

# Número de clases

As = 3.5*np.std(cw)*n**(-1/3)
Ks = math.ceil((max(cw)-min(cw))/As)

# Amplitud de clases (precisión a décimas)

A = round((max(cw)-min(cw))/Ks, 1) + precision

# Establecer limites de intervalos

L1 = min(cw)-1/2*precision
L = [L1]
for lim in range(Ks+1):
    L.append(round(L1+A*(lim+1), 2))
L
X = []
for lim in range(len(L)-2):
    X.append(round((L[lim]+L[lim+1])/2, 1))
X


# Regla de la raíz

import pandas as pd
import numpy as np
import math

crabs = pd.read_table("../../../../r-basic/data/datacrab.txt", sep = " ")
cw = crabs.width
n = len(cw)
precision = 0.1

# Número de clases

Kr = math.ceil(math.sqrt(n))

# Amplitud de clases (precisión a décimas)

A = round((max(cw)-min(cw))/Kr, 1) + precision

# Establecer limites de intervalos

L1 = min(cw)-1/2*precision
L = [L1]
for lim in range(Kr+1):
    L.append(round(L1+A*(lim+1), 2))
L
X = []
for lim in range(len(L)-2):
    X.append(round((L[lim]+L[lim+1])/2, 1))
X

# Regla de Sturges

import pandas as pd
import numpy as np
import math

crabs = pd.read_table("../../../../r-basic/data/datacrab.txt", sep = " ")
cw = crabs.width
n = len(cw)
precision = 0.1

# Número de clases

KS = math.ceil(1+np.log2(n))

# Amplitud de clases (precisión a décimas)

A = round((max(cw)-min(cw))/KS, 1) + precision

# Establecer limites de intervalos
L1 = min(cw)-1/2*precision
L = [L1]
for lim in range(KS+1):
    L.append(round(L1+A*(lim+1), 2))
L
X = []
for lim in range(len(L)-2):
    X.append(round((L[lim]+L[lim+1])/2, 1))
X

# Regla de Freedman-Diaconis

import pandas as pd
import numpy as np
import math

crabs = pd.read_table("../../../../r-basic/data/datacrab.txt", sep = " ")
cw = crabs.width
n = len(cw)
precision = 0.1

# Número de clases

Afd = 2*(np.quantile(cw, 0.75)-np.quantile(cw, 0.25))*n**(-1/3)
Kfd = math.ceil((max(cw)-min(cw))/Afd)

# Amplitud de clases (precisión a décimas)
A = round((max(cw)-min(cw))/Kfd, 1) + precision

# Establecer limites de intervalos
L1 = min(cw)-1/2*precision
L = [L1]
for lim in range(Kfd+1):
    L.append(round(L1+A*(lim+1), 2))
L
X = []
for lim in range(len(L)-2):
    X.append(round((L[lim]+L[lim+1])/2, 1))
X
