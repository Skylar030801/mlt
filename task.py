
import numpy as np


array = np.arange(20)
print(array)

r1 = np.mean(array)
print("\nMean: ", r1)

r2 = np.std(array)
print("\nstd: ", r2)

r3 = np.var(array)
print("\nvariance: ", r3)


#CHALLENGE 2

import numpy as np
import matplotlib.pyplot as plt
nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])
bins = np.array([0, 1, 2, 3])
print("nums: ",nums)
print("bins: ",bins)
print("Result:", np.histogram(nums, bins))
plt.hist(nums, bins=bins)
plt.title("Histogram of nums against bins")
plt.show()



