import pandas as pd

data = pd.read_csv("gastro21.csv", header=None).T
data.columns = ["Nazwa", "Rok", "Wartość"]
data["Rok"] = pd.Series(data["Rok"], dtype=int)