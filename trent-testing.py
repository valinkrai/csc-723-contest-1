import numpy as np
import pandas as pd

traindata = pd.read_csv('UNSW_NB15_training-set.csv', header='infer', low_memory=False)
print(traindata.head(5))
