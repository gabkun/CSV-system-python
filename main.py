import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import os
import plotly.express as px
import matplotlib.patheffects as pe
import sys

while True:
    print("please enter a car prices CSV summary report: ")
    print("A. Minimum Car prices")
    print("B. Car Prices")
    print("C. Maximum Car Prices")
    print("D. Range Car Prices")
    print("E. Total Cars Available")
    print("F. Meters Per Gallon histogram")
    print("G. MPG per Price")
    print("H. MPG average per car")
    print("I. Car Models Available")
    print("J. Car Average MPG per range price")
    print("K. Average MPG highway per max price")
    print("L. Average Stocks Per Month")
    print("X. End program")
    choice = input("Choice: ")
    if choice == 'a' or choice == 'A':
        x = []
        y = []

        with open('carprices.csv', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')

            for row in plots:
                x.append(row[1])
                y.append(str(row[2]))

        plt.bar(x, y, color='g', width=0.72, label="minimum range price")
        plt.xlabel('Type')
        plt.ylabel('Price(dollars)')
        plt.title('Car Prices Minimum')
        plt.legend()
        plt.show()
    if choice == 'b' or choice == 'B':
            x = []
            y = []

            with open('carprices.csv', 'r') as csvfile:
                lines = csv.reader(csvfile, delimiter=',')
                for row in lines:
                    x.append(row[1])
                    y.append(str(row[3]))

            plt.plot(x, y, color='yellow', linestyle='dashed',
                     marker='o', label="price(dollars)")

            plt.xticks(rotation=25)
            plt.xlabel('Vehicle types')
            plt.ylabel('price')
            plt.title('Price range for each type', fontsize=20)
            plt.grid()
            plt.legend()
            plt.show()
    if choice == 'c' or choice == 'C':
        Names = []
        Values = []

        with open('carprices.csv', 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            for row in lines:
                Names.append(row[1])
                Values.append(str(row[4]))

        plt.scatter(Names, Values, color='b', s=100)
        plt.xticks(rotation=25)
        plt.xlabel('Vehicles')
        plt.ylabel('Max Prices')
        plt.title('Maximum Vehicle Prices', fontsize=20)

        plt.show()
    if choice == 'd' or choice == 'D':
        x = []
        y = []

        with open('carprices.csv', 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            for row in lines:
                x.append(row[1])
                y.append(str(row[5]))

        plt.plot(x, y, color='violet', linestyle='dashed',
                 marker='o', label="car price range")

        plt.xticks(rotation=25)
        plt.xlabel('type')
        plt.ylabel('price range')
        plt.title('Price range for every vehicle type', fontsize=20)
        plt.grid()
        plt.legend()
        plt.show()
    if choice == 'e' or choice == 'E':
        y = np.array([7, 10, 8, 7, 11, 5])
        mylabels = ["Small", "Midsize", "Sporty", "Compact", "Large", "Van"]

        plt.pie(y, labels = mylabels, autopct='%1.2f%%',  shadow=True,explode=(0.1, 0.1, 0.1, 0.1, 0.1, 0.1))
        plt.legend(title="Car Types:")
        plt.title('Total Cars Available', fontsize=20)
        plt.show()
    if choice == 'f' or choice == 'F':
        x = []
        y = []

        with open('carprices.csv', 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            for row in lines:
                x.append(row[1])
                y.append(str(row[6]))
        data = np.concatenate((x, y))
        plt.hist(data, color='c', bins=10, label='histogram')
        plt.xlabel("types of vehicles")
        plt.ylabel("MPG CITY")
        plt.title("Histogram MPG")
        plt.show()
    if choice == 'g' or choice == 'G':
        x = []
        y1 = []
        y2 = []
        with open('carprices.csv', 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            for row in lines:
                x.append(row[3])
                y1.append(str(row[7]))
                y2.append(str(row[1]))
        fig, ax = plt.subplots()
        ax.plot(x, y2, color='blue', label='Price per MPG')
        ax.plot(x, y1, color='red', label='Type per MPG(Highway)')

        ax.fill_between(x, y1, y2, where=(y1 > y2), interpolate=True, color='blue', alpha=0.5)
        ax.fill_between(x, y1, y2, where=(y1 < y2), interpolate=True, color='red', alpha=0.5)
        plt.xlabel("Car prices")
        plt.ylabel("MPG(Meters Per Gallon)")
        plt.title("Fill Between of Car prices and MPG")
        plt.legend()
        plt.show()
    if choice == 'h' or choice == 'H':
        x = []
        y1 = []
        y2 = []
        with open('carprices.csv', 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            for row in lines:
                x.append(row[1])
                y1.append(str(row[6]))
                y2.append(str(row[7]))
        fig, ax = plt.subplots()
        line1 = ax.plot(x, y1, color='blue', label='MPG CITY')
        line2 = ax.plot(x, y2, color='red', label='MPG HIGHWAY')

        pe1 = pe.withStroke(linewidth=3, foreground='black')
        pe2 = pe.withStroke(linewidth=3, foreground='black')
        line1[0].set_path_effects([pe1])
        line2[0].set_path_effects([pe2])

        plt.xlabel("car types")
        plt.ylabel("MPG AVERAGE")
        plt.title("MPG average per car")
        plt.legend()
        plt.show()
    if choice == 'i' or choice == 'I':
        x = []
        with open('carprices.csv', 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            for row in lines:
                x.append(row[1])
        plt.stem(x)
        plt.xlabel("Car Model")
        plt.ylabel("Car types")
        plt.title("Car Models")
        plt.show()
    if choice == 'j' or choice == 'J':
        x = []
        y = []

        with open('carprices.csv', 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            for row in lines:
                x.append(row[5])
                y.append(str(row[6]))
        plt.rcdefaults()
        fig, ax = plt.subplots()

        ax.barh(x, y, align='center', color='khaki')
        ax.set_yticks(x)
        ax.invert_yaxis()
        ax.set_xlabel('Miles Per Gallon')
        ax.set_title('Average MPG city per range price')

        plt.show()
    if choice == 'k' or choice == 'K':
        x = []
        y = []

        with open('carprices.csv', 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            for row in lines:
                x.append(row[4])
                y.append(str(row[7]))
        plt.rcdefaults()
        fig, ax = plt.subplots()

        ax.barh(x, y, align='center', color='salmon')
        ax.set_yticks(x)
        ax.invert_yaxis()
        ax.set_xlabel('Miles Per Gallon')
        ax.set_title('Average MPG highway per max price')

        plt.show()
    if choice == 'l' or choice == 'L':
        x = []
        y = []

        with open('carpricessummary.csv', 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            for row in lines:
                x.append(row[1])
                y.append(str(row[2]))
        plt.rcdefaults()
        fig, ax = plt.subplots()

        ax.barh(x, y, align='center', color='r')
        ax.set_yticks(x)
        ax.invert_yaxis()
        ax.set_xlabel('Car types')
        ax.set_title('AVERAGE CAR STOCKS PER MONTH')

        plt.show()
    if choice == 'x' or choice == 'X':
        sys.exit()