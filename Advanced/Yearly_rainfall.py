import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("Seattle2014.csv")

Rainfall = data["PRCP"].values
Inches = Rainfall/254

print(f"Number of days without Rainfall {np.sum(Inches== 0)}")
print(f"Number of days with Rainfall {np.sum(Inches != 0)}")
print(f"Number of days with rain more than 0.5 inches:{np.sum(Inches>0.5)}")
print(f"Number of days with rain < 0.2 inches:{np.sum((Inches > 0)& (Inches < 0.2))}")

plt.hist(Inches,40)
plt.title("Rainfall")
plt.show()