import pandas as pd
import matplotlib.pyplot as plt

data_frame = pd.read_table("../../../r-basic/data/datacrab.txt", sep = " ")
data_frame
data_frame.describe()
data_frame.dropna().describe()
