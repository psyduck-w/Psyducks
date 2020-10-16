import matplotlib.pyplot as plt  
import numpy as np 
import matplotlib
import math
import mpl_toolkits.axisartist as axisartist
fig = plt.figure(figsize=(8, 8))
ax = axisartist.Subplot(fig, 111)  
fig.add_axes(ax)


ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("->", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
ax.axis["x"].set_axis_direction("top")
ax.axis["y"].set_axis_direction("right")

x = np.arange(-15,15,math.pi)
plt.xlim(-3*math.pi,3*math.pi)
plt.ylim(-5.0,5.0)


x=np.arange(-2*np.pi,2*np.pi,0.01)
y=np.sin(x+1/3*np.pi)
plt.plot(x,y) 
plt.show()