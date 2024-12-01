import unittest 
from plot import plot_normal, plot_line, plot_live 

class TestPlotFunctions(unittest.TestCase): 
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

    