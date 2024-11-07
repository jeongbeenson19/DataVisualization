import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
# print(tips.describe())

# 히스토그램
# plt.hist(tips["total_bill"])
# plt.show()

# tips["total_bill"].plot.hist()
# plt.show()

# plt.hist(tips["total_bill"], bins=20)  # 구간 수 설정
# plt.xlabel("Total Bill")
# plt.ylabel("Frequency")
# plt.title("Histogram of Total Bill")
# plt.show()

# 커널 밀도 함수
sns.kdeplot(tips["total_bill"])
plt.show()

# 분포도(distplot)
# sns.distplot(tips["total_bill"])
# plt.show()

# 박스 플롯(boxplot)
# plt.figure(figsize=(5, 5))
# sns.boxplot(y='total_bill', data=tips)
# plt.title('Boxplot of Total Bill')
# plt.show()

# 바이올린 플롯(violin plot)
# plt.figure(figsize=(5, 5))
# sns.violinplot(y='total_bill', data=tips)
# plt.title('Violin Plot of Total Bill')
# plt.show()

# 히트맵(Heatmap)
# tip1 = tips[['total_bill', 'tip', 'size']]
# print(tip1.corr())

# sns.heatmap(tip1.corr(), annot=True)
# plt.show()

# 라인플롯(line plot)
# sns.lineplot(x="size", y="tip", data=tips)
# plt.show()

# sns.lineplot(data=tips, x="total_bill", y="tip")  # 라인 플롯으로 표현하기 어려운 경우(scatter plot으로 대체)
# plt.show()

# 산점도(scatter plot)
# sns.scatterplot(data=tips, x="total_bill", y="tip")
# plt.show()

# 회귀 플롯(regression plot)
# sns.regplot(data=tips, x="total_bill", y="tip")
# plt.show()

space_size = 28*28
print(space_size)