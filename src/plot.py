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

