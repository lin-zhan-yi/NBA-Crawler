# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
 
# Set data
df=pd.read_csv("0032100001.csv")
df=df.sort_values(by="Points",ascending=False,ignore_index=True)
df=df.drop(columns=["Points","Turnovers","ftp","fgp","tpp","Minutes"])

#df = pd.DataFrame({
#'group': ['LeBron','Curry','Paul','Antetokoumpo','Green','Poole',],
#'minutes': [38, 1.5, 30, 4, 5, 32,],
#'points': [29, 10, 9, 34, 5, 45,],
#'assists': [8, 39, 23, 24, 5, 45,],
#'rebounds': [7, 31, 33, 14, 5, 13,],
#'steals': [28, 15, 32, 14, 5, 15,],
#'blocks': [28, 15, 32, 14, 5,7,],
#})
 
# ------- PART 1: Define a function that do a plot for one line of the dataset!
 
def make_spider( row, title, color):
    amount = len(df["Player name"])
    import math
    column_amount = math.sqrt(amount)
    column_amount = int(math.ceil(column_amount))

    # number of variable
    categories=list(df)[1:]
    N = len(categories)

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    ax = plt.subplot(column_amount,column_amount,row+1, polar=True, )

    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=8)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([1,4,7], ["1","4","7"], color="grey", size=7)
    plt.ylim(0,10)

    # Ind1
    values=df.loc[row].drop('Player name').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, color=color, linewidth=2, linestyle='solid')
    ax.fill(angles, values, color=color, alpha=0.4)

    # Add a title
    plt.title(title, size=11, color=color, y=1.1)

    
# ------- PART 2: Apply the function to all individuals
# initialize the figure
my_dpi=110
plt.figure(figsize=(5000/my_dpi, 1600/my_dpi), dpi=my_dpi)
 
# Create a color palette:
my_palette = plt.cm.get_cmap("Set2", len(df.index))
 
# Loop to plot
for row in range(0, len(df.index)):
    make_spider( row=row, title=''+df['Player name'][row], color=my_palette(row))

plt.show()
