import pandas as pd
datas1 = [1.2, 2.3, 1.5, 2, 3, 1.8, 1.4, 2.5]
datas2 = pd.Series(datas1)
print(datas2.mean())
