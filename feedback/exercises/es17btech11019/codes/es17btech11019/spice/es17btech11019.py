import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

data1 = np.loadtxt('open_loop_gain.dat.data')

plt.plot(data1[:,0],data1[:,1])
plt.grid()


plt.xlabel("Time")
plt.ylabel("gain")
plt.title("Open loop gain")

# if using termux
plt.savefig('./figs/es17btech11019/Gain.pdf')
plt.savefig('./figs/es17btech11019/Gain.eps')
subprocess.run(shlex.split("termux-open ./figs/es17btech11019/Gain.pdf"))
# else
#plt.show()




data2 = np.loadtxt('feedback_gain.dat.data')
plt.plot(data2[:,0],data2[:,1])
plt.grid()

plt.xlabel("Time")
plt.ylabel("feedback factor")
plt.title("Feedback factor ")

# if using termux
plt.savefig('./figs/es17btech11019/feedbackfactor.pdf')
plt.savefig('./figs/es17btech11019/feedbackfactor.eps')
subprocess.run(shlex.split("termux-open ./figs/es17btech11019/feedbackfactor.pdf"))
# else
#plt.show()



