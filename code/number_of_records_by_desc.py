# Author: Joey_Cheng
# Date: 2021 / 4 / 13

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../data/Special-Events-2020.csv")

plt.figure(figsize=(15, 10))
plt.title("Number of Records by Description 2020")
value_counts = data.DESCRIPTION.value_counts(ascending=True)
values = value_counts.values
index = value_counts.index
bars = plt.barh(data.DESCRIPTION.value_counts().index, values, color=["sienna", "olive", "brown", "peru"])

# add annotates
for bar, label in zip(bars, values):
    plt.annotate(label, xy=(label, bar.get_y() + 0.4), ha='left', va='center')

plt.tight_layout()
plt.savefig("../img/Number of Records by Description 2020.png")


