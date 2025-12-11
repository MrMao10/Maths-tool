import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import colors
from matplotlib.ticker import PercentFormatter


histogramTitle = input('Enter histogram title: ')
xAxisLabel = input('Enter x axis label: ')
densityCurve = input('Do you want a density plot on your histogram? ').capitalize()
manualData = input('Do you want to enter your own data or have it generated based on your parameters?(A or B)').capitalize()
if manualData == 'A':
    data = list(map(int, input('Enter your numbers, separated by spaces: ').split()))
elif manualData == 'B':
    minimumData = int(input('Enter minimum data bound: '))
    maximumData = int(input('Enter maximum data bound: '))
    sampleSize = int(input('Enter total data size (total frequency): '))
    a = (minimumData + maximumData) / 2
    data = np.random.normal(a, ((maximumData-a) + (a-minimumData)) /2, sampleSize)
print(data)

if densityCurve == 'Yes':
    sns.histplot(data, bins='fd', kde=True, color="orange")
else:
    pass

plt.hist(data, bins='fd', edgecolor="black")
plt.xlabel(xAxisLabel)
plt.ylabel("Frequency")
plt.title(histogramTitle)
hasGrid = input('Do you want your histogram to be lined? ').capitalize()
if hasGrid == 'yes':
    plt.grid()
else:
    pass

plt.show()