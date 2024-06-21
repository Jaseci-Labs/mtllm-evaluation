import pandas as pd
df = pd.read_csv("ModelSweep-19-06-2024-1820.csv")
print(df["ExactMatch"].mean())
