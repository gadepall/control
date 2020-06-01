import matplotlib.pyplot as plt
import pandas as pd
#if using termux
import subprocess
import shlex

data = pd.read_csv('./codes/ee18btech11051/spice/ee18btech11051_data.txt', sep="\t", header=None)

data[0] = data[0].astype(float)
data[1] = data[1].astype(float)
data.plot.line(x=0,y=1)
plt.xlabel("t")
plt.ylabel("V_Out")
plt.title("Spice Simulation")

#if using termux
plt.savefig('./figs/ee18btech11051/ee18btech11051_plot2.pdf')
plt.savefig('./figs/ee18btech11051/ee18btech11051_plot2.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11051/ee18btech11051_plot2.pdf"))
#plt.show()
