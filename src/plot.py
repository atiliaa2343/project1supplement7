import matplotlib.pyplot as plt 
import numpy as np 
import time 

def plot_normal(): 
    """ 
    Generates and displays a scatter plot of 200 points sampled from a standard normal distribution. 

    This function samples 200 data points from a normal distibution with a mean of 0 and 
    a standard deviation of 1. It then plots these points as a scatter plot, with a horizontal 
    line marking the mean (0). 

    The plot includes: 
    - A scatter plot of the data points. 
    - A dashed line at the mean. 
    - Labels for the axes and a legend. 

    Returns: 
        None: Displays the plot in an interactive window.
    
    """
    points = np.random.normal(0,1,200) 
    plt.scatter(range(len(points)), points, label="Standard Normal Points")
    plt.axhline(0, color="blue", linestyle='--', linewidth=0.8, label="Mean") 
    plt.title("200 Points Sample from Standard Normal Distribution") 
    plt.xlabel("Index") 
    plt.ylabel("Value") 
    plt.legend() 
    plt.show()  

def plot_line(y_intercept, slope, lower_x, upper_x):   
    """ 
    Plots a line based on the slope, y-intercept, and x-boundaries. 

    The function calculates the line equation `y = slope * x + y_intercept` over the range 
    defined by `lower_x` and `upper_x`. It then plots the line within this range. 

    Parameters: 
    y_intercept : The y-intercept of the line. 
    slope : The slope of the line 
    lower_x : The lower boundary for the x-axis. 
    upper_x : The upper boundary for the x-axis. 

    Returns: 
        None: Displays the plot in an interactive window. 
    
    """
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
    plt.ioff() 
    plt.show()
