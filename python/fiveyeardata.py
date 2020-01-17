import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('gapminder-FiveYearData.csv')
plot1 = pd.pivot_table(data, index=['continent'], values=['lifeExp'], columns=['year'])
sns.heatmap(plot1, linewidths=0.5).get_figure().savefig('myfig.png')

