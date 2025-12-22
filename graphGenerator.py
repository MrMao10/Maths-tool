import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
from lib.menuTest import menu

def exitProgram():
    while True:
                quit = input('Do you want to exit the program? ')
                if quit == 'yes':
                    sys.exit()
                elif quit == 'no':
                    break
                else:
                    print("Not a valid option. Please type yes or no")
                break

#opening 'menu'

print("Welcome to the Graph Generator!")
while True:
    choiceMenu = input('HISTOGRAM       SCATTER PLOT\nLINE GRAPH        BAR CHART\n        PIE CHART        \n').lower()
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
                    break
                elif hasGrid == 'No':
                    plt.show()
                    break
                else:
                    print("Not a valid option. Please type 'yes' for a gridded histogram and 'no' for a non-gridded histogram.")
            exitProgram()
            break
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
            exitProgram()
            break
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
            exitProgram()
            break 
        elif choiceMenu == 'bar chart':
            labels = []
            while True:
                try:
                    qualitativeMeasures = int(input('Enter number of qualatative measures (labels): '))
                    break
                except ValueError:
                    print("You must enter a number")
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
            exitProgram()
            break
        elif choiceMenu == 'pie chart':
            #could get user input through one prompting using the split function like earlier with
            #scatter plot but ask user for each wedge name followed by its value, separated with a comma
            numberOfObjects = int(input('Enter the amount of wedges in your pie (chart): '))
            wedges = []
            for i in range(numberOfObjects):
                wedge = input(f'Enter wedge {i+1} label: ')
                wedges.append(wedge)
            values = []
            for i in range(numberOfObjects):
                valueOfWedge = int(input(f'Enter wedge value {i+1}: '))
                values.append(valueOfWedge)
            values = np.array(values, dtype=int)
            print(wedges, values)
            pieChartTitle = input('Enter your pie chart title: ')
            plt.title(pieChartTitle)
            while True:
                legendOrLabels = input('Do you want a legend or labels on your pie chart? ')
                if legendOrLabels == 'labels':
                    plt.pie(values, labels=wedges, startangle=90)
                    plt.show()
                    break
                elif legendOrLabels == 'legend':
                    plt.pie(values, labels=wedges, startangle=90)
                    plt.legend()
                    plt.show()
                    break
                else:
                    print("Not a valid option. Type labels or legend.")
            exitProgram()
            break
        else:
            print("Not a valid option. Please pick one of the following: Histogram, scatter plot, line graph, or bar chart.")
            break
