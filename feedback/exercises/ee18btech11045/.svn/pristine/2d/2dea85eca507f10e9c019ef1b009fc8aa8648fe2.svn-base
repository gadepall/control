import numpy as np  
import matplotlib.pyplot as plt


#if using termux
import subprocess
import shlex
#end if

data=np.loadtxt('ee18btech11045_clresult.dat')  
plt.plot(data[:,0],data[:,1])  


plt.grid()
plt.xlabel("t")
plt.ylabel("Output Voltage")
plt.title('Closed loop Output Voltage')



#if using termux
plt.savefig('./figs/ee18btech11045/ee18btech11045_clresult.pdf')
plt.savefig('./figs/ee18btech11045/ee18btech11045_clresult.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11045/ee18btech11045_clresult.pdf"))
#else
#plt.show()