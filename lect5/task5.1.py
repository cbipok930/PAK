import numpy as np
import pandas as pd


def foo(s):
    if isinstance(s, pd.Series):
        s = np.where(s, s > 0.3, 0)
        s.sum()
        s

data = np.random.rand(10, 5)
df = pd.DataFrame(data)
a = df.apply(foo, axis=1)
print(df)
print("g")
