import matplotlib.pyplot as plt
import numpy as np

resistanceArr = 1000 * np.array([1., 2.2, 3.3, 4.7, 10.])
resistanceErr = 0.05 * resistanceArr
V0 = 6
V = 2.19
V0Err = 0
VErr = V0Err
tArr = 0.001 * np.array([1.400, 2.600, 3.600, 5.200, 10.40])
tErr = 0.001 * np.array([0.2, 0.2, 0.2, 0.4, 0.4])

def dCdt(t, R, V0, V):
    return 1 / (R * np.log(V0/V))
def dCdR(t, R, V0, V):
    return -t/(R**2 * np.log(V0/V))
def dCdV0(t, R, V0, V):
    return -t/(R * V0 * (np.log(V0/V))**2)
def dCdV(t, R, V0, V):
    return t/(R * V * (np.log(V0/V))**2)

print(str(
np.sqrt( (dCdt(tArr[0], resistanceErr[0], V0, V)*tErr[0])**2
                +(dCdR(tArr[0], resistanceErr[0], V0, V)*resistanceErr[0])**2
                +(dCdV0(tArr[0], resistanceErr[0], V0, V)*V0Err)**2
                +(dCdV(tArr[0], resistanceErr[0], V0, V)*VErr)**2 )
))

CArr = tArr / (resistanceArr * np.log(V0/V))
CErr = np.sqrt( (dCdt(tArr, resistanceErr, V0, V)*tErr)**2
                +(dCdR(tArr, resistanceErr, V0, V)*resistanceErr)**2
                +(dCdV0(tArr, resistanceErr, V0, V)*V0Err)**2
                +(dCdV(tArr, resistanceErr, V0, V)*VErr)**2 )

fig, ax = plt.subplots(figsize=(8, 5))
plt.axhline(y = 1e6 * np.mean(CArr), color = 'tab:red', label=r"mean measured capacitance")
ax.errorbar(x = 1e-3 * resistanceArr, y = 1e6 * CArr, xerr = 1e-3 * resistanceErr, yerr = 1e6 * CErr, fmt='.')

ax.set_xlabel(r"R (kΩ)")
ax.set_ylabel(r"C (μF)")
plt.legend()
fig.tight_layout()
plt.show()

print("C = " + str(1e6 * np.mean(CArr)) + " ± " + str(1e6 * np.mean(CErr)) + " μF")