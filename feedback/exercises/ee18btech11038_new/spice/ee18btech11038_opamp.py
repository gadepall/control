# 
import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end

data1 = np.loadtxt( 'ee18btech11038_opampgn.data' )
#PLotting the data from spice simulation
time1 = data1[:, 0]*6.28
value1 = data1[:, 1]
#Loading the data
data = np.loadtxt( 'ee18btech11038_opampph.data' )
#PLotting the data from spice simulation
time  = data[:, 0]*6.28
value = data[:, 1]


plt.subplot(2,1,1)
plt.semilogx(time1,value1)


plt.ylabel('Gain(dB)')
plt.title('Magnitude Plot')


plt.subplot(2,1,2)
plt.semilogx(time,value)


plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
plt.title('Phase Plot')

plt.subplots_adjust(hspace=0.5)
# if using termux
plt.savefig('./figs/ee18btech11038/ee18btech11038_opamp.pdf')
plt.savefig('./figs/ee18btech11038/ee18btech11038_opamp.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11038_opamp.pdf"))
# plt.savefig('./ee18btech11038_freqres.pdf')
# plt.savefig('./ee18btech11038_freqres.eps')

# plt.show()

