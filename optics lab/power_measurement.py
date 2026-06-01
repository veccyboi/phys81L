import numpy as np

redData = np.loadtxt('data/red.csv', delimiter=',')[:,1]
greenData = np.loadtxt('data/green.csv', delimiter=',')[:,1]
backgroundData = np.loadtxt('data/background.csv', delimiter=',')[:,1]

redMean = np.mean(redData)
greenMean = np.mean(greenData)
backgroundMean = np.mean(backgroundData)
redStdErr = np.std(redData, ddof=1)/np.sqrt(len(redData))
greenStdErr = np.std(greenData, ddof=1)/np.sqrt(len(greenData))
backgroundStdErr = np.std(backgroundData, ddof=1)/np.sqrt(len(backgroundData))

R = 100
ρAt639 = 0.424 + (0.448-0.424) * (639-620)/(20)
ρAt520 = 0.309

def P(V, R, ρ):
    return V/(R * ρ)
def dPdV(R, ρ):
    return 1/(R * ρ)


print(f"power of the red laser is {P(redMean, R, ρAt639):.3g} ± {redStdErr * dPdV(R, ρAt639):.3g}")
print(f"power of the green laser is {P(greenMean, R, ρAt520):.3g} ± {greenStdErr * dPdV(R, ρAt520):.3g}")
print(f"background power: {P(backgroundMean, R, 0.426)} ± {np.std(backgroundData, ddof=1):.3g}")


print(f"{backgroundMean:.7g} ± {backgroundStdErr:.7g}")