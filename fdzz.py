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
t=np.linspace(-3.0,3.0,1000)
plt.ylim(-4,4)
f=2*np.exp((complex(-0.5,8))*-t)
plt.plot(t,np.real(f))
plt.show()
