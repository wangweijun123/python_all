import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# solution script imports
# from solutions import bar_chart_solution_1, bar_chart_solution_2
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()


def bar_chart_test():
    pokemon = pd.read_csv('./data/pokemon.csv')
    print(pokemon.head())


bar_chart_test()