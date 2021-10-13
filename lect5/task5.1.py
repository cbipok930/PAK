import numpy as np
import pandas as pd


def foo(s):
    if isinstance(s, pd.Series):
        cnt = s[s > 0.3].size
        if cnt > 0:
            the_sum = s[s > 0.3].aggregate(sum) / cnt
        else:
            return None
        return the_sum
    return False


data = np.random.rand(10, 5)
df = pd.DataFrame(data)
out = df.apply(foo, axis=1)
print(df)
print(out)

