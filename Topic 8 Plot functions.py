import matplotlib.pyplot as plt # Import Required Modules 
import numpy as np

x = np.arange(0, 4, 0.1) # Set a-axis values, increments of "0.1" provdies a smoother graph

y1 = x  # Set y-axis Values
y2= x**2
y3 = x**3

plt.plot(y1, label = '$f(x) = x$') # Plot the provided points and label them in relation to their function
plt.plot(y2, label = '$g(x) = x^2$')
plt.plot(y3, label = '$h(x) = x^3$')

# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 

plt.legend() # Provides Legend
plt.title('Representation of functions $f(x) = x$, $g(x) = x^2$, $h(x) = x^3$, within range [0,4]  ')
plt.show() # Depicts graphic representation of the plot
