import numpy as np
import pandas as pd

test_data = pd.read_csv('test.csv', index_col=0)
id1 = test_data.index.values
test_array = test_data.values
y = np.mean(test_array, axis=1, dtype=np.float64)
d = {'Id': id1, 'y': y}
df = pd.DataFrame(data=d)
df.to_csv('solution.csv', index=False)

