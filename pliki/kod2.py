import pandas as pd

data = pd.read_csv("gastro21.csv", header=None).T
data.columns = ["Typ punktu", "Rok", "Wartość"]
data["Rok"] = pd.Series(data["Rok"], dtype=int)
data["Wartość"] = pd.Series(data["Wartość"], dtype=int)