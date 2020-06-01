from scipy import signal
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

s1 = signal.lti([10**7,2*(10**(11)),10**(15)], [1, 3*(10**4),3*(10**8),2*(10**(12))])
w, mag, phase = signal.bode(s1)

plt.subplot(2,1,1)
plt.semilogx(w, mag)    # Bode magnitude plot
plt.xlabel('Freq')
plt.ylabel('Magnitude')

plt.subplot(2,1,2)
plt.semilogx(w, phase)  # Bode phase plot
plt.xlabel('Freq')
plt.ylabel('Phase')

#if using termux
plt.savefig('./figs/ee18btech11038/ee18btech11038_bode.pdf')
plt.savefig('./figs/ee18btech11038/ee18btech11038_bode.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11038_bode.pdf"))
# plt.savefig('./ee18btech11038_bode.pdf')
# plt.savefig('./ee18btech11038_bode.eps')

#else
# plt.show()