# giảm về 3 chiều
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('plot3d.csv')
centers = pd.read_csv('centers3d.csv')

fig = plt.figure(figsize = (16, 9))
ax = plt.axes(projection ="3d")

for col, cl in zip([0, 1, 2], ['r', 'g', 'b']):
    ax.scatter3D(df[df.c==col].x, df[df.c==col].y, df[df.c==col].z, c=cl, label=f'{col}')
plt.legend()
ax.scatter3D(centers.x, centers.y, centers.z, color = "black", marker='*', s=300)
plt.title("Giảm về 3 chiều")
plt.show()