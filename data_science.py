import numpy as np
import pandas as pd

a = np.array([[4, 8, 15], [16, 23, 42]])

print(a.shape)
print(a[:, 1])
print(a.mean(axis=0))
print(a * 2)
print(a[a > 10])

data = {
    "Name": ["Fatima", "Zainab", "Sakina", "Ahmed", "Sana", "Bilal"],
    "Section": ["A", "A", "B", "B", "A", "B"],
    "City": ["Attock", "Kamra", "Attock", "Kamra", "Attock", "Rawalpindi"],
    "Marks": [85, 72, 90, 65, 58, 78]
}

dfOrbit = pd.DataFrame(data)

print(dfOrbit[dfOrbit["Marks"] > 70])
print(dfOrbit.groupby("Section")["Marks"].mean())

dfOrbit["Grade"] = dfOrbit["Marks"].apply(
    lambda x: "A" if x >= 80 else ("B" if x >= 60 else "C")
)

dfOrbit = dfOrbit.sort_values(by="Marks", ascending=False)
print(dfOrbit)
