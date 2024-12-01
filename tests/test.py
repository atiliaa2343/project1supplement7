import unittest 
from plot import plot_normal, plot_line, plot_live 

class TestPlotFunctions(unittest.TestCase): 
    """ 
    This class will be used for plotting functions in the 'plot' module 

    This test class tests the functionality of the functions: 
    - `plot_normal`: Plots 200 points sampled from a standard normal distribution 
    - `plot_line`: Plots a line given its slope, y-intercept, and x-boundaries 
    - `plot_live`: Generates live points and updates a graph.
    
    """
    def test_normal(self): 
        try: 
            plot_normal() 
        except Exception as e: 
            self.fail(f"plot_normal() raised an exception: {e}") 

    def test_line(self): 
        try: 
            plot_line(5,10,7,15) 
        except Exception as e: 
            self.fail(f"plot_line() raised an exception{e}") 

    def test_plot_live(self): 
        try: 
            plot_live(distribution="normal", mean=0,stddev =1, duration=2) 
        except Exception as e: 
            self.fail(f"plot_live() raised an exception: {e}") 

if __name__ == "__plot__": 
    unittest