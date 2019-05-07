import numpy as np
#import pandas as pd
import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt

print(matplotlib.get_backend())
values=np.cumsum(np.random.randn(1000, 1))
plt.plot(values)
plt.show()
