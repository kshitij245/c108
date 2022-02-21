import random
import plotly.figure_factory as ff
dice_Result=[]
count=[]
for i in range(0,100):

    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_Result.append(dice1+dice2)
    count.append(i)

fig=ff.create_distplot([dice_Result],["result"])
fig.show()

