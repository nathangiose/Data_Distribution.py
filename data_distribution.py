# Nathan John Giose


marks=[70, 45, 90, 12]
names=["Mpendulo", "Godwin", "Thando", "Thabo"]

# Importing numpy and represent it as np

import numpy as np


# Import matplotlib and representing it as plt


import matplotlib.pyplot as plt

marks = np.array([70, 45, 90, 12])
names = np.array(["Mpendulo", "Godwin", "Thando", "Thabo"])
plt.bar(names, marks)
plt.show()
