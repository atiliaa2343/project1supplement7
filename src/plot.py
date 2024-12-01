import matplotlib.pyplot as plt 
import numpy as np 
import time 

def plot_normal(): 
    points = np.random.normal(0,1,200) 
    plt.scatter(range(len(points)), points, label="Standard Normal Points")
    plt.axhline(0, color="blue", linestyle='--', linewidth=0.8, label="Mean") 
    plt.title("200 Points Sample from Standard Normal Distribution") 
    plt.xlabel("Index") 
    plt.ylabel("Value") 
    plt.legend() 
    plt.show()  

def plot_line(y_intercept, slope, lower_x, upper_x): 
    x = np.linspace(lower_x, upper_x, 100) 
    y = slope * x + y_intercept 
    plt.plot(x, y, label=f"y = {slope}x + {y_intercept}") 
    plt.xlim((lower_x, upper_x)) 
    plt.ylim(min(y), max(y)) 
    plt.title("Line Plot") 
    plt.xlabel("x") 
    plt.ylabel("y") 
    plt.legend() 
    plt.show()

def plot_live(distribution="normal", mean=0, stddev=1, duration=10): 
    points = []
    plt.ion() 
    fig, ax = plt.subplots() 

    for _ in range(duration): 
        if distribution == "normal": 
            point = np.random.normal(mean, stddev) 
        elif distribution == "uniform": 
            point = np.random.uniform(mean, stddev) 
        else: 
            raise ValueError("It could not be distributed, use either normal or uniform") 
        points.append(point) 

        if len(points) > 10: 
            points.pop(0) 

        ax.clear()
        ax.plot(points, marker="o", linestyle='-', label="Live Points") 
        ax.set_title("Live Point Generation") 
        ax.set_xlabel("Point Index") 
        ax.set_ylabel("Value") 
        ax.legend() 
        plt.pause(1) 
    plt
