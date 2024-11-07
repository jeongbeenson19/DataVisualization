import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib


cat = ['국어', '영어', '수학', '과학', '사회']
cat = [*cat, cat[0]]

hong = [90, 78, 88, 65, 89]
hong = [*hong, hong[0]]

sung = [80, 98, 78, 95, 80]
sung = [*sung, sung[0]]

lb = np.linspace(0, 2*np.pi, len(cat))

plt.figure(figsize=(8, 8))
ax = plt.subplot(polar=True)
ax.plot(lb, hong, label="홍길동", linestyle="dotted", color="red")
ax.fill(lb, hong, color="red", alpha=0.3)
ax.plot(lb, sung, label="성춘향", linestyle="dashed", color="skyblue")
ax.fill(lb, sung, color="skyblue", alpha=0.3)
ax.legend()
plt.xticks(lb, cat)
plt.show()
