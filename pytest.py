import seaborn as sns
import matplotlib.pyplot as plt

# Seaborn에 내장된 "tips" 데이터셋 불러오기
tips = sns.load_dataset("tips")

# 히스토그램 그리기 (요일별 전체 팁 금액 분포)
sns.histplot(data=tips, x="total_bill", hue="day", kde=True)
plt.title('Distribution of Total Bill by Day')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.show()

# 산점도 그리기 (팁과 전체 결제 금액의 관계)
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex", style="time")
plt.title('Scatter Plot of Tip vs Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()
