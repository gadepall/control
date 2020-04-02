import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
def CalculatePolesAndZeros(Slopes):
	dSlopes = Slopes[1:]-Slopes[:-1]
	Nz=0
	Np=0
	for i in dSlopes:
		if i%20!=0:
			return None
		if i>=0 :
			Nz+=i//20
		else:
			Np -= i//20
	return Np, Nz


Slopes = np.array([0,-20,-60,-40,0,-40,-60])
Np,Nz = CalculatePolesAndZeros(Slopes)
print("Number of Poles : " , Np)
print("Number of Zeros : " , Nz)

def getTransferFunction(Slopes):
    dSlopes = Slopes[1:]-Slopes[:-1]
    Num = []
    Den = []
    for i in range(len(dSlopes)):
        if dSlopes[i]%20!=0:
            return None
        if dSlopes[i]>=0 :
            Num += [10**(i+1)]*(dSlopes[i]//20)
        else:
            Den += [10**(i+1)]*(-dSlopes[i]//20)
        
    
    return np.array(Num),np.array(Den)

Num,Den =  getTransferFunction(Slopes)
s1 = signal.lti(Num,Den,1e15) 
w, mag, phase = signal.bode(s1)
plt.figure()
plt.xlabel("f")
plt.ylabel("H(f)")
plt.title("Bode Plot")
plt.semilogx(w, mag)    # Bode magnitude plot
 

x = np.array([1,10,100,1000,10000,1e5,1e6,1e7])
y = []
k = 100
for i in range(len(x)-1):
    
    y.append(k)
    k+=Slopes[i]
y.append(k)
plt.plot(x,y)
 
plt.legend(["Calculated Plot" , "Given Plot"]) 
