# Nathan John Giose
# Import matplotlib.pyplot and refer to it as plt


import matplotlib.pyplot as plt
# Insert data for the y and x axis


cities=['East London', 'Cape Town', 'Kimberley', 'Durban']
rainfall= [140,  200, 120, 157]
x_pos = [i for i, _ in enumerate(cities)]
# labels on the x-axis
# labeling and visuals


plt.bar(x_pos, rainfall, color='green')
plt.xlabel("cities")
plt.ylabel("Rainfall in (mm)")
plt.title("Rainfall for the 4 main cities in SA")
plt.xticks(x_pos, cities)
# Present the graphs


plt.show()
