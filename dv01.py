import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams["figure.figsize"] = [10, 6]

labels = ["A", "B", "C", "D"]
values = [3, 7, 1, 9]

# plt.bar(labels, values)
# plt.title("Bar Chart")
# plt.xlabel("Labels")
# plt.ylabel("Values")
# plt.show()

# sns.barplot(x=labels, y=values)
# plt.title("SNS Bar Charts")
# plt.show()

# sns.barplot(x=values, y=labels, orient="h")
# plt.title("SNS Bar Charts")
# plt.show()

data = {
    "Labels": ["A", "A", "B", "B", "C", "C", "D", "D"],
    "Values": [4, 3, 5, 7, 9, 3, 6, 2],
    "Group": ["G1", "G2", "G1", "G2", "G1", "G2", "G1", "G2"],
}

df = pd.DataFrame(data)

# plt.figure()
# plt.subplot(2, 1, 1)
# sns.barplot(data=df[df["Group"] == "G1"], x="Labels", y="Values")
# plt.subplot(2, 1, 2)
# sns.barplot(data=df[df["Group"] == "G2"], x="Labels", y="Values")
# plt.show()

# plt.figure()
# sns.barplot(data=df, x="Labels", y="Values", hue="Group")
# plt.show()

# plt.figure()
# sns.barplot(data=df[df["Group"] == "G1"], x="Labels", y="Values", label="G1", color="b")
# sns.barplot(data=df[df["Group"] == "G2"], x="Labels", y="Values", label="G2", color="r",
#             bottom=df[df["Group"] == "G1"]["Values"])
# plt.legend()

# sns.barplot(x="Labels", y="Values", data=df)
# plt.show()


