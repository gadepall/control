import numpy as np
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