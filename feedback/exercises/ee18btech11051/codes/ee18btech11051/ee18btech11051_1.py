import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
#if using termux
import subprocess
import shlex

RC = 8 *(10**-6)

num =  [570000*(RC)**3, 570000*6*(RC)**2, 570000*10*RC, 570000*4]	#describing transfer function
den = [(RC)**3, 6*(RC)**2, 10*RC, 61]
system = signal.lti(num,den)

print(system)
T, y_out = signal.impulse(system)	#Impluse response
print(T)
plt.plot(T,y_out)
plt.grid()
plt.xlabel("time (t)")
plt.title("Impulse system response ")
#if using termux
plt.savefig('./figs/ee18btech11051/ee18btech11051_plot1.pdf')
plt.savefig('./figs/ee18btech11051/ee18btech11051_plot1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11051/ee18btech11051_plot1.pdf"))
#plt.show()
