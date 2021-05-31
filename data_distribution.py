marks=[70, 45, 90, 12]
names=["Mpendulo", "Godwin", "Thando", "Thabo"]

import numpy as np
import matplotlib.pyplot as plt

marks = np.array([70, 45, 90, 12])
names = np.array(["Mpendulo", "Godwin", "Thando", "Thabo"])
plt.bar(names, marks)
plt.show()
