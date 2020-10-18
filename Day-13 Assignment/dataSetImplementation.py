import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
import inspect


print("Pandas Version:", pd.__version__)
print("Numpy Version:", np.__version__)
print("Matplotlib Version:", matplotlib.__version__)
print("Seaborn Version:", sns.__version__)


creditCard = pd.read_csv('creditcard.csv')

pd.options.display.max_rows = 100
pd.options.display.max_columns = 100

print(inspect.getfullargspec(pd.value_counts))

print("\nPrinting head data:\n", creditCard.head())
print("\nPrinting head 10 data:\n", creditCard.head(10))
print("\nPrinting tail data:\n", creditCard.tail())
print("\nPrinting tail 10 data:\n", creditCard.tail(10))
print("\nPrinting describe data:\n", creditCard['Amount'].describe())
print("\nPrinting max amount:", creditCard['Amount'].max())
print("\nPrinting amount value_counts data:\n", creditCard['Amount'].value_counts(normalize=True))
print("\nPrinting credit card info data:\n", creditCard.info())
print("\nPrinting credit card filter data:\n", creditCard.filter(['Time', 'Amount', 'Class']))

plt.boxplot(creditCard['Amount'])
plt.show()