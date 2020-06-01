# Released under GNU-GPL
# By B Sai Laxman
# Dt.30th May

import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end

#Loading the data
data = np.loadtxt( 'ee18btech11049_1.dat' )
#PLotting the data from spice simulation
plt.plot(data[:,0],data[:,1])
#plt.xlim(0,0.01)
plt.xlabel('time')
plt.ylabel('Vout')
# plt.title('Output from Oscillator -- R2/R1 = 2.35')

#if using termux
plt.savefig('./figs/ee18btech11049/ee18btech11049_1.pdf')
plt.savefig('./figs/ee18btech11049/ee18btech11049_2.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11049_1.pdf"))
# plt.show()
