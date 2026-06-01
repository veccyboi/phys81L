import numpy as np

data = np.load("./data/mokudata_20260602_040646.npy")
arr = [a[1] for a in data]
print(arr)