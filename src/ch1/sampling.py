
import numpy as np
import matplotlib.pyplot as plot
 
# Get x values of the sine wave
time        = np.arange(0, 10, 0.1);

# Amplitude of the sine wave 
amplitude   = np.sin(time)

# Plot a sine wave using time and amplitude obtained for the sine wave
plot.plot(time, amplitude)


# Give a title for the sine wave plot

plot.title('Sine wave')

 

# Give x axis label for the sine wave plot

plot.xlabel('Time')

 

# Give y axis label for the sine wave plot

plot.ylabel('Amplitude = sin(time)')

 

plot.grid(True, which='both')

 

plot.axhline(y=0, color='k')

 

plot.show()


import matplotlib.pyplot as plt

f = plt.figure()
plt.plot(range(10), range(10), "o")
plt.show()

f.savefig("./book/figures/ch1-image1.pdf", bbox_inches='tight')

