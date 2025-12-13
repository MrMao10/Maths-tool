import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

#opening 'menu'

print("Welcome to the Graph Generator!")

choiceMenu = input('HISTOGRAM       SCATTER PLOT\nLINE GRAPH        BAR CHART\n').lower()
while True:
    if choiceMenu == 'histogram':
        histogramTitle = input('Enter histogram title: ')
        xAxisLabel = input('Enter x axis label: ')
        yLabel = input('Do you require a y axis label other than "Frequency"? ')
        if yLabel == 'Yes':
            yAxisLabel = input('Enter y axis label: ')
        else:
            yAxisLabel = 'Frequency'
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
        plt.ylabel(yAxisLabel)
        plt.title(histogramTitle)
        while True:
            hasGrid = input('Do you want your histogram to be lined? ').capitalize()
            if hasGrid == 'Yes':
                plt.grid()
                plt.show()
                sys.exit()
            elif hasGrid == 'No':
                plt.show()
                sys.exit()
            else:
                print("Not a valid option. Please type 'yes' for a gridded histogram and 'no' for a non-gridded histogram.")
    elif choiceMenu == 'scatter plot':
        xCoord = []
        yCoord = []
        numberOfPoints = int(input('Enter number of points on scatter plot: '))
        for i in range(numberOfPoints):
            x, y = input(f'Enter plot {i+1}, with the x and y coordinates separated with a comma: ').split(',')
            int(x)
            int(y)
            xCoord.append(x)
            yCoord.append(y)
        xPoints = np.array(xCoord, dtype=int)
        yPoints = np.array(yCoord, dtype=int)
        print(xPoints, yPoints)
        xAxisLabel = input('Enter your x axis label: ')
        yAxisLabel = input('Enter your y axis label: ')
        scatterPlotTitle = input('Enter your scatter plot title: ')
        plt.scatter(xPoints, yPoints, color='blue', label='Test')
        coefficients = np.polyfit(xPoints, yPoints, 1)  # 1 means linear
        slope, intercept = coefficients
        lineOfBestFit = slope * xPoints + intercept
        plt.plot(xPoints, lineOfBestFit, color='red', linestyle='dashed', label='Best Fit Line')
        plt.xlabel(xAxisLabel)
        plt.ylabel(yAxisLabel)
        plt.title(scatterPlotTitle)
        plt.legend()
        plt.grid()
        plt.show()
        sys.exit()
    elif choiceMenu == 'line graph':
        xCoord = []
        yCoord = []
        numberOfPoints = int(input('Enter number of points to plot: '))
        for i in range(numberOfPoints):
            x, y = input(f'Enter point {i+1}, with the x and y coordinates separated with a comma: ').split(',')
            int(x)
            int(y)
            xCoord.append(x)
            yCoord.append(y)
        xPoints = np.array(xCoord, dtype=int)
        yPoints = np.array(yCoord, dtype=int)
        print(xPoints, yPoints)
        xAxisLabel = input('Enter your x axis label: ')
        yAxisLabel = input('Enter your y axis label: ')
        lineGraphTitle = input('Enter your line graph title: ')
        plt.plot(xPoints, yPoints, marker='o')
        plt.xlabel(xAxisLabel)
        plt.ylabel(yAxisLabel)
        plt.title(lineGraphTitle)
        plt.grid()
        plt.show()
        sys.exit()        
    elif choiceMenu == 'bar chart':
        labels = []
        qualitativeMeasures = int(input('Enter number of qualatative measures (labels): '))
        for i in range(qualitativeMeasures):
            qualitativeMeasure = input(f'Enter label {i+1}: ')
            labels.append(qualitativeMeasure)
        counts = []
        for i in range(qualitativeMeasures):
            count = int(input(f'Enter count {i+1}: '))
            counts.append(count)
        labels = np.array(labels, dtype=str)
        counts = np.array(counts, dtype=int)
        print(labels, counts)
        xAxisLabel = input('Enter your x axis label: ')
        yAxisLabel = input('Enter your y axis label: ')
        barChartTitle = input('Enter your bar chart title: ')
        plt.xlabel(xAxisLabel)
        plt.ylabel(yAxisLabel)
        plt.title(barChartTitle)
        plt.bar(labels, counts)
        plt.show()
        sys.exit() 
    else:
        print("Not a valid option. Please pick one of the following: Histogram, scatter plot, line graph, or bar chart.")
