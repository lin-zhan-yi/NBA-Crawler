import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
df=pd.read_csv("0032100001.csv")
df=df.sort_values(by="Points",ascending=False,ignore_index=True)
name_list=df["Player name"].to_list()
point_list=df["Points"].to_list()

x = np.arange(len(name_list[0:11]))  # the label locations
width = 0.35  # the width of the bars

fig,(ax1,ax2)= plt.subplots(2)
rects1 = ax1.bar(x, point_list[0:11], width, label='Points')
rects2 = ax2.bar(x, point_list[12:23], width, label='Points')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax1.set_ylabel('Scores')
ax1.set_title('Scores by group and gender')
ax1.set_xticks(x, name_list[0:11],fontsize=5)
ax1.legend()

ax2.set_ylabel('Scores')
ax2.set_title('Scores by group and gender')
ax2.set_xticks(x, name_list[12:23],fontsize=5)
ax2.legend()
ax2.bar_label(rects1, padding=3)
#ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()
