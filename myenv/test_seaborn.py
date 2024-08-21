# test_seaborn.py
import sys
print(sys.executable)  # Should point to your virtual environment's Python executable

import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="darkgrid")
tips = sns.load_dataset("tips")
sns.relplot(x="total_bill", y="tip", data=tips)
plt.show()
